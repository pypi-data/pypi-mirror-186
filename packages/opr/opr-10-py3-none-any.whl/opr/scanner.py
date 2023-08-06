# This file is placed in the Public Domain
# pylint: disable=C0115,C0116


"scanner"


import os


from opr.objects import spl


def include(name, namelist):
    for nme in namelist:
        if nme in name:
            return True
    return False


def listmod(path):
    res = []
    if not os.path.exists(path):
        return res
    for fnm in os.listdir(path):
        if fnm.endswith("~") or fnm.startswith("__"):
            continue
        res.append(fnm.split(os.sep)[-1][:-3])
    return res


def scanpkg(pkg, func, mods=None):
    path = pkg.__path__[0]
    name = pkg.__name__
    return scandir(path, func, name, mods)


def scandir(path, func, pname=None, mods=None):
    res = []
    if pname is None:
        pname = path.split(os.sep)[-1]
    for modname in listmod(path):
        if not modname:
            continue
        if mods and not include(modname, spl(mods)):
            continue
        mname = "%s.%s" % (pname, modname)
        ppath = os.path.join(path, "%s.py" % modname)
        mod = func(mname, ppath)
        if mod:
            res.append(mod)
    return res
