import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
    ActionsColumn,
)

from netbox_storage.models import LinuxVolume


class LinuxVolumeBaseTable(NetBoxTable):
    """Base class for tables displaying LinuxVolume"""

    filesystem = tables.Column(
        linkify=True,
    )
    vg_name = tables.Column(
        linkify=True,
    )


class LinuxVolumeTable(LinuxVolumeBaseTable):
    """Table for displaying LinuxVolume objects."""

    pk = ToggleColumn()

    class Meta(NetBoxTable.Meta):
        model = LinuxVolume
        fields = (
            "pk",
            "vg_name",
            "lv_name",
            "path",
            "filesystem",
            "description",
        )
        default_columns = (
            "filesystem",
            "description"
        )


class RelatedLinuxVolumeTable(LinuxVolumeBaseTable):
    actions = ActionsColumn(actions=())

    class Meta(NetBoxTable.Meta):
        model = LinuxVolume
        fields = (
            "pk",
            "vg_name",
            "lv_name",
            "path",
            "filesystem",
            "description",
        )
        default_columns = (
            "filesystem",
            "description"
        )

