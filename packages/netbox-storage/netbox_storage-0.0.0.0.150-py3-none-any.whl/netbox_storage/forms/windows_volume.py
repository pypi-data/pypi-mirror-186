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
    DynamicModelChoiceField, DynamicModelMultipleChoiceField,
)

from netbox_storage.models import Filesystem, WindowsVolume, Drive
from virtualization.models import VirtualMachine


class WindowsVolumeForm(NetBoxModelForm):
    """Form for creating a new LinuxVolume object."""

    drive_name = CharField(
        label="Drive Name",
        help_text="The drive name of the windows volume e.g. D",
    )
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        label="Filesystem Name",
        help_text="The Filesystem of the Volume e.g. NTFS",
    )
    description = CharField(
        required=False,
        label="Description",
        help_text="Short Description e.g. C: System Volume",
    )
    virtual_machine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )
    drives = DynamicModelMultipleChoiceField(
        queryset=Drive.objects.all(),
        label="Drives",
        required=False,
        help_text="The mapped drives to the volume e.g. Hard Drive 1",
    )
    size = IntegerField(
        required=False,
        label="Size (GB)",
        help_text="The size of the disk size mapping e.g. 25",
        validators=[MinValueValidator(1)],
    )
    loaded_drive = Drive.objects.all()

    fieldsets = (
        (
            "Windows Volume Configuration",
            (
                "drive_name",
                "fs",
                "virtual_machine",
                "description"
            ),
        ),
        (
            "Drive Configuration",
            (
                "drives",
                "size"
            ),
        ),
    )

    class Meta:
        model = WindowsVolume

        fields = (
            "drive_name",
            "fs",
            "drives",
            "virtual_machine",
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

