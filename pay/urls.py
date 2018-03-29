from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.zhifu, name='zhifu'),
    url(r"^aapay/$", views.pay),
    url(r"^check_pay/$", views.check_pay),
]