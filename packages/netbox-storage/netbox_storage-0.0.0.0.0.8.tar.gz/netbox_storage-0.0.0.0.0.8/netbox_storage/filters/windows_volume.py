from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_storage.models import WindowsVolume


class WindowsVolumeFilter(NetBoxModelFilterSet):
    """Filter capabilities for WindowsVolume instances."""

    class Meta:
        model = WindowsVolume
        fields = [
            "drive_name",
            "filesystem",
            "description"
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(drive_name__icontains=value)
            | Q(filesystem__icontains=value)
        )
        return queryset.filter(qs_filter)
