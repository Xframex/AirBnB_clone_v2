#!/usr/bin/python3

import os.path
from fabric.api import env, put, run

env.hosts = ["54.236.45.211", "18.214.88.83"]

def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        print(f"Error: Archive file not found at {archive_path}")
        return False

    archive_filename = os.path.basename(archive_path)
    name = os.path.splitext(archive_filename)[0]

    try:
        put(archive_path, f"/tmp/{archive_filename}")
        run(f"rm -rf /data/web_static/releases/{name}/")
        run(f"mkdir -p /data/web_static/releases/{name}/")
        run(f"tar -xzf /tmp/{archive_filename} -C /data/web_static/releases/{name}/")
        run(f"rm /tmp/{archive_filename}")
        run(f"mv /data/web_static/releases/{name}/web_static/* /data/web_static/releases/{name}/")
        run(f"rm -rf /data/web_static/releases/{name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
