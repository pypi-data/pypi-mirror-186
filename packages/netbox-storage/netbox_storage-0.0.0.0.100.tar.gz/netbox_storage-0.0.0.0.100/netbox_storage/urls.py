from django.urls import path

from netbox.views.generic import ObjectChangeLogView

from netbox_storage.models import Drive, Filesystem, LinuxVolume, WindowsVolume
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
    # WindowsVolume
    WindowsVolumeListView,
    WindowsVolumeView,
    WindowsVolumeDeleteView,
    WindowsVolumeEditView,
    WindowsVolumeBulkImportView,
    WindowsVolumeBulkEditView,
    WindowsVolumeBulkDeleteView,
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
    path("windowsvolume/", WindowsVolumeListView.as_view(), name="windowsvolume_list"),
    path("windowsvolume/add/", WindowsVolumeEditView.as_view(), name="windowsvolume_add"),
    path("windowsvolume/import/", WindowsVolumeBulkImportView.as_view(), name="windowsvolume_import"),
    path("windowsvolume/edit/", WindowsVolumeBulkEditView.as_view(), name="windowsvolume_bulk_edit"),
    path("windowsvolume/delete/", WindowsVolumeBulkDeleteView.as_view(), name="windowsvolume_bulk_delete"),
    path("windowsvolume/<int:pk>/", WindowsVolumeView.as_view(), name="windowsvolume"),
    path("windowsvolume/<int:pk>/edit/", WindowsVolumeEditView.as_view(), name="windowsvolume_edit"),
    path("windowsvolume/<int:pk>/delete/", WindowsVolumeDeleteView.as_view(), name="windowsvolume_delete"),
    path(
        "windowsvolume/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="windowsvolume_changelog",
        kwargs={"model": WindowsVolume},
    ),
]
