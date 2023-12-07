#!/usr/bin/python3
"""web static folder into a tgz file"""

from datetime import datetime
from fabric.api import *


env.user = "ubuntu"


def do_pack():
    """Compress web static folder into a tgz extension"""
    local("mkdir -p versions")
    date = datetime.now()
    now = date.strftime("%Y%m%d%H%M%S")
    tgz_file = "versions/web_static_{}.tgz".format(now)
    try:
        local("tar -cvzf {} web_static".format(tgz_file))
        return (tgz_file)
    except:
        return None
