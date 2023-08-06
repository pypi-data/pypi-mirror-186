from rest_framework import serializers

from netbox.api.fields import SerializedPKRelatedField
from netbox_storage.api.nested_serializers import NestedFilesystemSerializer, NestedDriveSerializer
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


class DriveSerializer(serializers.ModelSerializer):
    cluster = NestedClusterSerializer(required=False, allow_null=True)
    virtual_machine = NestedVirtualMachineSerializer(required=False, allow_null=True)

    class Meta:
        model = Drive
        fields = (
            "id",
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


class WindowsVolumeSerializer(serializers.ModelSerializer):
    fs = NestedFilesystemSerializer(required=False, allow_null=True)
    drives = SerializedPKRelatedField(
        queryset=Drive.objects.all(),
        serializer=NestedDriveSerializer,
        required=False,
        many=True
    )
    # drives = NestedDriveSerializer(required=False, allow_null=True)
    virtual_machine = NestedVirtualMachineSerializer(required=False, allow_null=True)

    class Meta:
        model = WindowsVolume
        fields = (
            "id",
            "drive_name",
            "fs",
            "drives",
            "virtual_machine",
            "description",
            "created",
            "last_updated",
            "custom_fields",
        )
