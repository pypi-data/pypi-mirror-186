"""
Flask-Pyadmin
-------------
 
an admin tool
"""
from setuptools import setup
 
setup(
    name='Uiadmin-Flask',
    version='1.0.0',
    url='http://uiadmin.net',
    license='Apache2',
    author='jry',
    author_email='ijry@qq.com',
    description='uiadmin的python实现',
    long_description=__doc__,
    packages=['uiadmin_flask'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
