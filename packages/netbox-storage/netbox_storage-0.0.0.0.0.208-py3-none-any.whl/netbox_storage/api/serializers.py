from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from netbox_storage.api.nested_serializers import NestedFilesystemSerializer, NestedDriveSerializer, \
    NestedLinuxVolumeSerializer
from netbox_storage.models import Drive, Filesystem, LinuxVolume
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


class LinuxVolumeDriveSerializer(serializers.ModelSerializer):
    drive = NestedDriveSerializer(required=False, allow_null=True)
    linuxvolume = NestedLinuxVolumeSerializer(required=False, allow_null=True)

    class Meta:
        model = LinuxVolume
        fields = (
            "id",
            "allocation",
            "drive",
            "linuxvolume",
            "description",
            "created",
            "last_updated",
            "custom_fields",
        )
