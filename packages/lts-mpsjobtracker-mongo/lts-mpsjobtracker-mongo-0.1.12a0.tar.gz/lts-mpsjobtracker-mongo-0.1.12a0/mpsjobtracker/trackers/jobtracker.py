import os, json, uuid, jsonschema, datetime, shutil, traceback, fcntl, pymongo
from tenacity import retry, wait_fixed, stop_after_attempt
from pymongo import MongoClient
from bson import ObjectId
from mpsjobtracker.trackers.validator import get_validator

def log_error_and_reraise(msg):
    print(msg)
    traceback.print_exc()
    raise

def mongo_url_from_env():
    '''Pulls mongoDB configuration from a set of known environment vars and returns a db connection URI'''
    mongo_host = os.getenv("MONGO_HOST")
    mongo_username = os.getenv("MONGO_USERNAME")
    mongo_password = os.getenv("MONGO_PASSWORD")
    mongo_db = os.getenv("MONGO_DB")
    mongo_auth_source = os.getenv("MONGO_AUTH_SOURCE", "admin")
    mongo_timeout_ms = os.getenv("MONGO_TIMEOUT_MS", "10000")
    mongo_replica_set = os.getenv("MONGO_REPLICA_SET")
    mongo_ssl = os.getenv("MONGO_SSL")
    mongo_ssl_ca_file = os.getenv("MONGO_SSL_CA_FILE")

    options = "authSource=" + mongo_auth_source + "&connectTimeoutMS=" + mongo_timeout_ms
    if mongo_replica_set is not None:
        options += "&replicaSet="+mongo_replica_set
    if mongo_ssl is not None and mongo_ssl_ca_file is not None:
        options += "&ssl="+mongo_ssl+"&ssl_ca_certs="+mongo_ssl_ca_file

    return "mongodb://"+ mongo_username + ":" + mongo_password + "@" + mongo_host +"/" + mongo_db + "?" + options


