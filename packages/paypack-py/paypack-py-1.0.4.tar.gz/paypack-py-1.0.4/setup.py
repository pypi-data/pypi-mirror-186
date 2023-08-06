import os
from setuptools import setup, find_packages
# from distutils.core import setup

# with open('LICENSE.txt') as file:
#     license_text = file.read()

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
	# Name of the package 
	name='paypack-py',
	# Packages to include into the distribution 
	packages=['paypack'],
	# Start with a small number and increase it with 
	py_modules=["client","events","merchant","transactions","oauth2"],
	# every change you make https://semver.org 
	version='1.0.4',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license='MIT',
	# Short description of your library 
	description='Python and Django SDK for Paypack API Payment Gateway',
	# Long description of your library 
	long_description=long_description,
	long_description_content_type='text/markdown',
	# url='https://github.com/quarksgroup/paypack-py',
	# Link from which the project can be downloaded 
	download_url='',
	# List of keywords 
	keywords=["paypack", "paypack-py-rwanda", "payment-py", "payments", "paypack-py", "paypack-py-sdk", "paypack-py-sdk-django", "paypack-py-sdk-flask", "paypack-py-sdk-pyramid", "paypack-py-sdk-tornado", "paypack-py-sdk-web", "paypack-py-sdk-web-django", "paypack-py-sdk-web-flask", "paypack-py-sdk-web-pyramid", "paypack-py-sdk-web-tornado"],
	# List of packages to install with this one 
	install_requires=['requests ~= 2.26.0'],
	# https://pypi.org/classifiers/ 
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
	include_package_data=True,
)
