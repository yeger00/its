import subprocess
import tempfile
import os


def test_itscli_issue_sanity():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["itscli", "init"]).returncode == 0
    assert subprocess.run(["itscli", "issue"]).returncode == 0
    tempdir.cleanup()


def test_itscli_issue_not_init():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["itscli", "issue"]).returncode == 1
    tempdir.cleanup()


def test_itscli_issue_empty_list():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["itscli", "init"]).returncode == 0
    run = subprocess.run(["itscli", "issue", "list"], stdout=subprocess.PIPE)
    assert run.returncode == 0
    assert run.stdout == b'no issues\n'
    tempdir.cleanup()

def test_itscli_issue_new_issue():
    tempdir = tempfile.TemporaryDirectory()
    os.chdir(tempdir.name)
    assert subprocess.run(["itscli", "init"]).returncode == 0
    assert subprocess.run(["itscli", "issue", "new", "title"]).returncode == 0
    assert subprocess.run(["itscli", "issue", "new", "title"]).returncode == 0
    run = subprocess.run(["itscli", "issue", "list"], stdout=subprocess.PIPE)
    assert run.returncode == 0
    assert run.stdout == b'id: 0\ntitle: title\nstatus: new\nid: 1\ntitle: title\nstatus: new\n'
    tempdir.cleanup()
