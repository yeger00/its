'''
Its main script file
'''

import os
import tinydb

def to_type(obj, new_type):
    '''
    Helper funciton that receives an object or a dict and convert it to a new given type.

    :param object|dict o: The object to convert
    :param Type new_type: The type to convert to.
    '''
    if new_type == type(obj):
        return obj
    return new_type(**obj)

def find_first_parent_dir_contains_path(first_dir, path):
    '''
    return the first parent directory starting from the given first_dir
    that contains the given path
    '''
    current_path = first_dir
    tested_path = None
    while current_path != tested_path:
        if os.path.exists(os.path.join(current_path, path)):
            # found dir
            return os.path.join(current_path, path)
        tested_path = current_path
        current_path = os.path.abspath(os.path.join(current_path, os.pardir))
    return None

class Issue(object): # pylint: disable=too-few-public-methods
    '''
    Issue class
    '''
    def __init__(self, title, status="new", description="", issue_id=None, comments=None): #pylint: disable=too-many-arguments
        self.issue_id = issue_id
        self.status = status
        self.description = description
        self.title = title
        self.comments = []
        if comments:
            self.comments = comments

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def str_summary(self):
        '''
        return a summary of the issue
        '''
        return "id: {issue_id}\ntitle: {title}\nstatus: {status}".format(
            issue_id=self.issue_id, title=self.title, status=self.status)

    def str_full(self):
        '''
        return the full issue
        '''
        return "id: {issue_id}\ntitle: {title}\nstatus: {status}\n\n{description}".format(
            issue_id=self.issue_id, title=self.title,
            status=self.status, description=self.description)

    def __str__(self):
        return self.str_summary()

class Comment(object): # pylint: disable=too-few-public-methods
    '''
    Issue class
    '''
    def __init__(self, author, comment):
        self.author = author
        self.comment = comment

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        return "{author}: {comment}".format(author=self.author, comment=self.comment)

class Change(object): # pylint: disable=too-few-public-methods
    '''
    Issue class
    '''
    def __init__(self, what, old, new):
        self.what = what
        self.old = old
        self.new = new

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        return "{what}: {old} -> {new}".format(what=self.what, old=self.old, new=self.new)

class Its(object): # pylint: disable=too-few-public-methods
    '''
    Its class
    '''
    ITS_DIR_NAME = ".its"
    ISSUES_FILE = "issues.json"
    def __init__(self, path, create_db=False):
        if create_db:
            # check if current directory already contains its
            if os.path.exists(os.path.join(path, self.ITS_DIR_NAME)):
                raise Exception("its already exists")
            self.its_dir_path = os.path.join(path, self.ITS_DIR_NAME)
            os.mkdir(self.its_dir_path)
        else:
            its_dir = find_first_parent_dir_contains_path(path, self.ITS_DIR_NAME)
            if not its_dir:
                raise Exception("not a its repo")
            self.its_dir_path = its_dir


    def issues(self):
        '''
        returns the issues
        '''
        db_path = os.path.join(self.its_dir_path, self.ISSUES_FILE)
        return Issues(tinydb.TinyDB(db_path, sort_keys=True, indent=4, separators=(',', ': ')))

class Issues(object):
    '''
    Issues class
    '''
    def __init__(self, database):
        self.database = database

    def add(self, issue):
        '''
        Adds a new issue
        '''
        issue.issue_id = len(self.database)
        self.database.insert({"issue" : issue.__dict__, "issue_id" : issue.issue_id})

    def all(self):
        '''
        returns all the issues
        '''
        return [to_type(issue["issue"], Issue) for issue in self.database.all()]

    def get(self, issue_id):
        '''
        returns an issue by id
        '''
        issue = self.database.get(tinydb.Query().issue_id == issue_id)["issue"]
        if issue:
            return to_type(issue, Issue)
        return None

    def update(self, issue):
        '''
        updates the given issue
        '''
        issue = self.database.update({"issue": issue.__dict__},
                                     tinydb.Query().issue_id == issue.issue_id)
