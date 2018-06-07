from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateTimeView, DetailsTimeView, CreatePrimeiraFaseView, DetailsPrimeiraFaseView

urlpatterns = {
    url(r'^times/$', CreateTimeView.as_view(), name="create"),
    url(r'^times/(?P<pk>[0-9]+)/$',
        DetailsTimeView.as_view(), name="details"),

    url(r'^primeira-fase/$', CreatePrimeiraFaseView.as_view(), name="create"),
    url(r'^primeira-fase/(?P<pk>[0-9]+)/$',
        DetailsPrimeiraFaseView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)