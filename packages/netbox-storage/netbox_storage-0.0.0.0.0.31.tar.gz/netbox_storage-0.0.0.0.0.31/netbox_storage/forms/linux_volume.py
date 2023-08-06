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
    APISelect,
)

from django.urls import reverse_lazy

from netbox_storage.models import Filesystem, LinuxVolume


class LinuxVolumeForm(NetBoxModelForm):
    """Form for creating a new LinuxVolume object."""

    vg_name = CharField(
        label="VG Name",
    )
    lv_name = CharField(
        label="LV Name",
    )
    path = CharField(
        label="Path",
    )
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
    )

    class Meta:
        model = LinuxVolume

        fields = (
            "vg_name",
            "lv_name",
            "fs",
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
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        label="Filesystem Name",
    )


class LinuxVolumeImportForm(NetBoxModelImportForm):
    fs = DynamicModelChoiceField(
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
            "fs",
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
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False,
        label="Filesystem Name",
    )
    description = CharField(max_length=255, required=False)

    fieldsets = (
        (
            None,
            ("vg_name", "lv_name", "path", "fs", "description"),
        ),
    )
    nullable_fields = ["description"]
