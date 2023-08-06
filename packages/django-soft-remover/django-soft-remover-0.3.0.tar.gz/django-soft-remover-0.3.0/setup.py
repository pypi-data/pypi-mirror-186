#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-soft-remover',
    version='0.3.0',
    description='Abstract Django models for soft removal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sergei Pikhovkin',
    author_email='s@pikhovkin.ru',
    url='https://github.com/pikhovkin/django-soft-remover',
    packages=[
        'soft_remover',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=3.0,<4.2'
    ],
    python_requires='>=3.8.*, <4.0.*',
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords=[
        'django',
        'restore',
        'soft-delete',
        'restore-data',
        'soft-deleting',
        'soft-remove',
    ],
)
