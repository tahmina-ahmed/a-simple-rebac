
class Policy(object):
        def check_policy(self, action_type, source_user, target_user):
            if action_type == 'addRelation':
                 return self.add_relationship_policy(source_user, target_user)
            elif action_type == 'deleteRelation':
                 return self.delete_relationship_policy(source_user, target_user)
            elif action_type == 'access':
                 return self.access_policy(source_user, target_user)

        def add_relationship_policy(self, source_user, target_user):
           """ check policy to add relationship between two users"""
           paths=self.find_all_paths(source_user,target_user)
           return True

        def delete_relationship_policy(self,source_user,target_user):
           """ check  policy to delete relationship between two users"""
           return True

        def access_policy(self,source_user,target_user):
           """check policy to access target user"""
           return True

