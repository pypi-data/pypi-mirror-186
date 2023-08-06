import subprocess
import sys
from typing import Dict
from typing import Tuple

try:
    import pip
    from pip._internal.operations.freeze import freeze as freeze_

    HAS_PIP = True
except ImportError:
    HAS_PIP = False


def freeze(hub) -> Dict[str, str]:
    """
    Return the output of pip freeze
    """
    if HAS_PIP:
        # Get the freeze information from pip internals
        pip_freeze = [line for line in freeze_()]
    else:
        # Shell out to pip
        ret = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
        pip_freeze = ret.decode("utf-8").strip().split("\n")

    result = {}
    for line in pip_freeze:
        version_ = ""
        package = ""
        editable = "-e " in line

        if "#egg=" in line:
            v, package = line.split("#egg=")
        elif "==" in line:
            package, v = line.split("==")

        result[package] = {"version": version_, "editable": editable}
    return result


def version(hub) -> Tuple[int, int, int]:
    """
    Return the version of pip
    """
    major = minor = point = 0
    try:
        split = pip.__version__.split(".", maxsplit=2)
        major = int(split[0])
        minor = int(split[1])
        point = int(split[2])
    except:
        ...

    return major, minor, point
