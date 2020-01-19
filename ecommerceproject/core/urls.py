
from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^lst', views.base_view ),
    url(r'^$', views.ListViews.as_view(),name='list_view' ),
    url(r'^(?P<slug>[-\w]+)/$', views.DetailViews.as_view(),name='detail_view' ),
    url(r'^(?P<slug>[-\w]+)/$', views.add_to_cart,name='add_to_cart_view' ),
]
