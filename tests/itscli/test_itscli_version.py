import subprocess
import tempfile
import os

import its

def test_itscli_version_sanity():
    run = subprocess.run(["itscli", "--version"], stdout=subprocess.PIPE)
    assert run.returncode == 0
    assert run.stdout.decode("utf-8")  == its.version + "\n"
