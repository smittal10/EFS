# This file contains the WSGI configuration required to serve up your
# web application at http://adeora7.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://www.pythonanywhere.com/wiki/DebuggingImportError


# +++++++++++ HELLO WORLD +++++++++++
# A little pure-wsgi hello world we've cooked up, just
# to prove everything works.  You should delete this
# code to get your own working.
# def application(environ, start_response):
    # if environ.get('PATH_INFO') == '/':
import sys
sys.path.insert(0, '/home/adeora7/efs/')
from my_inverted_index import display_results

def application(environ, start_response):
    if environ.get('PATH_INFO') == '/':
        a = environ['QUERY_STRING']
        if(len(a.split('=')) == 2):
            status = '200 OK'
            response_headers = [('Content-type', 'text/plain')]
            start_response(status, response_headers)
            q = a.split('=')[1]
            q = q.replace('%20',' ')
            result = display_results(q)
            c = ""
            for a in result:
                for b in a:
                    c = c + "," + b
            return [c.encode('utf-8')]
        else:
            status = '200 OK'
            response_headers = [('Content-type', 'text/html')]
            start_response(status, response_headers)
            filelike = open('/home/adeora7/efs/views/index.html', 'rb')
            block_size = 4096
            if 'wsgi.file_wrapper' in environ:
                    return environ['wsgi.file_wrapper'](filelike, block_size)
            else:
                return iter(lambda: filelike.read(block_size), '')
    elif environ.get('PATH_INFO') == '/views/main.js':
        status = '200 OK'
        response_headers = [('Content-type', 'application/javascript')]
        start_response(status, response_headers)

        filelike = open('/home/adeora7/efs/views/main.js', 'rb')
        block_size = 4096

        if 'wsgi.file_wrapper' in environ:
                return environ['wsgi.file_wrapper'](filelike, block_size)
        else:
            return iter(lambda: filelike.read(block_size), '')
    elif environ.get('PATH_INFO') == '/views/main.css':
        status = '200 OK'
        response_headers = [('Content-type', 'text/css')]
        start_response(status, response_headers)

        filelike = open('/home/adeora7/efs/views/main.css', 'rb')
        block_size = 4096

        if 'wsgi.file_wrapper' in environ:
                return environ['wsgi.file_wrapper'](filelike, block_size)
        else:
            return iter(lambda: filelike.read(block_size), '')
    elif environ.get('PATH_INFO') == '/views/fonts/AlexBrush-Regular.ttf':
        status = '200 OK'
        response_headers = [('Content-type', 'application/x-font-ttf')]
        start_response(status, response_headers)

        filelike = open('/home/adeora7/efs/views/fonts/AlexBrush-Regular.ttf', 'rb')
        block_size = 4096

        if 'wsgi.file_wrapper' in environ:
                return environ['wsgi.file_wrapper'](filelike, block_size)
        else:
            return iter(lambda: filelike.read(block_size), '')
    # else:
    #     status = '200 OK'
    #     response_header = [('Content-type', 'text/html')]
    #     start_response(status, response_header)
    #     content = 'a,b,c,d,e,f'
    #     return content.encode('utf-8')
# Below are templates for Django and Flask.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload /yourdomain.com/' button on the 'Web' tab to make your site
# live.

# +++++++++++ VIRTUALENV +++++++++++
# If you want to use a virtualenv, set its path on the web app setup tab.
# Then come back here and import your application object as per the
# instructions below


# +++++++++++ CUSTOM WSGI +++++++++++
# If you have a WSGI file that you want to serve using PythonAnywhere, perhaps
# in your home directory under version control, then use something like this:
#
#import sys
#
#path = '/home/adeora7/path/to/my/app
#if path not in sys.path:
#    sys.path.append(path)
#
#from my_wsgi_file import application


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/adeora7/mysite/mysite/settings.py'
## and your manage.py is is at '/home/adeora7/mysite/manage.py'
#path = '/home/adeora7/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then, for django >=1.5:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
## or, for older django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()



# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
#
#import sys
#
## The "/home/adeora7" below specifies your home
## directory -- the rest should be the directory you uploaded your Flask
## code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
## ...or uploaded files to the directory "myproject", then you should
## specify "/home/adeora7/myproject"
#path = '/home/adeora7/path/to/flask_app_directory'
#if path not in sys.path:
#    sys.path.append(path)
#
## After you uncomment the line below, the yellow triangle on the left
## side in our in-browser editor shows a warning saying:
##     'application' imported but unused.
## You can ignore this error. The line is necessary, and the variable
## is used externally.
#from main_flask_app_file import app as application
#
# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.
