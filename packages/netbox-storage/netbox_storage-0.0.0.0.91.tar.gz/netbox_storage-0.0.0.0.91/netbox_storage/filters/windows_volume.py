import django_filters
from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_storage.models import WindowsVolume
from virtualization.models import VirtualMachine


class WindowsVolumeFilter(NetBoxModelFilterSet):
    """Filter capabilities for WindowsVolume instances."""
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        field_name='virtual_machine__name',
        queryset=VirtualMachine.objects.all(),
        to_field_name='name',
        label='Virtual machine (name)',
    )

    class Meta:
        model = WindowsVolume
        fields = [
            "drive_name",
            "fs",
            "drives",
            "virtual_machine",
            "description"
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(drive_name__icontains=value)
            | Q(fs__icontains=value)
        )
        return queryset.filter(qs_filter)
