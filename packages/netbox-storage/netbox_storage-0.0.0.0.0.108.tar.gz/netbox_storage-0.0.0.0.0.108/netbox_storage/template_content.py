from extras.plugins import PluginTemplateExtension

from netbox_storage.models import Drive, LinuxVolume
from netbox_storage.tables import RelatedDriveTable


class RelatedDrives(PluginTemplateExtension):
    model = "virtualization.virtualmachine"

    def full_width_page(self):
        obj = self.context.get("object")

        drives = Drive.objects.filter(
            virtual_machine=obj
        )
        drive_table = RelatedDriveTable(
            data=drives
        )
        volumes = LinuxVolume.objects.filter(
            virtual_machine=obj
        )
        exclude_drive_id = []
        for volume in volumes.all():
            for drive in volume.drives.all():
                exclude_drive_id.append(drive.id)
        unmapped_drives = Drive.objects.filter(
            virtual_machine=obj
        ).exclude(id__in=exclude_drive_id).order_by('identifier')

        all_volumes = LinuxVolume.objects.all()
        display_volume = []
        for volume in all_volumes:
            display_volume = volume.drives.all().intersection(drives)

        platform = obj.platform
        if platform is not None:
            if platform.name.lower().__contains__('windows'):
                return self.render(
                    "netbox_storage/volume/windowsvolume_box.html",
                    extra_context={
                        "volumes": volumes,
                        "unmapped_drives": unmapped_drives,
                        "type": type(obj.platform),
                        "display_volume": display_volume
                    },
                )
            elif platform.name.lower().__contains__('linux'):
                return self.render(
                    "netbox_storage/volume/linuxvolume_box.html",
                    extra_context={
                        "related_drives": drive_table,
                    },
                )
        else:
            return self.render(
                "netbox_storage/volume/unknown_os_box.html",
            )


template_extensions = [RelatedDrives]
