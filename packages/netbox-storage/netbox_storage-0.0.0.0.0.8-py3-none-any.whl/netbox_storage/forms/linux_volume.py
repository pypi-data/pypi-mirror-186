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

from netbox_storage.models import Filesystem, LinuxVolume


class LinuxVolumeForm(NetBoxModelForm):
    """Form for creating a new LinuxVolume object."""

    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )

    class Meta:
        model = LinuxVolume

        fields = (
            "vg_name",
            "lv_name",
            "filesystem",
            "path",
            "description",
        )


class LinuxVolumeFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering LinuxVolume instances."""

    model = LinuxVolume

    vg_name = CharField(
        required=False,
        label="VG Name",
    )
    lv_name = CharField(
        required=False,
        label="LV Name",
    )
    path = CharField(
        required=False,
        label="Path",
    )
    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )


class LinuxVolumeImportForm(NetBoxModelImportForm):
    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = LinuxVolume

        fields = (
            "vg_name",
            "lv_name",
            "filesystem",
            "path",
            "description",
        )


class LinuxVolumeBulkEditForm(NetBoxModelBulkEditForm):
    model = LinuxVolume

    vg_name = CharField(
        required=False,
        label="VG Name",
    )
    lv_name = CharField(
        required=False,
        label="LV Name",
    )
    path = CharField(
        required=False,
        label="Path",
    )
    filesystem = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )
    description = CharField(max_length=255, required=False)

    fieldsets = (
        (
            None,
            ("vg_name", "lv_name", "path", "filesystem", "description"),
        ),
    )
    nullable_fields = ["description"]

