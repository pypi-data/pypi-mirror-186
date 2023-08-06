import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
    ActionsColumn,
)

from netbox_storage.models import WindowsVolume


class WindowsVolumeBaseTable(NetBoxTable):
    """Base class for tables displaying WindowsVolume"""

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


class WindowsVolumeTable(WindowsVolumeBaseTable):
    """Table for displaying WindowsVolume objects."""

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
            "description"
        )


class RelatedWindowsVolumeTable(WindowsVolumeBaseTable):
    actions = ActionsColumn(actions=())

    class Meta(NetBoxTable.Meta):
        model = WindowsVolume
        fields = (
            "pk",
            "drive_name",
            "fs",
            "description",
        )
        default_columns = (
            "drive_name",
            "fs",
            "description"
        )

