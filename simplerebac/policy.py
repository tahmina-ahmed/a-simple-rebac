
import json
from pprint import pprint

class Policy(object):
        _path_dict = {}
        _paths= []
        _policy_dict= {}
        _source_user
        _target_user
        def __init__(self):
            with open('policy.json') as data_file:
            self._policy_dict = json.load(data_file)

        def check_policy(self, action_type, source_user, target_user):
           self._paths = paths
           self.compute_path_dict()
           return self.evaluate_policy(action_type)

        def compute_path_dict():
            for path in self._paths:
                    self._path_dict[len(path)].append(path)
                    
        def evaluate_policy(action-type):
                
                    
