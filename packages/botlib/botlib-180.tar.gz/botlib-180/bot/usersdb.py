# This file is placed in the Public Domain.


"users"


from bot.objects import Class, Object
from bot.objects import find, save, update


class NoUser(Exception):

    "no matching user found"

    def done(self):
        "flag ok"


class Users(Object):

    "users database interface"

    @staticmethod
    def allowed(origin, perm):
        "check if origin has permission"
        perm = perm.upper()
        user = Users.get_user(origin)
        val = False
        if user and perm in user.perms:
            val = True
        return val

    @staticmethod
    def delete(origin, perm):
        "delete permission from origin"
        res = False
        for user in Users.get_users(origin):
            try:
                user.perms.remove(perm)
                save(user)
                res = True
            except ValueError:
                pass
        return res

    @staticmethod
    def get_users(origin=""):
        "return user objects matching origin"
        selector = {"user": origin}
        return find("user", selector)

    @staticmethod
    def get_user(origin):
        "return matching user object"
        users = list(Users.get_users(origin))
        res = None
        if len(users) > 0:
            res = users[-1]
        return res

    @staticmethod
    def perm(origin, permission):
        "check for permission"
        user = Users.get_user(origin)
        if not user:
            raise NoUser(origin)
        if permission.upper() not in user.perms:
            user.perms.append(permission.upper())
            save(user)
        return user


class User(Object):

    "user data"

    def __init__(self, val=None):
        Object.__init__(self)
        self.user = ""
        self.perms = []
        if val:
            update(self, val)

    def addperm(self, perm):
        "add a permission"
        self.perms.append(perm)

    def setuser(self, origin):
        "set the user's origin"
        self.user = origin


Class.add(User)
