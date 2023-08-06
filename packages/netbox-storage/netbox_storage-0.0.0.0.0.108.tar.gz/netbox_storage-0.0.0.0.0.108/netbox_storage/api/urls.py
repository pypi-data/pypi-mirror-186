from netbox.api.routers import NetBoxRouter

from netbox_storage.api.views import (
    NetboxStorageRootView,
    DriveViewSet,
    FilesystemViewSet,
    LinuxVolumeViewSet,
    LinuxVolumeDriveViewSet,
)

router = NetBoxRouter()
router.APIRootView = NetboxStorageRootView

router.register("drive", DriveViewSet)
router.register("filesystem", FilesystemViewSet)
router.register("linuxvolume", LinuxVolumeViewSet)
router.register("linuxvolumedrive", LinuxVolumeDriveViewSet)

urlpatterns = router.urls
