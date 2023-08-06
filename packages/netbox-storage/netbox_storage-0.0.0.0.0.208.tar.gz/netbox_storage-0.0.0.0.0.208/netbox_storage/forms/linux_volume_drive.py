from django.core.validators import MinValueValidator
from django.forms import (
    CharField, IntegerField,
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

from netbox_storage.models import Filesystem, LinuxVolumeDrive, Drive, LinuxVolume


class LinuxVolumeDriveForm(NetBoxModelForm):
    """Form for creating a new LinuxVolume object."""

    allocation = IntegerField(
        required=True,
        label="Size (GB)",
        help_text="The size of the drive e.g. 25",
        validators=[MinValueValidator(1)],
    )
    linuxvolume = CharField(
        queryset=LinuxVolume.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )
    drive = DynamicModelChoiceField(
        queryset=Drive.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )

    class Meta:
        model = LinuxVolumeDrive

        fields = (
            "drive",
            "linuxvolume",
            "allocation",
            "description",
        )


class LinuxVolumeDriveFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering LinuxVolume instances."""

    model = LinuxVolumeDrive

    allocation = IntegerField(
        required=True,
        label="Size (GB)",
        help_text="The size of the drive e.g. 25",
        validators=[MinValueValidator(1)],
    )
    linuxvolume = CharField(
        queryset=LinuxVolume.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )
    drive = DynamicModelChoiceField(
        queryset=Drive.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )


class LinuxVolumeDriveImportForm(NetBoxModelImportForm):
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = LinuxVolumeDrive

        fields = (
            "drive",
            "linuxvolume",
            "allocation",
            "description",
        )


class LinuxVolumeDriveBulkEditForm(NetBoxModelBulkEditForm):
    model = LinuxVolumeDrive

    allocation = IntegerField(
        required=True,
        label="Size (GB)",
        help_text="The size of the drive e.g. 25",
        validators=[MinValueValidator(1)],
    )
    linuxvolume = CharField(
        queryset=LinuxVolume.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )
    drive = DynamicModelChoiceField(
        queryset=Drive.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )
    description = CharField(max_length=255, required=False)

    fieldsets = (
        (
            None,
            ("drive", "linuxvolume", "allocation", "description",),
        ),
    )
    nullable_fields = ["description"]
