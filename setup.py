# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""IIIF API for Invenio."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'urllib3>=1.21.1,<1.25',
    'invenio-db>=1.0.0',
    'isort>=4.3.4',
    'pydocstyle>=1.0.0',
    'pytest-invenio>=1.1.1',
    'pytest-pep8>=1.0.6',
    'pytest>=4.0.0,<5.0.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.8.0',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    'Flask>=0.11.1',
    'Flask-CeleryExt>=0.3.1',
    'Flask-IIIF>=0.5.1',
    'invenio-access>=1.0.0',
    'invenio-files-rest>=1.0.0a23',
    'invenio-records-files>=1.0.0a9',
    'six>=1.11.0',
    'Wand>=0.4.4',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_iiif', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-iiif',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio IIIF',
    license='MIT',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-iiif',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.apps': [
            'invenio_iiif = invenio_iiif:InvenioIIIF',
        ],
        'invenio_base.api_apps': [
            'invenio_iiif = invenio_iiif:InvenioIIIFAPI',
        ],
        'invenio_base.blueprints': [
            'invenio_iiif = invenio_iiif.previewer:blueprint',
        ],
        'invenio_celery.tasks': [
            'invenio_iiif = invenio_iiif.tasks',
        ],
        'invenio_previewer.previewers': [
            'iiif_image = invenio_iiif.previewer',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 5 - Production/Stable',
    ],
)
