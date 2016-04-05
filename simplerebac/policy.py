import json
from pprint import pprint

class Policy(object):
        _policy_dict= {
                "add_relationship":[-1],
                "delete_relationship" :[1,-3],
                "access":[]
            }

        def __init__(self):
             print("Policy")
#            with open('policy.json') as data_file:
 #               self._policy_dict = json.load(data_file)

        def check_policy(self, action_type, source_user, target_user, paths):
            path_dict=self.compute_path_dict(paths)
            return self.evaluate_policy(action_type, source_user, target_user, path_dict)

        def compute_path_dict(self,paths):
            """ compute a dictionary using path length as key"""
            path_dict={}
            for path in paths:
                    if len(path)-1 in path_dict.keys():
                       path_dict[len(path)-1].append(path)
                    else:
                       path_dict[len(path)-1]= [path] 
            return path_dict

        def evaluate_policy(self, action_type, source_user, target_user, path_dict):
            """ evaluating policy using policy_dict and path_dict"""
            evaluation_result = True
            sub_policy_result = True
            for num in self._policy_dict[action_type]:
                    if num > 0:
                            if num > len(path_dict):
                                sub_policy_result= False
                            else:
                                  if num in path_dict.keys():
                                    sub_policy_result = True
                                  if num  not in path_dict.keys():
                                    sub_policy_result =  False
                    if num < 0:
                             if abs(num)> len(path_dict):
                                sub_policy_result = True
                             else:
                                 if abs(num) in path_dict.keys():
                                     sub_policy_result=  False
                                 if abs(num) not in path_dict.keys():
                                     sub_policy_result = True

                    evaluation_result = evaluation_result and sub_policy_result

            return  evaluation_result

