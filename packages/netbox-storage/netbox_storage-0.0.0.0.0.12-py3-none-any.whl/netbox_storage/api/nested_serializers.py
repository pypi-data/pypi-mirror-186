from rest_framework import serializers

from netbox.api.serializers import WritableNestedSerializer
from netbox_storage.models import Filesystem


#
# Filesystem
#

class NestedFilesystemSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dns-api:view-detail"
    )

    class Meta:
        model = Filesystem
        fields = ['id', 'filesystem']

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_dns-api:view-detail"
    )

    class Meta:
        model = View
        fields = ["id", "url", "display", "name"]