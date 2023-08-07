import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "vt.cdk-vpc-constuct",
    "version": "0.0.5",
    "description": "Deploys VPC with tags and small EC2 NATGateways to reduce and track cost of development environments",
    "license": "Apache-2.0",
    "url": "https://github.com/vaughngit/projen-awsvpc-constuct.git",
    "long_description_content_type": "text/markdown",
    "author": "VaughnTech<alvin.vaughn@outlook.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/vaughngit/projen-awsvpc-constuct.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "vt_cdk_vpc_construct",
        "vt_cdk_vpc_construct._jsii"
    ],
    "package_data": {
        "vt_cdk_vpc_construct._jsii": [
            "vt-vpc-construct@0.0.5.jsii.tgz"
        ],
        "vt_cdk_vpc_construct": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.60.0, <3.0.0",
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
