from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_storage.models import LinuxVolume


class LinuxVolumeDriveFilter(NetBoxModelFilterSet):
    """Filter capabilities for LinuxVolume instances."""

    class Meta:
        model = LinuxVolume
        fields = [
            "drive",
            "linuxvolume",
            "allocation",
            "description",
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(allocation__icontains=value)
        )
        return queryset.filter(qs_filter)
