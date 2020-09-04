class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
test_group = Group("test_group")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_user("child")

print(is_user_in_group(sub_child_user, parent)) #should return True
print(is_user_in_group("child", parent)) #should return True
print(is_user_in_group(sub_child_user, test_group)) #should return False
