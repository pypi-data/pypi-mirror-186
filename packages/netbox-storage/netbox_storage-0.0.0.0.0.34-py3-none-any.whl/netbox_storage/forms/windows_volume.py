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
    DynamicModelChoiceField, DynamicModelMultipleChoiceField,
)

from netbox_storage.models import Filesystem, WindowsVolume, Drive


class WindowsVolumeForm(NetBoxModelForm):
    """Form for creating a new LinuxVolume object."""

    drive_name = CharField(
        label="Drive Name",
    )
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        label="Filesystem Name",
    )
    drives = DynamicModelMultipleChoiceField(
        queryset=Drive.objects.all(),
        label="Drives",
    )

    class Meta:
        model = WindowsVolume

        fields = (
            "drive_name",
            "fs",
            "drives",
            "description",
        )


class WindowsVolumeFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering LinuxVolume instances."""

    model = WindowsVolume

    drive_name = CharField(
        required=False,
        label="VG Name",
    )
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False,
        label="Filesystem Name",
    )


class WindowsVolumeImportForm(NetBoxModelImportForm):
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = WindowsVolume

        fields = (
            "drive_name",
            "fs",
            "description",
        )


class WindowsVolumeBulkEditForm(NetBoxModelBulkEditForm):
    model = WindowsVolume

    drive_name = CharField(
        required=False,
        label="Drive Name",
    )
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )
    description = CharField(max_length=255, required=False)

    fieldsets = (
        (
            None,
            ("drive_name", "fs", "description"),
        ),
    )
    nullable_fields = ["description"]

