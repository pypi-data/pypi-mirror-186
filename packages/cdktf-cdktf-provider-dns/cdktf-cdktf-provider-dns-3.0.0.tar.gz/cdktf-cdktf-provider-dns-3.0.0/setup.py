import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-dns",
    "version": "3.0.0",
    "description": "Prebuilt dns Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-dns.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-dns.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_dns",
        "cdktf_cdktf_provider_dns._jsii",
        "cdktf_cdktf_provider_dns.a_record_set",
        "cdktf_cdktf_provider_dns.aaaa_record_set",
        "cdktf_cdktf_provider_dns.cname_record",
        "cdktf_cdktf_provider_dns.data_dns_a_record_set",
        "cdktf_cdktf_provider_dns.data_dns_aaaa_record_set",
        "cdktf_cdktf_provider_dns.data_dns_cname_record_set",
        "cdktf_cdktf_provider_dns.data_dns_mx_record_set",
        "cdktf_cdktf_provider_dns.data_dns_ns_record_set",
        "cdktf_cdktf_provider_dns.data_dns_ptr_record_set",
        "cdktf_cdktf_provider_dns.data_dns_srv_record_set",
        "cdktf_cdktf_provider_dns.data_dns_txt_record_set",
        "cdktf_cdktf_provider_dns.mx_record_set",
        "cdktf_cdktf_provider_dns.ns_record_set",
        "cdktf_cdktf_provider_dns.provider",
        "cdktf_cdktf_provider_dns.ptr_record",
        "cdktf_cdktf_provider_dns.srv_record_set",
        "cdktf_cdktf_provider_dns.txt_record_set"
    ],
    "package_data": {
        "cdktf_cdktf_provider_dns._jsii": [
            "provider-dns@3.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_dns": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "cdktf>=0.15.0, <0.16.0",
        "constructs>=10.0.0, <11.0.0",
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
