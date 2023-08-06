from extras.plugins import PluginTemplateExtension

from netbox_storage.models import Drive
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

        if obj.platform.__contains__('Windows'):
            return self.render(
                "netbox_storage/volume/windowsvolume_box.html",
                extra_context={
                    "related_drives": drive_table,
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
