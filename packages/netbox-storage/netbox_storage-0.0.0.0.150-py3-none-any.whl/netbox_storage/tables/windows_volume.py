import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
)

from netbox_storage.models import WindowsVolume


class WindowsVolumeTable(NetBoxTable):
    """Table for displaying WindowsVolume objects."""
    fs = tables.Column(
        linkify=True,
    )
    drive_name = tables.Column(
        linkify=True,
        verbose_name="Drive Name"
    )
    virtual_machine = tables.Column(
        linkify=True
    )

    pk = ToggleColumn()

    class Meta(NetBoxTable.Meta):
        model = WindowsVolume
        fields = (
            "pk",
            "drive_name",
            "fs",
            "drives",
            "virtual_machine",
            "description",
        )
        default_columns = (
            "drive_name",
            "fs",
            "drives",
            "virtual_machine"
        )
