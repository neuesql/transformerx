#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Qunfei Wu",
    author_email='wu.qunfei@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A private hub for huggingface transformers hosting on your AWS/Azure/GCP Cloud",
    entry_points={
        'console_scripts': [
            'transformerz=transformerz.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='transformerz',
    name='transformerz',
    packages=find_packages(include=['transformerz', 'transformerz.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/wuqunfei/transformerz',
    version='0.1.0',
    zip_safe=False,
)
