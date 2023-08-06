
from django.forms import (
    CharField,

)

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)


from netbox_storage.models import Filesystem


class FilesystemForm(NetBoxModelForm):
    """Form for creating a new Filesystem object."""
    filesystem = CharField(
        required=True,
        label="Filesystem Name",
        help_text="The name of the filesystem e.g. ext4, NTFS",
    )
    description = CharField(
        required=False,
        label="Description",
        help_text="Short Description e.g. NTFS is a Filesystem for Windows",
    )

    class Meta:
        model = Filesystem

        fields = (
            "filesystem",
            "description",
        )


class FilesystemFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering Filesystem instances."""

    model = Filesystem

    filesystem = CharField(
        required=False,
        label="Filesystem Name",
    )


class FilesystemImportForm(NetBoxModelImportForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Filesystem

        fields = (
            "filesystem",
            "description",
        )


class FilesystemBulkEditForm(NetBoxModelBulkEditForm):
    model = Filesystem

    filesystem = CharField(
        required=False,
        label="Filesystem Name",
    )
    description = CharField(max_length=255, required=False)

    fieldsets = (
        (
            None,
            ("filesystem", "description"),
        ),
    )
    nullable_fields = ["description"]
