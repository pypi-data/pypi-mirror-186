import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
    ActionsColumn,
)

from netbox_storage.models import Filesystem


class FilesystemBaseTable(NetBoxTable):
    """Base class for tables displaying Filesystems"""

    filesystem = tables.Column(
        linkify=True,
    )


class FilesystemTable(FilesystemBaseTable):
    """Table for displaying Filesystem objects."""

    pk = ToggleColumn()

    class Meta(NetBoxTable.Meta):
        model = Filesystem
        fields = (
            "pk",
            "filesystem",
            "description",
        )
        default_columns = (
            "filesystem",
            "description"
        )


class RelatedFilesystemTable(FilesystemBaseTable):
    actions = ActionsColumn(actions=())

    class Meta(NetBoxTable.Meta):
        model = Filesystem
        fields = (
            "pk",
            "filesystem",
            "description",
        )
        default_columns = (
            "filesystem",
            "description"
        )
