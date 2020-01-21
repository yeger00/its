import subprocess
import tempfile
import os

def test_aiccli_sanity():
    assert subprocess.run(["aiccli"]).returncode == 0

def test_aiccli_init_sanity():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["aiccli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir.name, ".aic"))
    tempdir.cleanup()

def test_aiccli_init_exists():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["aiccli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir.name, ".aic"))
    assert subprocess.run(["aiccli", "init"]).returncode == 1
    tempdir.cleanup()

def test_aiccli_init_parent_exists():
    tempdir = tempfile.TemporaryDirectory()
    tempdir_son = tempfile.TemporaryDirectory(dir=tempdir.name)
    print(tempdir.name)
    os.chdir(tempdir.name)
    assert subprocess.run(["aiccli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir.name, ".aic"))
    os.chdir(tempdir_son.name)
    assert subprocess.run(["aiccli", "init"]).returncode == 0
    assert os.path.exists(os.path.join(tempdir_son.name, ".aic"))
    tempdir_son.cleanup()
    tempdir.cleanup()
