from netbox.views import generic

from netbox_storage.filters import LinuxVolumeFilter
from netbox_storage.forms import (
    LinuxVolumeImportForm,
    LinuxVolumeFilterForm,
    LinuxVolumeForm,
    LinuxVolumeBulkEditForm
)

from netbox_storage.models import LinuxVolume
from netbox_storage.tables import LinuxVolumeTable


class LinuxVolumeListView(generic.ObjectListView):
    queryset = LinuxVolume.objects.all()
    filterset = LinuxVolumeFilter
    filterset_form = LinuxVolumeFilterForm
    table = LinuxVolumeTable


class LinuxVolumeView(generic.ObjectView):
    """Display LinuxVolume details"""

    queryset = LinuxVolume.objects.all()


class LinuxVolumeEditView(generic.ObjectEditView):
    """View for editing a LinuxVolume instance."""

    queryset = LinuxVolume.objects.all()
    form = LinuxVolumeForm
    default_return_url = "plugins:netbox_storage:linuxvolume_list"


class LinuxVolumeDeleteView(generic.ObjectDeleteView):
    queryset = LinuxVolume.objects.all()
    default_return_url = "plugins:netbox_storage:linuxvolume_list"


class LinuxVolumeBulkImportView(generic.BulkImportView):
    queryset = LinuxVolume.objects.all()
    model_form = LinuxVolumeImportForm
    table = LinuxVolumeTable
    default_return_url = "plugins:netbox_storage:linuxvolume_list"


class LinuxVolumeBulkEditView(generic.BulkEditView):
    queryset = LinuxVolume.objects.all()
    filterset = LinuxVolumeFilter
    table = LinuxVolumeTable
    form = LinuxVolumeBulkEditForm


class LinuxVolumeBulkDeleteView(generic.BulkDeleteView):
    queryset = LinuxVolume.objects.all()
    table = LinuxVolumeTable

