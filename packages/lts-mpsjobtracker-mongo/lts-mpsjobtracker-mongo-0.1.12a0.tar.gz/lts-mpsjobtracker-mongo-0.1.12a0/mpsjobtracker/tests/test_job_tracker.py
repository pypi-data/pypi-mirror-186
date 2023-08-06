import sys, os, pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import trackers.jobtracker as jobtracker
from bson import ObjectId
from datetime import timedelta

jt = jobtracker.JobTracker()
SECOND_THRESHOLD=1

class TestJobTracker():
    """
    To run these tests, run the pytest command:
    python -m pytest

    Test filename must start with "test_"
    Test class name must start with "Test"
    Test method name must start with "test_"
    """

    def test_db_connection(self):
        db = jt.client.get_default_database()
        print("Checking DB connection")
        assert db.name == "mps-jobtracker"

    def test_init_asset_tracker_parent_document(self):
        initial_tracker_doc = jt.init_tracker_document("assets", context)
        TestJobTracker.parent_job_ref = initial_tracker_doc["_id"]
        assert TestJobTracker.parent_job_ref is not None
        assert initial_tracker_doc["job_name"] == "assets"
        assert initial_tracker_doc["job_management"]["current_step"] == 1
        assert initial_tracker_doc["job_management"]["job_status"] == "ready"
        assert initial_tracker_doc["job_management"]["previous_step_status"] == "success"

    def test_init_asset_tracker_child_document(self):
        child_tracker_doc = jt.init_tracker_document("assets", context, TestJobTracker.parent_job_ref)
        TestJobTracker.child_job_ref = child_tracker_doc["_id"]
        assert child_tracker_doc["job_name"] == "assets"
        assert child_tracker_doc["parent_job_ref"] == TestJobTracker.parent_job_ref

    def test_parent_update_timestamp(self):
        timestamp_now = jt.update_timestamp(TestJobTracker.parent_job_ref)
        parent_tracker_mod_date = jt.get_timestamp(TestJobTracker.parent_job_ref)
        delta = timedelta(seconds=SECOND_THRESHOLD)
        assert (timestamp_now - parent_tracker_mod_date) < delta

    def test_child_update_timestamp(self):
        timestamp_now = jt.update_timestamp(TestJobTracker.child_job_ref)
        parent_tracker_mod_date = jt.get_timestamp(TestJobTracker.parent_job_ref)
        child_tracker_mod_date = jt.get_timestamp(TestJobTracker.child_job_ref)
        delta = timedelta(seconds=SECOND_THRESHOLD)
        assert (timestamp_now - parent_tracker_mod_date) < delta
        assert (timestamp_now - child_tracker_mod_date) < delta

    def test_update_context_data(self):
        jt.update_context_data(TestJobTracker.child_job_ref, "assetLocation", "Updated Location")
        child_tracker_doc = jt.get_tracker_document(TestJobTracker.child_job_ref)
        assert child_tracker_doc["context"]["assetLocation"] == "Updated Location"

    def test_add_error(self):
        jt.append_error(TestJobTracker.child_job_ref, "AN ERROR MESSAGE", None, False)
        child_tracker_doc = jt.get_tracker_document(TestJobTracker.child_job_ref)
        assert "AN ERROR MESSAGE" in child_tracker_doc["context"]["errors_encountered"]
        assert child_tracker_doc['job_management']["job_status"] != "failed"
        jt.append_error(TestJobTracker.child_job_ref, "A SECOND ERROR MESSAGE", None, True)
        child_tracker_doc = jt.get_tracker_document(TestJobTracker.child_job_ref)
        assert "A SECOND ERROR MESSAGE" in child_tracker_doc["context"]["errors_encountered"]
        assert child_tracker_doc['job_management']["job_status"] == "failed"

    def test_get_document_with_different_formated_ticket_id(self):
        """"Ticket Id can be a string or ObjectId"""
        #ObjectId
        assert isinstance(TestJobTracker.parent_job_ref, ObjectId)
        tracker_doc = jt.get_tracker_document(TestJobTracker.parent_job_ref)
        assert tracker_doc is not None
        #String
        string_tracker_doc = jt.get_tracker_document(str(TestJobTracker.parent_job_ref))
        assert string_tracker_doc is not None

    def test_get_jobs(self):
        '''Assert that we can get all jobs or all jobs of a specific status (in this case failed)'''
        all_jobs = list(jt.get_jobs())
        assert len(all_jobs)
        assert isinstance(all_jobs[0]['_id'], ObjectId) # proxy for "is a job"
        failed_jobs = list(jt.get_jobs('failed'))
        assert len(failed_jobs)
        assert isinstance(failed_jobs[0]['_id'], ObjectId) # proxy for "is a job"
        assert all(job['job_management']['job_status'] == 'failed' for job in failed_jobs)

    def test_get_child_jobs(self):
        child_jobs = list(jt.get_child_jobs(TestJobTracker.parent_job_ref))
        assert len(child_jobs)
        assert all(job["parent_job_ref"] == TestJobTracker.parent_job_ref for job in child_jobs)

    def test_count_child_jobs(self):
        child_job_count = jt.count_child_jobs(TestJobTracker.parent_job_ref)
        assert child_job_count

    def get_job_directory(self):
        '''Assert that we can get a job directory, it will be created if not present'''
        doc = jt.get_tracker_document(TestJobTracker.parent_job_ref)
        dir = jt.get_job_directory(doc['_id'])
        assert os.path.exist(dir)
        dir_again = jt.get_job_directory(doc['_id'])

    ######################### Failure Testing ##################################

    def test_get_non_existent_tracker_document(self):
        non_existent_id = '5f1819229fdf8a0c7c2d8c36'
        tracker_doc = jt.get_tracker_document(non_existent_id)
        assert tracker_doc is None

    def test_get_tracker_document_with_none_job_ticket(self):
        with pytest.raises(Exception):
            tracker_doc = jt.get_tracker_document(None)

    def test_init_asset_tracker_child_document_with_non_existent_parent(self):
        with pytest.raises(Exception):
            non_existent_id = '5f1819229fdf8a0c7c2d8c36'
            child_tracker_doc = jt.init_tracker_document("assets", context, non_existent_id)


