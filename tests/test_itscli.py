import subprocess
import tempfile
import os

def test_itscli_sanity():
    assert subprocess.run(["itscli"]).returncode == 0

def test_itscli_init_sanity():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["itscli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir.name, ".its"))
    tempdir.cleanup()

def test_itscli_init_exists():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["itscli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir.name, ".its"))
    assert subprocess.run(["itscli", "init"]).returncode == 1
    tempdir.cleanup()

def test_itscli_init_parent_exists():
    tempdir = tempfile.TemporaryDirectory()
    tempdir_son = tempfile.TemporaryDirectory(dir=tempdir.name)
    os.chdir(tempdir.name)
    assert subprocess.run(["itscli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir.name, ".its"))
    os.chdir(tempdir_son.name)
    assert subprocess.run(["itscli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir_son.name, ".its"))
    tempdir_son.cleanup()
    tempdir.cleanup()
