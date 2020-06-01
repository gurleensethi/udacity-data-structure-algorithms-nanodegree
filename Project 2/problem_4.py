# I have modified the Group class to hold user is a dictionary (Map), insted
# of an array. This allows us to check for existance of a user in a particular
# group in O(1).
#
# is_user_in_group is a recursive function that will find the existance of a
# user in a group or in all of its sub-groups.
# Time time complexity of this opeartion is O(N) where N is the total number
# of sub-groups + 1 (the group itself) inside a given group.

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users[user] = user

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if not group or not user:
        return False

    if user in group.users:
        return True

    for g in group.groups:
        if is_user_in_group(user, g):
            return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child.add_user('child')
parent.add_user('parent')

print(is_user_in_group('parent', parent))  # returns True
print(is_user_in_group('parent', sub_child))  # returns False
print(is_user_in_group('parent', None))  # returns False
