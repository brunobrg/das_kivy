from model.user import User
from model.role import Administrator
from model.object import Directory
from model.assignment import Assignment

admin_user = User("admin", "12345")
admin_role = Administrator()
admin_assign = Assignment(admin_user, admin_role)
rootpath = "/home/gagos/unb/git/das/rbac_python/objects/organization"
rootdir = Directory(rootpath, None, admin_role)
