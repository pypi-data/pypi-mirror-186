import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name="satsure_cloud_utils",
    version="0.0.24",
    author="Rehan",
    author_email="rehan@satsure.co",
    description="A package to navigate SatSure Cloud infrastructure",
    long_description=README,
    Homepage="https://pypi.org/project/satsure-cloud-utils/",
    project_urls={
        'Documentation': "https://docs-satsure-cloud-utils.netlify.app/"
        },
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    packages=['satsure_cloud_utils'],
    install_requires=['awscli','python-dotenv']
)