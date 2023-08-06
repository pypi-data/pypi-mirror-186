from netbox.views import generic

from netbox_storage.filters import WindowsVolumeFilter
from netbox_storage.forms import (
    WindowsVolumeImportForm,
    WindowsVolumeFilterForm,
    WindowsVolumeForm,
    WindowsVolumeBulkEditForm
)

from netbox_storage.models import WindowsVolume
from netbox_storage.tables import WindowsVolumeTable


class WindowsVolumeListView(generic.ObjectListView):
    queryset = WindowsVolume.objects.all()
    filterset = WindowsVolumeFilter
    filterset_form = WindowsVolumeFilterForm
    table = WindowsVolumeTable


class WindowsVolumeView(generic.ObjectView):
    """Display WindowsVolume details"""

    queryset = WindowsVolume.objects.all()


class WindowsVolumeEditView(generic.ObjectEditView):
    """View for editing a WindowsVolume instance."""

    queryset = WindowsVolume.objects.all()
    form = WindowsVolumeForm
    template_name = "netbox_storage/volume/windowsvolume_add.html",
    default_return_url = "plugins:netbox_storage:windowsvolume_list"


class WindowsVolumeDeleteView(generic.ObjectDeleteView):
    queryset = WindowsVolume.objects.all()
    default_return_url = "plugins:netbox_storage:windowsvolume_list"


class WindowsVolumeBulkImportView(generic.BulkImportView):
    queryset = WindowsVolume.objects.all()
    model_form = WindowsVolumeImportForm
    table = WindowsVolumeTable
    default_return_url = "plugins:netbox_storage:windowsvolume_list"


class WindowsVolumeBulkEditView(generic.BulkEditView):
    queryset = WindowsVolume.objects.all()
    filterset = WindowsVolumeFilter
    table = WindowsVolumeTable
    form = WindowsVolumeBulkEditForm


class WindowsVolumeBulkDeleteView(generic.BulkDeleteView):
    queryset = WindowsVolume.objects.all()
    table = WindowsVolumeTable

