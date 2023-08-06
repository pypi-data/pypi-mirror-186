from netbox.api.serializers import WritableNestedSerializer
from netbox_storage.models import Filesystem

__all__ = [
    'NestedFilesystemSerializer',
]


#
# Filesystem
#

class NestedFilesystemSerializer(WritableNestedSerializer):
    class Meta:
        model = Filesystem
        fields = ['id', 'filesystem']
