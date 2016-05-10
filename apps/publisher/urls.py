from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^review', views.review, name='review'),
    url(r'^search$', views.search, name='search'),
    url(r'^new$', views.new, name='new'),
    url(r'^finddoi$', views.finddoi),
    url(r'^review/', views.review, name='review'),
    url(r'^edit/(\d+)', views.edit, name='edit'),
    url(r'^delete/(\d+)', views.delete, name='delete'),
    url(r'^ajax/?$', views.ajax),
    url(r'^ajax/citation/(?P<pub_id>\d+)/$', views.ajax_citation),
    url(r'^ajax/moreinfo/(?P<pub_id>\d+)/$', views.ajax_more_info),
    url(r'^ajax/data/prefetch_authors/$', views.ajax_prefetch_authors),
    url(r'^ajax/data/all_authors/$', views.ajax_all_authors),
]