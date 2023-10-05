#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path
from fabric.decorators import task

# env.user = 'ubuntu'
env.hosts = ["18.235.248.71", "54.146.78.208"]
# env.key_filename = "~/id_rsa"


@task
def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers"""
    try:
        with_ext = archive_path.split("/")[-1]
        without_ext = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/" + without_ext)
        run(
            "tar -xzf /tmp/"
            + with_ext + " -C /data/web_static/releases/"
            + without_ext
        )
        run("rm /tmp/" + with_ext)
        run(
            "mv /data/web_static/releases/"
            + without_ext
            + "/web_static/* /data/web_static/releases/"
            + without_ext
        )
        run("rm -rf /data/web_static/releases/"
            + without_ext + "/web_static")
        run("rm -rf /data/web_static/current")
        run(
            "ln -s /data/web_static/releases/"
            + without_ext
            + "/ /data/web_static/current"
        )
        return True
    except Exception:
        return False


@task
def do_pack():
    """generates a .tgz archive from web_static"""
    local(
        "mkdir versions ; tar -cvzf \
versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static/"
    )
