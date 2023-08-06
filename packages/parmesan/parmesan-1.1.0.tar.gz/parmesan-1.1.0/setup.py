#!/usr/bin/env python3
# system modules
import os
import itertools
import re
import subprocess
from setuptools import setup

# internal modules

# external modules


def get_version():
    try:
        git_version = subprocess.check_output(
            [
                "git",
                "describe",
                "--tags",
                "--match",
                "v*",
                "--always",
                "--dirty",
            ],
            stderr=subprocess.DEVNULL,
            cwd=os.path.dirname(os.path.abspath(__file__)),
        )
        d = re.fullmatch(
            pattern=r"[a-z]*(?P<tagversion>\d+(:?\.\d+)*)"
            r"(?:[^.\d]+(?P<revcount>\d+)[^.\da-z]+?(?P<commit>[a-z0-9]+))?"
            r"(?:[^.\d]+?(?P<dirty>dirty))?",
            string=git_version.decode(errors="ignore").strip(),
            flags=re.IGNORECASE,
        ).groupdict()
        return "+".join(
            filter(
                bool,
                itertools.chain(
                    (d.get("tagversion", "0"),),
                    (
                        ".".join(
                            filter(
                                bool,
                                (
                                    d[k]
                                    for k in (
                                        "revcount",
                                        "commit",
                                        "dirty",
                                    )
                                ),
                            )
                        ),
                    ),
                ),
            )
        )
    except (
        subprocess.CalledProcessError,
        OSError,
        ModuleNotFoundError,
        AttributeError,
        TypeError,
        StopIteration,
    ) as e:
        print(e)
        return None


dynamic_version = get_version()
if dynamic_version:
    version_path = os.path.join(
        os.path.dirname(__file__), "parmesan", "version.py"
    )
    with open(version_path, "w") as fh:
        fh.write('__version__ = "{}"\n'.format(dynamic_version))


setup()
