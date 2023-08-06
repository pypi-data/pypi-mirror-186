from __future__ import unicode_literals

from django.urls import path
from nautobot.extras.views import ObjectChangeLogView
from . import views
from .models import SFPType, SFP

app_name = 'nautobot_sfp_inventory'
urlpatterns = [
    path("sfp-types/", views.SFPTypeListView.as_view(), name="sfptype_list"),
    path("sfp-types/add/", views.SFPTypeEditView.as_view(), name="sfptype_add"),
    path(
        "sfp-types/import/",
        views.SFPTypeBulkImportView.as_view(),
        name="sfptype_import",
    ),
    path(
        "sfp-types/delete/",
        views.SFPTypeBulkDeleteView.as_view(),
        name="sfptype_bulk_delete",
    ),
    path("sfp-types/<uuid:pk>/", views.SFPTypeView.as_view(), name="sfptype"),
    path(
        "sfp-types/<uuid:pk>/edit/",
        views.SFPTypeEditView.as_view(),
        name="sfptype_edit",
    ),
    path(
        "sfp-types/<uuid:pk>/delete/",
        views.SFPTypeDeleteView.as_view(),
        name="sfptype_delete",
    ),
    path(
        "sfp-types/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="sfptype_changelog",
        kwargs={"model": SFPType},
    ),
    path("sfps/", views.SFPListView.as_view(), name="sfp_list"),
    path("sfps/add/", views.SFPEditView.as_view(), name="sfp_add"),
    path("sfps/bulk-add/", views.SFPBulkCreateView.as_view(), name="sfp_bulk_add"),
    path(
        "sfps/edit/",
        views.SFPBulkEditView.as_view(),
        name="sfp_bulk_edit",
    ),
    path(
        "sfps/import/",
        views.SFPBulkImportView.as_view(),
        name="sfp_import",
    ),
    path(
        "sfps/delete/",
        views.SFPBulkDeleteView.as_view(),
        name="sfp_bulk_delete",
    ),
    path("sfps/<uuid:pk>/", views.SFPView.as_view(), name="sfp"),
    path(
        "sfps/<uuid:pk>/edit/",
        views.SFPEditView.as_view(),
        name="sfp_edit",
    ),
    path(
        "sfps/<uuid:pk>/delete/",
        views.SFPDeleteView.as_view(),
        name="sfp_delete",
    ),
    path(
        "sfps/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="sfp_changelog",
        kwargs={"model": SFP},
    ),
]
