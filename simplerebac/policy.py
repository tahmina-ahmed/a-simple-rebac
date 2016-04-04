
import json
from pprint import pprint

class Policy(object):
        _policy_dict= {}
        def __init__(self):
            with open('policy.json') as data_file:
                self._policy_dict = json.load(data_file)

        def check_policy(self, action_type, source_user, target_user, paths):
           path_dict=self.compute_path_dict(paths)
           return self.evaluate_policy(action_type, source_user, target_user, path_dict)

        def compute_path_dict(paths):
            path_dict={}                
            for path in paths:
                    path_dict[len(path)].append(path)
            return path_dict
            
        def evaluate_policy(action_type, source_user, target_user, path_dict):
                evaluation_result = True
                for int(num) in self._policy_dict:
                        if num > 0:
                                if target_user in path_dict[num]:
                                        evaluation_result = evaluation_result and True
                                if target_user not in path_dict[num]:
                                        evaluation_result = evaluation_result and False
                        if num < 0:
                                if target_user in path_dict[abs(num)]:
                                        evaluation_result = evaluation_result and False
                                if target_user not in path_dict[abs(num)]:
                                        evaluation_result = evaluation_result and True
                return  evaluation_result                        
                                        
                
                    
