#!/usr/bin/env python3
import os
import site

from setuptools import find_packages, setup
import sys
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

_ = """
py -3.9 .\setup.py build bdist_wheel --plat-name win-amd64
twine upload dist/*

now uninstall all conflicting versions of the script:
py -3.9 -m pip uninstall electrumsv-sdk

and install the one you want:
py -3.9 -m pip install electrumsv-sdk
"""

SCRIPT_FILE_PATH = os.path.realpath(__file__)
SCRIPT_PATH = os.path.dirname(SCRIPT_FILE_PATH)


with open(os.path.join(SCRIPT_PATH, "electrumsv_sdk", "__init__.py"), "r") as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break


def _locate_requirements():
    return open(os.path.join(SCRIPT_PATH, "requirements", "requirements.txt"),
        "r").read()


setup(
    name='electrumsv-sdk',
    version=version,
    install_requires=_locate_requirements(),
    description='ElectrumSV SDK',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Roger Taylor',
    author_email="roger.taylor.email@gmail.com",
    maintainer='Roger Taylor',
    maintainer_email='roger.taylor.email@gmail.com',
    url='https://github.com/electrumsv/electrumsv-sdk',
    download_url='https://github.com/electrumsv/electrumsv-sdk/tarball/{}'.format(version),
    license='Open BSV',
    keywords=[
        'bitcoinsv',
        'bsv',
        'bitcoin sv',
        'cryptocurrency',
        'tools',
        'wallet',
    ],
    entry_points={
        'console_scripts': [
            'electrumsv-sdk=electrumsv_sdk.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    include_package_data=True,
    package_data={"":
        [
            "electrumsv_sdk/scripts/*",
            "electrumsv-server/*",
            "electrumsv_sdk/builtin_components/merchant_api/exe-config/*",
            "electrumsv_sdk/builtin_components/header_sv/exe-config/*",
            "electrumsv_sdk/builtin_components/dpp_proxy/exe-config/*"
        ],
    },
    packages=find_packages(),
)
