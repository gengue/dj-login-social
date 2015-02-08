from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view() ,name="home"),
    url(r'^login$', views.SigninView.as_view(), name="Signin"),
)
