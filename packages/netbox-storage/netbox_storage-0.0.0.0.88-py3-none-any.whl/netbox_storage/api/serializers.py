from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from netbox_storage.api.nested_serializers import NestedFilesystemSerializer, NestedDriveSerializer, \
    NestedWindowsVolumeSerializer
from netbox_storage.models import Drive, Filesystem, LinuxVolume, WindowsVolume
from virtualization.api.nested_serializers import NestedClusterSerializer, NestedVirtualMachineSerializer


class FilesystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filesystem
        fields = (
            "id",
            "filesystem",
            "description",
            "created",
            "last_updated",
            "custom_fields",
        )


class DriveSerializer(NetBoxModelSerializer):
    cluster = NestedClusterSerializer(required=False, allow_null=True)
    virtual_machine = NestedVirtualMachineSerializer(required=False, allow_null=True)
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_storage-api:drive-detail")
    windowsvolumes = NestedWindowsVolumeSerializer(many=True, read_only=True, required=False, default=None,)

    class Meta:
        model = Drive
        fields = (
            "id",
            "url",
            "display",
            "size",
            "cluster",
            "virtual_machine",
            "identifier",
            "description",
            "windowsvolumes",
            "created",
            "last_updated",
            "custom_fields",
        )


class LinuxVolumeSerializer(serializers.ModelSerializer):
    fs = NestedFilesystemSerializer(required=False, allow_null=True)

    class Meta:
        model = LinuxVolume
        fields = (
            "id",
            "vg_name",
            "lv_name",
            "fs",
            "path",
            "description",
            "created",
            "last_updated",
            "custom_fields",
        )


class WindowsVolumeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_storage-api:windowsvolume-detail")
    fs = NestedFilesystemSerializer(required=False, allow_null=True)
    drives = NestedDriveSerializer(required=False, many=True, read_only=False)
    virtual_machine = NestedVirtualMachineSerializer(required=False, allow_null=True)

    class Meta:
        model = WindowsVolume
        fields = (
            "id",
            "url",
            "drive_name",
            "fs",
            "drives",
            "virtual_machine",
            "description",
            "created",
            "last_updated",
            "custom_fields",
        )

    def create(self, validated_data):
        drives = validated_data.pop("drives", None)

        windowsvolume = super().create(validated_data)

        if drives is not None:
            windowsvolume.drives.set(drives)

        return windowsvolume

    def update(self, instance, validated_data):
        drives = validated_data.pop("drives", None)

        windowsvolume = super().update(instance, validated_data)

        if drives is not None:
            windowsvolume.drives.set(drives)

        return windowsvolume