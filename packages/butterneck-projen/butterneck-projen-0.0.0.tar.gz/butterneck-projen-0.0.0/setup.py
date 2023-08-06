import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "butterneck-projen",
    "version": "0.0.0",
    "description": "butterneck-projen",
    "license": "Apache-2.0",
    "url": "https://github.com/butterneck/butterneck-projen.git",
    "long_description_content_type": "text/markdown",
    "author": "Filippo Pinton<pinton.filippo@protonmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/butterneck/butterneck-projen.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "butterneck_projen",
        "butterneck_projen._jsii"
    ],
    "package_data": {
        "butterneck_projen._jsii": [
            "butterneck-projen@0.0.0.jsii.tgz"
        ],
        "butterneck_projen": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "jsii>=1.73.0, <2.0.0",
        "projen>=0.66.15, <0.67.0",
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
