class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users[user] = True

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child.add_user('child')
parent.add_user('parent')


def is_user_in_group(user, group):
    if user in group.users:
        return True

    for g in group.groups:
        if is_user_in_group(user, g):
            return True
    return False
