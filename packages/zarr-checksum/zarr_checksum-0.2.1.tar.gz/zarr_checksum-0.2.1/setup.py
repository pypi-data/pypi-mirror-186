# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zarr_checksum']

package_data = \
{'': ['*']}

install_requires = \
['boto3-stubs[s3]>=1.26.29,<2.0.0',
 'boto3>=1.26.29,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'zarr>=2.13.3,<3.0.0']

entry_points = \
{'console_scripts': ['zarrsum = zarr_checksum.cli:cli']}

setup_kwargs = {
    'name': 'zarr-checksum',
    'version': '0.2.1',
    'description': 'Checksum support for zarrs stored in various backends',
    'long_description': '# zarr_checksum\nAlgorithms for calculating a zarr checksum against local or cloud storage\n\n# Install\n```\npip install zarr-checksum\n```\n\n# Usage\n\n## CLI\nTo calculate the checksum for a local zarr archive\n```\nzarrsum local <directory>\n```\n\nTo calcuate the checksum for a remote (S3) zarr archive\n```\nzarrsum remote s3://your_bucket/prefix_to_zarr\n```\n\n## Python\nTo calculate the checksum for a local zarr archive\n```python\nfrom zarr_checksum import compute_zarr_checksum\nfrom zarr_checksum.generators import yield_files_local, yield_files_s3\n\n# Local\nchecksum = compute_zarr_checksum(yield_files_local("local_path"))\n\n# Remote\nchecksum = compute_zarr_checksum(\n    yield_files_s3(\n        bucket="your_bucket",\n        prefix="prefix_to_zarr",\n        # Credentials can also be passed via environment variables\n        credentials={\n            aws_access_key_id: "youraccesskey",\n            aws_secret_access_key: "yoursecretkey",\n            region_name: "us-east-1",\n        }\n    )\n)\n```\n\nAccess checksum information\n```python\n>>> checksum.digest\n\'c228464f432c4376f0de6ddaea32650c-37481--38757151179\'\n>>> checksum.md5\n\'c228464f432c4376f0de6ddaea32650c\'\n>>> checksum.count\n37481\n>>> checksum.size\n38757151179\n```\n',
    'author': 'Kitware, Inc.',
    'author_email': 'kitware@kitware.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dandi/zarr_checksum',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.10,<4.0.0',
}


setup(**setup_kwargs)
