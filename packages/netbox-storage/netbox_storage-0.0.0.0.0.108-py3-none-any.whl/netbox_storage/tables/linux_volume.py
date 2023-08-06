import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
    ActionsColumn,
)

from netbox_storage.models import LinuxVolume


class LinuxVolumeBaseTable(NetBoxTable):
    """Base class for tables displaying LinuxVolume"""

    fs = tables.Column(
        linkify=True,
        verbose_name="Filesystem"
    )
    vg_name = tables.Column(
        linkify=True,
        verbose_name="Volume Group Name"
    )
    lv_name = tables.Column(
        linkify=True,
        verbose_name="Logical Volume Name"
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
            "fs",
            "description",
        )
        default_columns = (
            "vg_name",
            "lv_name",
            "path",
            "fs",
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
            "fs",
            "description",
        )
        default_columns = (
            "fs",
            "description"
        )