class JobTracker():
    """Job tracker file management

    Parameters
    ----------
    job_ticket_id: job ticket ID of an existing tracker file
    job_name: name of the job in the master task list
    """

    def __init__(self):
        self.hostname = os.uname().nodename
        # Absolute path to this script
        self.current_script_dir = os.path.dirname(__file__)
        self.schemas_dir = os.getenv(
            'SCHEMAS_DIR',
            os.path.join(self.current_script_dir, '..', 'schemas') # default to included schemas
        )
        # prevent duplicate file reads per validation
        self.schemas = {}

        self.json_dir = os.getenv(
            'JSON_TEMPLATES_DIR',
            os.path.join(self.current_script_dir, '..', 'json_templates') # default to included templates
        )

        init_data = {
          'hostname': self.hostname,
          'schemas_dir': self.schemas_dir,
          'json_dir': self.json_dir
        }
        print('init_data')
        print(init_data)

        db_url = mongo_url_from_env()

        self.client = MongoClient(db_url)
        self.db = self.client.get_default_database()

    def get_jobs(self, status=None):
        """Return an iterator of all jobs (potentially filtered by status)

        Parameters
        ----------
        status: job_management.job_status, can be singular, list of statuses, or mongo expression valid in field query
        """

        query = {}
        if isinstance(status, (str, dict)):
            query['job_management.job_status'] = status
        elif isinstance(status, (list, tuple,)):
            query['job_management.job_status'] = {"$in": status}
        return self.db.jobtracker.find(query)

    def get_child_jobs(self, job_ticket_id, status=None):
        """Return an iterator of all child jobs of job (optionally filtered by status)

        Parameters
        ----------
        job_ticket_id: str or ObjectId value representing the _id of a job with child jobs
        status: job_management.job_status, can be singular, list of statuses, or mongo expression valid in field query
        """

        query = {"parent_job_ref": ObjectId(job_ticket_id)}
        if isinstance(status, (str, dict)):
            query['job_management.job_status'] = status
        elif isinstance(status, (list, tuple,)):
            query['job_management.job_status'] = {"$in": status}

        return self.db.jobtracker.find(query)

    def count_child_jobs(self, job_ticket_id, status=None):
        """Returns count of all child jobs of job (optionally filtered by status)

         Parameters
        ----------
        job_ticket_id: str or ObjectId value representing the _id of a job with child jobs
        status: job_management.job_status, can be singular, list of statuses, or mongo expression valid in field query
        """
        query = {"parent_job_ref": ObjectId(job_ticket_id)}
        if isinstance(status, (str, dict)):
            query['job_management.job_status'] = status
        elif isinstance(status, (list, tuple,)):
            query['job_management.job_status'] = {"$in": status}

        return self.db.jobtracker.count_documents(query)

    def get_job_directory(self, job_ticket_id):
        """Get (creating if necessary) path to locally mounted storage directory associated with a job."""
        basedir = os.getenv('JOB_DATA_BASEDIR')

        if not basedir:
            raise RuntimeError('Attempted to get job directory without a defined JOB_DATA_BASEDIR')

        job_dir = os.path.join(basedir, str(job_ticket_id))
        os.makedirs(job_dir, exist_ok=True)
        return job_dir


    def get_timestamp_utc_now(self):
        """Get timestamp now in UTC ISO8601 format with timezone (always '+00:00' for UTC timezone) and truncate microseconds"""

        return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc, microsecond=0).isoformat()

    def filter_element_by_property(self, arr, prop, val):
        """
        Filter an element in an array of objects by property name
        Return a list that contains the matching element

        Parameters
        ----------
        arr: array of objects, required
        prop: str, property name
        Val: str, value to match
        """

        return list( filter((lambda x: x[prop] == val), arr))


    def __get_main_step_list(self):
        main_step_list = None
        # Get master task list JSON file
        try:
            with open('{}/{}.json'.format(self.json_dir, 'main_step_list')) as json_file:
                main_step_list = json.load(json_file)
        except Exception as e:
            log_error_and_reraise('Unable to get main step list json file.')

        return main_step_list

    def __create_initial_tracker_document(self):
        initial_tracker_doc = None
        # Get tracker init JSON file
        try:
            with open('{}/{}.json'.format(self.json_dir, 'job_tracker_init')) as json_file:
                initial_tracker_doc = json.load(json_file)
        except Exception as e:
            log_error_and_reraise('Unable to get tracker init json file.')

        return initial_tracker_doc

    def __validate_json_schema(self, schema_filename, file_to_validate):
        """
        Validate JSON schema
        Parameters
        ----------
        schema_filename: name of the json file in the /schemas directory without the file extension
        file_to_validate: a json file to validate
        """

        is_file_valid = False

        # Get JSON validation schema
        if schema_filename not in self.schemas:
            try:
                with open('{}/{}.json'.format(self.schemas_dir, schema_filename)) as json_file:
                    self.schemas[schema_filename] = json.load(json_file)
            except Exception as e:
                log_error_and_reraise('Unable to get json schema file: {traceback.format_exc()}')

        validation_schema = self.schemas[schema_filename]
        validator = get_validator(validation_schema)

        # Validate JSON schema
        try:
            validator.validate(file_to_validate)
        except Exception as e:
            log_error_and_reraise('Unable to validate JSON')
        else:
            is_file_valid = True
        return is_file_valid


    #@retry(wait=wait_fixed(1), stop=stop_after_attempt(10))
    def get_tracker_document(self, job_ticket_id):
        """
        Get job tracker document from mongo


        Parameters
        ----------
        job_ticket_id: job ticket ID of an existing tracker file
        """

        print('*** MPSJOBTRACKER get_tracker_file ***')

        get_tracker_document_data = {
          'job_ticket_id': job_ticket_id
        }

        print('get_tracker_document_data')
        print(get_tracker_document_data)
        # Get tracker file
        if job_ticket_id is None:
            raise Exception("job_tracker_id must be supplied. Value is None.")

        job_ticket_id = ObjectId(job_ticket_id)
        #Return data from Document DB
        return self.db.jobtracker.find_one({"_id": job_ticket_id})



    def init_tracker_document(self, job_name, job_context = None, parent_job_ref = None):
        """Initialize a new tracker file by job name"""

        print('*** MPSJOBTRACKER init_tracker_document ***')
        print('job_name')
        print(job_name)
        print('job_context')
        print(job_context)
        print('parent_job_ticket_id')
        print(str(parent_job_ref))

        # Get initial tracker file
        try:
            initial_tracker_doc = self.__create_initial_tracker_document()
        except Exception as e:
            log_error_and_reraise('Unable to get initial tracker file.')

        print('initial_tracker_doc')
        print(initial_tracker_doc)

        # Get main step list
        main_step_list = self.__get_main_step_list()
        print('main_step_list')
        print(main_step_list)
        # Get steps in main step list by job name
        step_list_for_this_job = self.filter_element_by_property(main_step_list, 'job_name', job_name)

        print('step_list_for_this_job')
        print(step_list_for_this_job)

        steps_error_msg = 'Unable to get steps from main step list job_name {}'.format(job_name)
        if not step_list_for_this_job or len(step_list_for_this_job) < 1:
            raise Exception(steps_error_msg)

        steps = step_list_for_this_job[0].get('steps')
        job_name = step_list_for_this_job[0].get('job_name')

        if steps is None or job_name is None:
            raise Exception(steps_error_msg)

        # Add list of job steps to tracker file
        initial_tracker_doc['job_management']['steps'] = steps
        initial_tracker_doc['job_name'] = job_name

        # Add job ID to tracker file
        if parent_job_ref:
            parent_job_ref = ObjectId(parent_job_ref)
            parent_tracker_document = self.get_tracker_document(parent_job_ref)
            if parent_tracker_document is None:
                raise Exception("Cannot find {} in database".format(str(parent_job_ref)))
            initial_tracker_doc['parent_job_ref'] = parent_job_ref

        # Add created and updated dates to tracker file
        timestamp_utc_now = datetime.datetime.utcnow()
        initial_tracker_doc['last_modified_date'] = initial_tracker_doc['creation_date'] = timestamp_utc_now

        # Add job context to tracker file
        if job_context is not None:
            initial_tracker_doc['context'] = job_context

        print('Add list of job steps to initial_tracker_doc')
        print(initial_tracker_doc)

        # Raises and logs error if invalid
        self.__validate_json_schema('job', initial_tracker_doc)

        # Write initial tracker file
        try:
            print('Default DB')
            print(self.db.name)
            result = self.db.jobtracker.insert_one(initial_tracker_doc)
            initial_tracker_doc["_id"] = result.inserted_id
            print(f"INSERTED ID: {result.inserted_id}")
        except Exception as e:
            log_error_and_reraise('Unable to write initial tracker file to db.')

        return initial_tracker_doc


    def update_timestamp(self, job_ticket_id, now=None, parent_also=False):
        """Update job timestamp file with current timestamp (or passed-in timestamp)

        Parameters
        ----------
        job_ticket_id: job ticket ID of an existing tracker file
        now: datetime to be set
        parent_also: update the parent as well
        """

        print('*** MPSJOBTRACKER update_timestamp ***')
        print('job_ticket_id')
        print(job_ticket_id)

        if job_ticket_id:
            job_ticket_id = ObjectId(job_ticket_id)
            timestamp_utc_now = now or datetime.datetime.utcnow()
            newvalue = {"$set": {"last_modified_date": timestamp_utc_now}}

            #Update the timestamp for the job
            query = {"_id": job_ticket_id}
            res = self.db.jobtracker.update_one(query,newvalue)
            if not res.matched_count:
                raise Exception("Cannot find document for {} in method update_timestamp".format(job_ticket_id))

            #Update the timestamp for the parent ticket if it exists
            tracker_document = self.get_tracker_document(job_ticket_id)
            if parent_also and "parent_job_ref" in tracker_document:
                parent_query = {"_id": tracker_document["parent_job_ref"]}
                res = self.db.jobtracker.update_one(parent_query,newvalue)
                if not res.matched_count:
                    raise Exception("Cannot find parent document {} for document {} in method update_timestamp".format(parent_query["_id"], job_ticket_id))
            return timestamp_utc_now
        else:
            raise Exception("job_tracker_id must be supplied in update_timestamp. Value is None.")



    def get_timestamp(self, job_ticket_id):
        """
        Get last modified datetime from document
        Parameters
        ----------
        job_ticket_id: job ticket ID of an existing tracker file
        """

        # Get tracker file
        tracker_document = self.get_tracker_document(job_ticket_id)
        # Get the timestamp from the document data
        if tracker_document is None:
            raise Exception("Cannot find document for {} in method get_timestamp".format(job_ticket_id))
        return tracker_document['last_modified_date']


    def append_error(self, job_ticket_id, error_msg, exception_msg = None, set_job_failed = True):
        """
        Append a new error to the job tracker file errors_encountered array
        Set job status and previous step status to failed by default,
        this will cause the workflow to move backwards and revert all the steps

        Parameters
        ----------
        job_ticket_id: job ticket ID for the job tracker file to be updated
        error_msg: the error message to append to the job tracker file
        exception_msg (optional): more details about the exception that will be appended to the job tracker file
        set_job_failed (optional, default is True): if True set the job status and previous step status to failed
        """

        print('append_error job_ticket_id {} error_msg {} exception_msg {} set_job_failed {}'.format(job_ticket_id, error_msg, exception_msg, set_job_failed))

        job_ticket_id = ObjectId(job_ticket_id)

        tracker_doc = self.get_tracker_document(job_ticket_id)

        context = tracker_doc["context"]
        errors_encountered_array = context.get('errors_encountered', [])

        error_encountered = error_msg
        if exception_msg:
            error_encountered += ' Exception: ' + exception_msg
        errors_encountered_array.append(error_encountered)

        context['errors_encountered'] = errors_encountered_array

        # Update job status and previous step status
        if set_job_failed:
            self.set_job_status("failed", job_ticket_id, "failed")
        # Update job tracker file on filesystem
        newvalue = {"$set": {"context": context}}
        query = {"_id": job_ticket_id}
        self.db.jobtracker.update_one(query,newvalue)


    def get_job_status(self, job_ticket_id):
        """
        Get the job status
        Job status: job_management.job_status

        Parameters
        ----------
        job_ticket_id: job ticket ID of an existing tracker file
        """

        tracker_document = self.db.jobtracker.find_one({"_id": ObjectId(job_ticket_id)}, {"job_management.job_status": 1})
        #Get the status from the document data
        if tracker_document is None:
            raise Exception("Cannot find document for {} in method get_job_status".format(job_ticket_id))
        return tracker_document['job_management']['job_status']


    def set_job_status(self, status, job_ticket_id, previous_status = "success"):
        """
        Set job status and previous step status
        Update the job tracker file on the filesystem
        Job status: job_management.job_status
        Previous step status: job_management.previous_step_status

        Parameters
        ----------
        status: the job status
        job_ticket_id: job ticket ID of an existing tracker file
        """

        job_ticket_id = ObjectId(job_ticket_id)

        # Get existing tracker doc
        tracker_document = self.get_tracker_document(job_ticket_id)
        if tracker_document is None:
            raise Exception('Unable to get job tracker doc job_ticket_id: {}'.format(job_ticket_id))
        newvalue = {"$set": {"job_management.job_status": status, "job_management.previous_step_status": previous_status, "last_modified_date": datetime.datetime.utcnow()}}
        query = {"_id": job_ticket_id}
        self.db.jobtracker.update_one(query,newvalue)

    def replace_tracker_doc(self, tracker_doc):
        """
        Replace tracker document with contents, relies on _id value in replacement tracker doc.

        Parameters
        ----------
        tracker_doc: a tracker document matching the job.json schema, with an _id value resident in the DB
        """
        query = {"_id": tracker_doc['_id']}
        tracker_doc['last_modified_date'] = datetime.datetime.utcnow()

        # Raise and log error if invalid
        self.__validate_json_schema('job', tracker_doc)

        self.db.jobtracker.replace_one(query, tracker_doc)
        if 'parent_job_ref' in tracker_doc:
            self.update_timestamp(tracker_doc['parent_job_ref'], tracker_doc['last_modified_date'])

        return tracker_doc

    def update_context_data(self, job_ticket_id, property_name, value = None):
        """
        A generic method to update a context property value in an existing tracker file
        Replaces any existing value for the specified property
        Adds a new property if it does not exist already
        Note: This supports updating top-level properties only,
        this does not support updating nested properties currently

        Parameters
        ----------
        job_ticket_id: job ticket ID of an existing tracker file
        property_name: name of the property to be updated
        value: value to set
        """

        job_ticket_id = ObjectId(job_ticket_id)
        now = datetime.datetime.utcnow()

        # Get existing tracker file
        tracker_doc = self.get_tracker_document(job_ticket_id)
        if "context" in tracker_doc:
            context = tracker_doc["context"]
        else:
            context = {}
        context[property_name] = value

        # do update
        query = {"_id": job_ticket_id}
        newvalue = {"$set": {"context": context, "last_modified_date": now}}
        self.db.jobtracker.update_one(query,newvalue)

        # update timestamp on parent
        if "parent_job_ref" in tracker_doc:
            self.update_timestamp(tracker_doc['parent_job_ref'], now)
