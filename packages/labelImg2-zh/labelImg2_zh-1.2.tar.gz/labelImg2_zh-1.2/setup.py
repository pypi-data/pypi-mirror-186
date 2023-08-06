#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages




requirements = [
    'lxml'
]

required_packages = find_packages()
required_packages.append('labelImg')

APP = ['labelImg.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icons/app.icns'
}

setup(
    app=APP,
    name='labelImg2_zh',
    version='1.2',
    description="LabelImg2 is a graphical image annotation tool and label object bounding boxes in images",
    author="TzuTa Lin",
    author_email='tzu.ta.lin@gmail.com',
    url='https://github.com/chinakook/labelImg2',
    package_dir={'labelImg': '.'},
    packages=required_packages,
    entry_points={
        'console_scripts': [
            'labelImg2=labelimg2_zh.labelImg:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='labelImg labelTool development annotation deeplearning',
    package_data={'data/predefined_classes.txt': ['data/predefined_classes.txt']},
)
