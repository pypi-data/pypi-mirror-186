from netbox.views import generic

from netbox_storage.filters import LinuxVolumeDriveFilter
from netbox_storage.forms import (
    LinuxVolumeDriveImportForm,
    LinuxVolumeDriveFilterForm,
    LinuxVolumeDriveForm,
    LinuxVolumeDriveBulkEditForm
)

from netbox_storage.models import LinuxVolumeDrive
from netbox_storage.tables import LinuxVolumeDriveTable


class LinuxVolumeDriveListView(generic.ObjectListView):
    queryset = LinuxVolumeDrive.objects.all()
    filterset = LinuxVolumeDriveFilter
    filterset_form = LinuxVolumeDriveFilterForm
    table = LinuxVolumeDriveTable


class LinuxVolumeDriveView(generic.ObjectView):
    """Display LinuxVolume details"""

    queryset = LinuxVolumeDrive.objects.all()


class LinuxVolumeDriveEditView(generic.ObjectEditView):
    """View for editing a LinuxVolumeDrive instance."""

    queryset = LinuxVolumeDrive.objects.all()
    form = LinuxVolumeDriveForm
    default_return_url = "plugins:netbox_storage:linuxvolumedrive_list"


class LinuxVolumeDriveDeleteView(generic.ObjectDeleteView):
    queryset = LinuxVolumeDrive.objects.all()
    default_return_url = "plugins:netbox_storage:linuxvolumedrive_list"


class LinuxVolumeDriveBulkImportView(generic.BulkImportView):
    queryset = LinuxVolumeDrive.objects.all()
    model_form = LinuxVolumeDriveImportForm
    table = LinuxVolumeDriveTable
    default_return_url = "plugins:netbox_storage:linuxvolumedrive_list"


class LinuxVolumeDriveBulkEditView(generic.BulkEditView):
    queryset = LinuxVolumeDrive.objects.all()
    filterset = LinuxVolumeDriveFilter
    table = LinuxVolumeDriveTable
    form = LinuxVolumeDriveBulkEditForm


class LinuxVolumeDriveBulkDeleteView(generic.BulkDeleteView):
    queryset = LinuxVolumeDrive.objects.all()
    table = LinuxVolumeDriveTable

