from django.forms import (
    CharField,
)

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms import (
    DynamicModelChoiceField,
)

from netbox_storage.models import Filesystem, WindowsVolume


class WindowsVolumeForm(NetBoxModelForm):
    """Form for creating a new LinuxVolume object."""

    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )

    class Meta:
        model = WindowsVolume

        fields = (
            "drive_name",
            "filesystem",
            "description",
        )


class WindowsVolumeFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering LinuxVolume instances."""

    model = WindowsVolume

    drive_name = CharField(
        required=False,
        label="VG Name",
    )
    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )


class WindowsVolumeImportForm(NetBoxModelImportForm):
    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = WindowsVolume

        fields = (
            "drive_name",
            "filesystem",
            "description",
        )


class WindowsVolumeBulkEditForm(NetBoxModelBulkEditForm):
    model = WindowsVolume

    drive_name = CharField(
        required=False,
        label="Drive Name",
    )
    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )
    description = CharField(max_length=255, required=False)

    fieldsets = (
        (
            None,
            ("drive_name", "filesystem", "description"),
        ),
    )
    nullable_fields = ["description"]

