import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "amazon-textract-idp-cdk-constructs",
    "version": "0.0.11",
    "description": "amazon-textract-idp-cdk-constructs",
    "license": "MIT-0",
    "url": "https://github.com/aws-samples/amazon-textract-idp-cdk-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Martin Schade<45048633+schadem@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws-samples/amazon-textract-idp-cdk-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "amazon_textract_idp_cdk_constructs",
        "amazon_textract_idp_cdk_constructs._jsii"
    ],
    "package_data": {
        "amazon_textract_idp_cdk_constructs._jsii": [
            "amazon-textract-idp-cdk-constructs@0.0.11.jsii.tgz"
        ],
        "amazon_textract_idp_cdk_constructs": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.1.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.70.0, <2.0.0",
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
