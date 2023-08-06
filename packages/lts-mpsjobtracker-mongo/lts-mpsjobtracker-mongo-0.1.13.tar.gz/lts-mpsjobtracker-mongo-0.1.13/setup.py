import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lts-mpsjobtracker-mongo",
    version="0.1.13",
    author="Katie Amaral",
    author_email="kathryn_amaral@harvard.edu",
    description="A job tracker management module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.huit.harvard.edu/LTS/mps-jobtracker",
    packages=setuptools.find_packages(),
    install_requires=[
        'jsonschema',
        'pymongo',
        'pytest',
        'tenacity',
        'uuid'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True
)
