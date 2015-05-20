# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_fitz', [dirname(__file__)])
        except ImportError:
            import _fitz
            return _fitz
        if fp is not None:
            try:
                _mod = imp.load_module('_fitz', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fitz = swig_import_helper()
    del swig_import_helper
else:
    import _fitz
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def initContext():
    return _fitz.initContext()
initContext = _fitz.initContext

def dropContext():
    return _fitz.dropContext()
dropContext = _fitz.dropContext
class Document(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Document, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Document, name)
    __repr__ = _swig_repr

    def __init__(self, filename):
        this = _fitz.new_Document(filename)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_Document
    __del__ = lambda self: None

    def pageCount_get(self):
        return _fitz.Document_pageCount_get(self)

    def loadPage(self, number):
        return _fitz.Document_loadPage(self, number)
    __swig_getmethods__["pageCount"] = _fitz.Document_pageCount_get
    if _newclass:
        pageCount = _swig_property(_fitz.Document_pageCount_get)

Document_swigregister = _fitz.Document_swigregister
Document_swigregister(Document)
cvar = _fitz.cvar

class Page(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Page, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Page, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _fitz.delete_Page
    __del__ = lambda self: None

    def bound(self):
        return _fitz.Page_bound(self)
Page_swigregister = _fitz.Page_swigregister
Page_swigregister(Page)

class Rect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x0"] = _fitz.Rect_x0_set
    __swig_getmethods__["x0"] = _fitz.Rect_x0_get
    if _newclass:
        x0 = _swig_property(_fitz.Rect_x0_get, _fitz.Rect_x0_set)
    __swig_setmethods__["y0"] = _fitz.Rect_y0_set
    __swig_getmethods__["y0"] = _fitz.Rect_y0_get
    if _newclass:
        y0 = _swig_property(_fitz.Rect_y0_get, _fitz.Rect_y0_set)
    __swig_setmethods__["x1"] = _fitz.Rect_x1_set
    __swig_getmethods__["x1"] = _fitz.Rect_x1_get
    if _newclass:
        x1 = _swig_property(_fitz.Rect_x1_get, _fitz.Rect_x1_set)
    __swig_setmethods__["y1"] = _fitz.Rect_y1_set
    __swig_getmethods__["y1"] = _fitz.Rect_y1_get
    if _newclass:
        y1 = _swig_property(_fitz.Rect_y1_get, _fitz.Rect_y1_set)

    def __init__(self):
        this = _fitz.new_Rect()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_Rect
    __del__ = lambda self: None
Rect_swigregister = _fitz.Rect_swigregister
Rect_swigregister(Rect)

# This file is compatible with both classic and new-style classes.


