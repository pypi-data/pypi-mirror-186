import sys

from setuptools import setup, find_packages

if sys.version_info[0] != 3:
    print('This script requires Python >= 3')
    exit(1)

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

requirements = ['httpx[socks]>=0.23.3', 'aiofiles>=22.0.1']

setup(
    name='tra-yan',
    version='0.1.0',
    author='re1von project',
    author_email='re1von_project@bk.ru',
    url='https://github.com/re1von/tra-yan',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
