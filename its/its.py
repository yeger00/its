import os
import tinydb 

def to_type(o, new_type):
    '''
    Helper funciton that receives an object or a dict and convert it to a new given type.

    :param object|dict o: The object to convert
    :param Type new_type: The type to convert to.
    '''
    if new_type == type(o):
        return o
    else:
        return new_type(**o)
    
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

class Issue(object):
    def __init__(self, title, id = None, labels = []):
        self.id = id
        self.title = title

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class Its(object):
    ITS_DIR_NAME = ".its"
    ISSUES_FILE = "issues.json"
    def __init__(self, path, create_db=False):
        if create_db:
            # check if current directory already contains its
            if os.path.exists(os.path.join(path, self.ITS_DIR_NAME)):
                raise Exception("its already exists")
            else:
                self.its_dir_path = os.path.join(path, self.ITS_DIR_NAME)
                os.mkdir(self.its_dir_path)
        else:
            its_dir = find_first_parent_dir_contains_path(path, self.ITS_DIR_NAME)
            if not its_dir:
                raise Exception("not a its repo")
            else:
                self.its_dir_path = its_dir


    def issues(self):
        db_path = os.path.join(self.its_dir_path, self.ISSUES_FILE)
        db = tinydb.TinyDB(db_path, sort_keys=True, indent=4, separators=(',', ': '))
        return Issues(db)

class Issues(object):
    def __init__(self, db):
        self.db = db

    def add(self, issue):
        issue.id = len(self.db)
        self.db.insert(issue.__dict__)

    def all(self):
        return [to_type(issue, Issue) for issue in self.db.all()]

    def get(self, id):
        issue = self.db.get(tinydb.Query().id == id)
        if issue:
            return to_type(issue, Issue)
        return None

