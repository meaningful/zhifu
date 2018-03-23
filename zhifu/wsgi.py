"""
WSGI config for zhifu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
output = 'sys.path = %s\n' % repr(sys.path)
output += 'sys.version = %s\n' % repr(sys.version)
output += 'sys.prefix = %s\n' % repr(sys.prefix)

#print(output)
#sys.path = ['/home/liujie/PycharmProjects/zhifu', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/home/liujie/PycharmProjects/zhifu/venv/lib/python3.5/site-packages', '/home/liujie/PycharmProjects/zhifu/venv/lib/python3.5/site-packages/setuptools-28.8.0-py3.5.egg', '/home/liujie/PycharmProjects/zhifu/venv/lib/python3.5/site-packages/pip-9.0.1-py3.5.egg']

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhifu.settings")

application = get_wsgi_application()
