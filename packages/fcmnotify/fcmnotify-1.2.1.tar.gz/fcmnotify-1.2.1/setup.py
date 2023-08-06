import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='fcmnotify',
    version='1.2.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django app to send notifications using Firebase! Adding Firebase Cloud Messaging Service into a Django Project The aim of this repository is to provide a step-by-step guide and a basic project sample to implement FCM (Firebase Cloud Messaging) feature into a django-based project.',
    long_description=README,
    url='https://github.com/dkkundu/fcmnotify',
    author='Dipto Kumar Kundu',
    author_email='dkkundu00@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
