
class Policy(object):
        _path_dict = {}
        _paths= []
        _policy_dict= {}
        def check_policy(self, action_type, source_user, target_user):
            if action_type == 'addRelation':
                 return self.add_relationship_policy(source_user, target_user)
            elif action_type == 'deleteRelation':
                 return self.delete_relationship_policy(source_user, target_user)
            elif action_type == 'access':
                 return self.access_policy(source_user, target_user)

        def add_relationship_policy(self, paths, source_user, target_user):
           """ check policy to add relationship between two users"""
           self._paths= paths
           return True

        def delete_relationship_policy(self, paths, source_user,target_user):
           """ check  policy to delete relationship between two users"""
           self._paths = paths 
           return True

        def access_policy(self, paths,source_user,target_user):
           """check policy to access target user"""
           self._paths = paths
           return True
           
        def compute_path_dict():
            for path in self._paths:
                    self._path_dict[len(path)].append(path)
                    
