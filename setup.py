# See https://github.com/walero-moon/Worldtime-py
from setuptools import setup, find_packages
import pathlib

description = "A wrapper for WorldtimeAPI with search functionality."
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='worldtimepy',
    version='0.1.1',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/walero-moon/Worldtime-py',
    keywords='worldtimeAPI, worldtime-py, timezones, timezone-api, wrapper',
    package_dir={'':'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['countryinfo', 'requests', 'unidecode'],
    project_urls={
        'My GitHub': 'https://github.com/walero-moon',
        'Source': 'https://github.com/walero-moon/Worldtime-py'
        },
    license='GPL-3.0',
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    ]
)