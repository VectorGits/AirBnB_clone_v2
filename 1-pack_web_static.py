#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder of the AirBnB Clone repo
"""

from fabric.api import local
from datetime import datetime

def do_pack():
	"""
	Generates a .tgz archive from the contents of the 
	web_static folder of the AirBnB Clone repo
	"""
	# Create a versions directory if it doesn't exist
	local("mkdir -p versions")

	# Create a tgz archive of the web_static directory
	timestr = datetime.now().strftime("%Y%m%d%H%M%S")
	archive_path = "versions/web_static_{}.tgz".format(timestr)
	result = local("tar -cvzf {} web_static".fromat(archive_path))

	# Return the path of the archive if it was created, otherwise None
	if result.failed:
		return None
	else:
		return archive_path