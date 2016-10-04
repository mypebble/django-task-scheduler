from setuptools import setup, find_packages


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]


setup(
    name='django-task-scheduler',
    version='0.0.1',
    description="A simple task scheduling system for Django",
    author="SF Software limited t/a Pebble",
    author_email="sysadmin@mypebble.co.uk",
    url="https://github.com/mypebble/django-task-scheduler",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['six', 'django'],
    classifiers=CLASSIFIERS,
)
