from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='GitDeets',
  version='0.0.2',
  description='A github data scrapper package',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Nikhil Raj',
  author_email='nikhil25803@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='scrapper', 
  packages=find_packages(),
  install_requires=['bs4','requests'] 
)
