import os
import yaml
    
def find_first_parent_dir_contains_path(first_dir, path):
    '''
    return the first parent directory starting from the given first_dir
    that contains the given path
    '''
    current_path = first_dir
    tested_path = None
    while current_path != tested_path:
        if os.path.exists(os.path.join(current_path, path)):
            # found aic dir
            return os.path.join(current_path, path)
        tested_path = current_path
        current_path = os.path.abspath(os.path.join(current_path, os.pardir))
    return None

class Issue(object):
    def __init__(self, id, title, labels = []):
        self.id = id
        self.title = title

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class Aic(object):
    AIC_DIR_NAME = ".aic"
    ISSUES_FILE = "issues.yml"
    def __init__(self, path, create_db=False):
        if create_db:
            # check if current directory already contains aic
            if os.path.exists(os.path.join(path, self.AIC_DIR_NAME)):
                raise Exception("aic already exists")
            else:
                self.aic_dir_path = os.path.join(path, self.AIC_DIR_NAME)
                os.mkdir(self.aic_dir_path)
        else:
            aic_dir = self.find_first_parent_dir_contains_path(path, self.AIC_DIR_NAME)
            if not aic_dir:
                raise Exception("not a aic repo")
            else:
                self.aic_dir_path = aic_dir


    def issues(self):
        return YamlWrapper(os.path.join(self.aic_dir_path, self.ISSUES_FILE))


class YamlWrapper(object):
    def __init__(self, path):
        self.path = path
        self.all_objects = []
        if not os.path.exists(path):
            self.write_all()
        self.read_all()


    def get(self, id):
        for i in self.all_objects:
            if i.id == id:
                return i


    def read_all(self):
        with open(self.path, "r") as f:
            self.all_objects = yaml.load(f, Loader=yaml.FullLoader)
    

    def write_all(self):
        with open(self.path, "w") as f:
            return yaml.dump(self.all_objects, f)


    def add(self, obj):
        self.all_objects.append(obj)
        self.write_all()
