#!/usr/bin/env python

from distutils.core import setup
import sys

if sys.version_info < (2, 7):
	print("rawdog requires Python 2.7 or later.")
	sys.exit(1)

setup(name="rawdog",
	version="3.0rc1",
	description="RSS Aggregator Without Delusions Of Grandeur",
	author="Adam Sampson",
	author_email="ats@offog.org",
	url="http://offog.org/code/rawdog/",
	scripts=['rawdog'],
	data_files=[('share/man/man1', ['rawdog.1'])],
	packages=['rawdoglib'],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Environment :: Console",
		"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
		"Operating System :: POSIX",
		"Programming Language :: Python :: 3",
		"Topic :: Internet :: WWW/HTTP",
	])
