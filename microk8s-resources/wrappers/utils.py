import os
import sys
from pathlib import Path

import click


def snap_data() -> Path:
    try:
        return Path(os.environ['SNAP_DATA'])
    except KeyError:
        return Path('/var/snap/microk8s/current')


def check_clustering():
    if (snap_data() / 'var/lock/clustered.lock').exists():
        click.echo('This MicroK8s deployment is acting as a node in a cluster.')
        click.echo('Please use `microk8s enable` on the master.')
        sys.exit(1)
