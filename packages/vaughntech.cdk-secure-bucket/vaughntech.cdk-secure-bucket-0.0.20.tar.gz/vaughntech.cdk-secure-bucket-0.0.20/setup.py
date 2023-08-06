import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "vaughntech.cdk-secure-bucket",
    "version": "0.0.20",
    "description": "S3 Bucket with defaults set to configure KMS Encption, loggings, and lifecycle policy",
    "license": "Apache-2.0",
    "url": "https://github.com/vaughngit/secure-s3-bucket-cdk-construct.git",
    "long_description_content_type": "text/markdown",
    "author": "Alvin Vaughn<alvin.vaughn@outlook.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/vaughngit/secure-s3-bucket-cdk-construct.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "vaughntech_cdk_secure_bucket",
        "vaughntech_cdk_secure_bucket._jsii"
    ],
    "package_data": {
        "vaughntech_cdk_secure_bucket._jsii": [
            "vaughntech-secure-s3-bucket@0.0.20.jsii.tgz"
        ],
        "vaughntech_cdk_secure_bucket": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.56.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.73.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
