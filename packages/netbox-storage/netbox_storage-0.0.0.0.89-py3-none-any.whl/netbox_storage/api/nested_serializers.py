from rest_framework import serializers

from netbox.api.serializers import WritableNestedSerializer
from netbox_storage.models import Filesystem, Drive, WindowsVolume


#
# Filesystem
#

class NestedFilesystemSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_storage-api:filesystem-detail"
    )

    class Meta:
        model = Filesystem
        fields = ["id", "url", "display", "filesystem"]


#
# WindowsVolume
#
class NestedWindowsVolumeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_storage-api:windowsvolume-detail"
    )

    class Meta:
        model = WindowsVolume
        fields = ["id", "url", "display", "drive_name"]


#
# Drive
#
class NestedDriveSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_storage-api:drive-detail"
    )

    class Meta:
        model = Drive
        fields = ["id", "url", "display", "size", "identifier"]
