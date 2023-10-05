#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("archive_path", help="Path to the archive file")
parser.add_argument("-u", "--ssh-user", required=True, help="SSH username")
args = parser.parse_args()

env.user = args.ssh_user  # Use the SSH username provided as an argument

# Check if an SSH key file was provided as an argument
if "keyfile" in env:
    env.key_filename = env.keyfile
else:
    env.key_filename = "~/.ssh/school"

env.hosts = ["18.235.248.71", "54.146.78.208"]


def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split("/")
        base = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}".format(base)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except:
        return False
