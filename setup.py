# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='pywebhdfs',
    version='0.1',
    description='Python wrapper for the Hadoop WebHDFS REST API',
    author='Steven D. Gonzales',
    author_email='stevendgonzales@gmail.com',
    tests_require=[
        "mock",
        "nose",
        "nosexcover",
        "testtools",
        "tox"
    ],
    install_requires=[
        "requests"
    ],
    test_suite='nose.collector',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)
