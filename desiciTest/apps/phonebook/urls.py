from django.conf.urls import re_path

from apps.phonebook.views import person
from apps.phonebook.views.person import PersonView, PersonDetailView,\
    PersonRenderPage, PersonEditPage
from apps.phonebook.views.address import AddressView, AddressDetailView
from apps.phonebook.views.phone import PhoneView, PhoneDetailView
from django.urls import path


urlpatterns = [
    re_path(
        route=r"^person/?$",
        view=PersonView.as_view(),
        name="person_view",
    ),
    re_path(
        route=r"^person/add/?$",
        view=PersonRenderPage.as_view(),
        name="person_render_page",
    ),
    re_path(
        route=r"^person/edit/(?P<pk>\w+)/?$",
        view=PersonEditPage.as_view(),
        name="person_edit_page",
    ),
    re_path(
        route=r"^api/v1/person/(?P<pk>\w+)/$",
        view=PersonDetailView.as_view(),
        name="person_detail_view"
    ),
    re_path(
        route=r"^api/v1/person/(?P<pk>\w+)/$",
        view=PersonDetailView.as_view(),
        name="person_detail_view_v1"
    ),
    re_path(
        route=r"^api/v1/address/(?P<pk>\w+)/$",
        view=AddressDetailView.as_view(),
        name="address_detail_view_v1"
    ),
    re_path(
        route=r"^api/v1/address/?$",
        view=AddressView.as_view(),
        name="address_view_v1",
    ),
    re_path(
        route=r"^api/v1/phone/?$",
        view=PhoneView.as_view(),
        name="phone_view_v1",
    ),
    re_path(
        route=r"^api/v1/phone/(?P<pk>\w+)/$",
        view=PhoneDetailView.as_view(),
        name="phone_detail_view_v1"
    ),
]
