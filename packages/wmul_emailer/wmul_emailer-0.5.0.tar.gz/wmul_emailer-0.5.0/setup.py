"""
@Author = 'Mike Stanley'

============ Change Log ============
2022-May-06 = Changed License from MIT to GPLv2.

2018-May-18 = Created.

============ License ============
Copyright (c) 2018-2023 Michael Stanley

This file is part of wmul_emailer.

wmul_emailer is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version.

wmul_emailer is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR 
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
wmul_emailer. If not, see <https://www.gnu.org/licenses/>. 
"""

from setuptools import setup, find_packages

setup(
    name='wmul_emailer',
    version='0.5.0',
    license='GPLv3',
    description='E-Mailer Interface for WMUL-FM',

    author='Michael Stanley',
    author_email='stanley50@marshall.edu',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click'],

    tests_require=["pytest", "pytest-mock", "wmul_test_utils"],

    entry_points='''
    [console_scripts]
    send_test_email=wmul_emailer.cli:send_test_email
'''
)
