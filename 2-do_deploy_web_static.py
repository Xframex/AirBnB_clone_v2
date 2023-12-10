#!/usr/bin/python3
"""Compress web static folder into a tgz file"""

from datetime import datetime
from fabric.api import *
from os.path import exists


env.user = "ubuntu"
env.hosts = [
    '54.236.45.211',
    '18.214.88.83',
]


def do_pack():
    """Convert web static folder into a tgz file"""
    local("mkdir -p versions")
    date = datetime.now()
    now = date.strftime("%Y%m%d%H%M%S")
    file_tgz = "versions/web_static_{}.tgz".format(now)
    try:
        local("tar -cvzf {} web_static".format(file_tgz))
        return (file_tgz)
    except Keyword:
        return None


def do_deploy(archive_path):
    """distributes an tgz archive web servers (two servers)"""
    if exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            file_tgz = archive_path.split('/')[-1]
            file = file_tgz.split('.')[0]
            archive_folder = '/data/web_static/releases/{}/'.format(file)
            run('mkdir -p {}'.format(archive_folder))
            run('tar -xvzf /tmp/{} -C {}'.format(file_tgz, archive_folder))
            run('rm /tmp/{}'.format(file_tgz))
            run('mv {}web_static/* {}'.format(archive_folder, archive_folder))
            run('rm -rf {}web_static'.format(archive_folder))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(archive_folder))
            return True
        except Keyword:
            return False
    else:
        return False
