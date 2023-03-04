from sys import argv
from setuptools import setup, find_packages


classifiers = [
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='C-',
  version='1.8.3',
  description='The official C- programming language.',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/Rayan25062011/C-", 
  project_urls={
   "Documentation": "https://github.com/Rayan25062011/cmp#get-started",
   "Issue tracker": "https://github.com/Rayan25062011/C-/issues",
   },
  author='Rayan Haddad',
  author_email='rayan.m.haddad@icloud.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='cm, c-, cminus', 
  packages=find_packages(),
  install_requires= ['shutil', 'os', 'sys', 'subprocess', 'error'],
  python_requires='>=3.6'
)
