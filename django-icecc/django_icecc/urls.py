from django.conf.urls.defaults import patterns
from django_icecc.views import *

urlpatterns = patterns('',
    # Example:
    (r'^listcs/?$', listcs),
    (r'^listjobs/?$', listjobs),
    (r'^internals/?$', internals),
    (r'^blockcs/?$', blockcs),
    (r'^/?$', summary),
    
)
