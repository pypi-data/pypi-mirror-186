from extras.plugins import PluginTemplateExtension

from netbox_storage.models import Drive, WindowsVolume
from netbox_storage.tables import RelatedDriveTable
from dcim.models import Platform


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
        volumes = WindowsVolume.objects.filter(
            virtual_machine=obj
        )
        unmapped_drives = Drive.objects.filter(
            virtual_machine=obj
        ).exclude(id_in=volumes.values().drives.id)

        platform = obj.platform
        if platform.name.__contains__('Windows'):
            return self.render(
                "netbox_storage/volume/windowsvolume_box.html",
                extra_context={
                    "volumes": volumes,
                    "unmapped_drives": unmapped_drives
                },
            )
        else:
            return self.render(
                "netbox_storage/volume/linuxvolume_box.html",
                extra_context={
                    "related_drives": drive_table,
                },
            )


template_extensions = [RelatedDrives]
