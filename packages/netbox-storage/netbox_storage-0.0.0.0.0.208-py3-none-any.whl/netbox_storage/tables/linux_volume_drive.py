import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
    ActionsColumn,
)

from netbox_storage.models import LinuxVolumeDrive


class LinuxVolumeDriveBaseTable(NetBoxTable):
    """Base class for tables displaying LinuxVolume"""

    drive = tables.Column(
        linkify=True,
        verbose_name="drive"
    )
    linuxvolume = tables.Column(
        linkify=True,
        verbose_name="linuxvolume"
    )
    allocation = tables.Column(
        linkify=True,
        verbose_name="allocation"
    )


class LinuxVolumeDriveTable(LinuxVolumeDriveBaseTable):
    """Table for displaying LinuxVolume objects."""

    pk = ToggleColumn()

    class Meta(NetBoxTable.Meta):
        model = LinuxVolumeDrive
        fields = (
            "pk",
            "drive",
            "linuxvolume",
            "allocation",
            "description",
        )
        default_columns = (
            "drive",
            "linuxvolume",
            "allocation",
            "description"
        )


class RelatedLinuxVolumeTable(LinuxVolumeDriveBaseTable):
    actions = ActionsColumn(actions=())

    class Meta(NetBoxTable.Meta):
        model = LinuxVolumeDrive
        fields = (
            "pk",
            "drive",
            "linuxvolume",
            "allocation",
            "description",
        )
        default_columns = (
            "drive",
            "linuxvolume",
            "allocation",
            "description"
        )

