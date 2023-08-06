from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import APIRootView

from netbox.api.viewsets import NetBoxModelViewSet

from netbox_storage.api.serializers import (
    DriveSerializer,
    FilesystemSerializer, LinuxVolumeSerializer, LinuxVolumeDriveSerializer,
)
from netbox_storage.filters import DriveFilter, FilesystemFilter, LinuxVolumeFilter, \
    LinuxVolumeDriveFilter
from netbox_storage.models import Drive, Filesystem, LinuxVolume, LinuxVolumeDrive


class NetboxStorageRootView(APIRootView):
    """
    NetboxDNS API root view
    """

    def get_view_name(self):
        return "NetboxStorage"


class DriveViewSet(NetBoxModelViewSet):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer
    filterset_class = DriveFilter

    @action(detail=True, methods=["get"])
    def drive(self, request, pk=None):
        drives = Drive.objects.filter(drive__id=pk)
        serializer = DriveSerializer(drives, many=True, context={"request": request})
        return Response(serializer.data)


class FilesystemViewSet(NetBoxModelViewSet):
    queryset = Filesystem.objects.all()
    serializer_class = FilesystemSerializer
    filterset_class = FilesystemFilter

    @action(detail=True, methods=["get"])
    def filesystem(self, request, pk=None):
        filesystem = Filesystem.objects.filter(filesystem__id=pk)
        serializer = FilesystemSerializer(filesystem, many=True, context={"request": request})
        return Response(serializer.data)


class LinuxVolumeViewSet(NetBoxModelViewSet):
    queryset = LinuxVolume.objects.all()
    serializer_class = LinuxVolumeSerializer
    filterset_class = LinuxVolumeFilter

    @action(detail=True, methods=["get"])
    def linuxvolume(self, request, pk=None):
        linuxvolume = LinuxVolume.objects.filter(linuxvolume__id=pk)
        serializer = LinuxVolumeSerializer(linuxvolume, many=True, context={"request": request})
        return Response(serializer.data)


class LinuxVolumeDriveViewSet(NetBoxModelViewSet):
    queryset = LinuxVolumeDrive.objects.all()
    serializer_class = LinuxVolumeDriveSerializer
    filterset_class = LinuxVolumeDriveFilter

    @action(detail=True, methods=["get"])
    def linuxvolumedrive(self, request, pk=None):
        linuxvolumedrive = LinuxVolumeDrive.objects.filter(linuxvolumedrive__id=pk)
        serializer = LinuxVolumeSerializer(linuxvolumedrive, many=True, context={"request": request})
        return Response(serializer.data)

