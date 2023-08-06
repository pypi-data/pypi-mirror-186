from django.urls import path

from netbox.views.generic import ObjectChangeLogView

from netbox_storage.models import Drive, Filesystem, LinuxVolume, LinuxVolumeDrive
from netbox_storage.views import (
    # Drive View
    DriveListView,
    DriveView,
    DriveEditView,
    DriveDeleteView,
    DriveBulkImportView,
    DriveBulkEditView,
    DriveBulkDeleteView,
    # Filesystem Views
    FilesystemListView,
    FilesystemView,
    FilesystemEditView,
    FilesystemDeleteView,
    FilesystemBulkImportView,
    FilesystemBulkEditView,
    FilesystemBulkDeleteView,
    # LinuxVolume
    LinuxVolumeListView,
    LinuxVolumeView,
    LinuxVolumeDeleteView,
    LinuxVolumeEditView,
    LinuxVolumeBulkImportView,
    LinuxVolumeBulkEditView,
    LinuxVolumeBulkDeleteView,
    # LinuxVolume
    LinuxVolumeDriveListView,
    LinuxVolumeDriveView,
    LinuxVolumeDriveDeleteView,
    LinuxVolumeDriveEditView,
    LinuxVolumeDriveBulkImportView,
    LinuxVolumeDriveBulkEditView,
    LinuxVolumeDriveBulkDeleteView,
)

app_name = "netbox_storage"

urlpatterns = [
    #
    # Drive urls
    #
    path("drive/", DriveListView.as_view(), name="drive_list"),
    path("drive/add/", DriveEditView.as_view(), name="drive_add"),
    path("drive/import/", DriveBulkImportView.as_view(), name="drive_import"),
    path("drive/edit/", DriveBulkEditView.as_view(), name="drive_bulk_edit"),
    path("drive/delete/", DriveBulkDeleteView.as_view(), name="drive_bulk_delete"),
    path("drive/<int:pk>/", DriveView.as_view(), name="drive"),
    path("drive/<int:pk>/edit/", DriveEditView.as_view(), name="drive_edit"),
    path("drive/<int:pk>/delete/", DriveDeleteView.as_view(), name="drive_delete"),
    path(
        "drive/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="drive_changelog",
        kwargs={"model": Drive},
    ),
    #
    # Filesystem urls
    #
    path("filesystem/", FilesystemListView.as_view(), name="filesystem_list"),
    path("filesystem/add/", FilesystemEditView.as_view(), name="filesystem_add"),
    path("filesystem/import/", FilesystemBulkImportView.as_view(), name="filesystem_import"),
    path("filesystem/edit/", FilesystemBulkEditView.as_view(), name="filesystem_bulk_edit"),
    path("filesystem/delete/", FilesystemBulkDeleteView.as_view(), name="filesystem_bulk_delete"),
    path("filesystem/<int:pk>/", FilesystemView.as_view(), name="filesystem"),
    path("filesystem/<int:pk>/edit/", FilesystemEditView.as_view(), name="filesystem_edit"),
    path("filesystem/<int:pk>/delete/", FilesystemDeleteView.as_view(), name="filesystem_delete"),
    path(
        "filesystem/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="filesystem_changelog",
        kwargs={"model": Filesystem},
    ),
    #
    # LinuxVolume urls
    #
    path("linuxvolume/", LinuxVolumeListView.as_view(), name="linuxvolume_list"),
    path("linuxvolume/add/", LinuxVolumeEditView.as_view(), name="linuxvolume_add"),
    path("linuxvolume/import/", LinuxVolumeBulkImportView.as_view(), name="linuxvolume_import"),
    path("linuxvolume/edit/", LinuxVolumeBulkEditView.as_view(), name="linuxvolume_bulk_edit"),
    path("linuxvolume/delete/", LinuxVolumeBulkDeleteView.as_view(), name="linuxvolume_bulk_delete"),
    path("linuxvolume/<int:pk>/", LinuxVolumeView.as_view(), name="linuxvolume"),
    path("linuxvolume/<int:pk>/edit/", LinuxVolumeEditView.as_view(), name="linuxvolume_edit"),
    path("linuxvolume/<int:pk>/delete/", LinuxVolumeDeleteView.as_view(), name="linuxvolume_delete"),
    path(
        "linuxvolume/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="linuxvolume_changelog",
        kwargs={"model": LinuxVolume},
    ),
    #
    # LinuxVolume urls
    #
    path("linuxvolumedrive/", LinuxVolumeDriveListView.as_view(), name="linuxvolumedrive_list"),
    path("linuxvolumedrive/add/", LinuxVolumeDriveEditView.as_view(), name="linuxvolumedrive_add"),
    path("linuxvolumedrive/import/", LinuxVolumeDriveBulkImportView.as_view(), name="linuxvolumedrive_import"),
    path("linuxvolumedrive/edit/", LinuxVolumeDriveBulkEditView.as_view(), name="linuxvolumedrive_bulk_edit"),
    path("linuxvolumedrive/delete/", LinuxVolumeDriveBulkDeleteView.as_view(), name="linuxvolumedrive_bulk_delete"),
    path("linuxvolumedrive/<int:pk>/", LinuxVolumeDriveView.as_view(), name="linuxvolumedrive"),
    path("linuxvolumedrive/<int:pk>/edit/", LinuxVolumeDriveEditView.as_view(), name="linuxvolumedrive_edit"),
    path("linuxvolumedrive/<int:pk>/delete/", LinuxVolumeDriveDeleteView.as_view(), name="linuxvolumedrive_delete"),
    path(
        "linuxvolumedrive/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="linuxvolume_changelog",
        kwargs={"model": LinuxVolumeDrive},
    ),
]
