"""
Implements some utility stuff
for authorization and dynamic importing stuff

I wish I didn't have to do this importing myself
"""
from django.utils.importlib import import_module

from models import Device

def authorize(key):
    """
    Checks if the key is registered with a device
    """
    try:
        return Device.objects.get(key=key)
    except Device.DoesNotExist:
        return None

def get_callable(lookup_string):
    """
    Convert a string version of a function name to the callable object.
    
    copy and pasted from django url resolving
    """
    mod_name, func_name = get_mod_func(lookup_string)

    function = getattr(import_module(mod_name), func_name) # we let the attribute error bubble
    if not callable(function):
        raise TypeError(
            "Could not import %s.%s. SMS Handler is not callable." %
            (mod_name, func_name))

    return function

def get_mod_func(callback):
    """
    Copy and pasted from url resolving
    
    Converts 'django.views.news.stories.story_detail' to
    ['django.views.news.stories', 'story_detail']
    """
    try:
        dot = callback.rindex('.')
    except ValueError:
        return callback, ''
    return callback[:dot], callback[dot+1:]
    

def get_class(path): 
    """
    Copy and pasted from middleware resolving,
    
    pulls out and imports the given class
    """
    try:
        module, classname = path.rsplit('.', 1)
        mod = import_module(module)
        klass = getattr(mod, mw_classname)
    except:
        raise ValueError("Error finding SMS sender class: %s" % path)
        
    return klass
