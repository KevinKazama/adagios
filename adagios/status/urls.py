from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^/?$', 'status.views.status_hostgroup'),
    (r'^/test/?$', 'status.views.test_livestatus'),
    (r'^/treeview/(?P<hostgroup_name>.+)?/?$', 'status.views.status_treeview'),
    (r'^/parents/?$', 'status.views.status_parents'),
    (r'^/hostgroups/?$', 'status.views.status_hostgroup'),
    (r'^/hostgroups/(?P<hostgroup_name>.+)/?$', 'status.views.status_hostgroup'),
    (r'^/hosts/?$', 'status.views.status'),
    (r'^/hosts/(?P<host_name>.+)/(?P<service_description>.+)/?$', 'status.views.status_detail'),
    (r'^/hosts/(?P<host_name>.+)/$', 'status.views.status_detail'),
    (r'^/hosts/(?P<host_name>.+)$', 'status.views.status_detail'),
    )
 