context = {
  "action": "create",
  "sourceSystemId": "4827718",
  "storageSrcKey": "sampleimage1.jp2",
  "storageDestKey": "sampleimage1.jp2",
  "storageSrcPath": "iiif-mps-dev",
  "thumbSizes": [
    150,
    300
  ],
  "identifier": "drs:400000203",
  "space": "testspace",
  "createdByAgent": "testagent",
  "createDate": "2021-02-11 17:56:09",
  "lastModifiedByAgent": "testagent",
  "lastModifiedDate": "2021-02-11 17:56:09",
  "status": "ACTIVE",
  "storageTier": "s3",
  "iiifApiVersion": "2",
  "assetLocation": "DRS",
  "mediaType": "image",
  "policyDefinition": {
    "policy": {
      "authenticated": {
        "height": 2400,
        "width": 2400
      },
      "public": {
        "height": 1200,
        "width": 1200
      }
    },
    "thumbnail": {
      "authenticated": {
        "height": 250,
        "width": 250
      },
      "public": {
        "height": 250,
        "width": 250
      }
    }
  },
  "assetMetadata": [
    {
      "fieldName": "admin",
      "jsonValue": {
        "name": "Hello there!",
        "description": "A test description",
        "type": "Standard",
        "pages": "120",
        "rating": "10",
        "shelf": "1A",
        "case": "Cabinet 1"
      }
    }
  ]
}

manifest = {
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "@id": "http://nrs-dev.lts.harvard.edu/URN-3:IIIF_DEMO:TEST_SINGLE_PUBLIC_IMAGE",
    "@type": "sc:Manifest",
    "attribution": "Provided by Harvard University",
    "label": "Harvard University, Single image public manifest, HUIT LTS",
    "license": "https://nrs.harvard.edu/urn-3:HUL.eother:idscopyright",
    "logo": "https://iiif.lib.harvard.edu/static/manifests/harvard_logo.jpg",
    "sequences": [
        {
            "@id": "http://nrs-dev.lts.harvard.edu/URN-3:IIIF_DEMO:TEST_SINGLE_PUBLIC_IMAGE/sequence/normal.json",
            "@type": "sc:Sequence",
            "canvases": [
                {
                    "@id": "http://nrs-dev.lts.harvard.edu/URN-3:IIIF_DEMO:TEST_SINGLE_PUBLIC_IMAGE/canvas/canvas-4827718.json",
                    "@type": "sc:Canvas",
                    "height": 1200,
                    "images": [
                        {
                            "@id": "http://nrs-dev.lts.harvard.edu/URN-3:IIIF_DEMO:TEST_SINGLE_PUBLIC_IMAGE/annotation/anno-4827718.json",
                            "@type": "oa:Annotation",
                            "motivation": "sc:painting",
                            "on": "http://nrs-dev.lts.harvard.edu/URN-3:IIIF_DEMO:TEST_SINGLE_PUBLIC_IMAGE/canvas/canvas-4827718.json",
                            "resource": {
                                "@id": "https://mps-dev.lib.harvard.edu/assets/images/iiif/2/URN-3:IIIF_DEMO:10001/full/1200,/0/default.jpg",
                                "@type": "dctypes:Image",
                                "format": "image/jpeg",
                                "height": 1200,
                                "service": {
                                    "@context": "http://iiif.io/api/image/2/context.json",
                                    "@id": "https://mps-dev.lib.harvard.edu/assets/images/iiif/2/URN-3:IIIF_DEMO:10001",
                                    "profile": "http://iiif.io/api/image/2/level2.json"
                                },
                                "width": 1200
                            }
                        }
                    ],
                    "label": "Harvard University, Single image public manifest, HUIT LTS",
                    "thumbnail": {
                        "@id": "https://ids.lib.harvard.edu/ids/iiif/4827718/full/,150/0/default.jpg",
                        "@type": "dctypes:Image"
                    },
                    "width": 1200
                }
            ],
            "label": "Harvard University, Single image public manifest, HUIT LTS",
            "startCanvas": "http://nrs-dev.lts.harvard.edu/URN-3:IIIF_DEMO:TEST_SINGLE_PUBLIC_IMAGE/canvas/canvas-4827718.json",
            "viewingHint": "individuals"
        }
    ]
}
