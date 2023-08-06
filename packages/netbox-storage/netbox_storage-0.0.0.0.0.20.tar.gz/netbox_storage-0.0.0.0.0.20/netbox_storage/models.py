from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search


class Drive(NetBoxModel):
    size = models.PositiveIntegerField(
        verbose_name="Size (GB)"
    )
    cluster = models.ForeignKey(
        to='virtualization.Cluster',
        on_delete=models.PROTECT,
        related_name='drive',
    )
    virtual_machine = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.CASCADE,
        related_name='drive',
    )
    identifier = models.CharField(
        max_length=255,
    )
    description = models.CharField(
        max_length=255,
        blank=True,
    )

    clone_fields = ["size", "cluster", "virtual_machine", "description"]

    prerequisite_models = (
        'virtualization.Cluster',
        'virtualization.VirtualMachine',
    )

    class Meta:
        ordering = ["size"]

    def __str__(self):
        return f"VM: {self.virtual_machine} {self.identifier} Size: {self.size} GB Storage Cluster: {self.cluster}"

    def get_absolute_url(self):
        return reverse("plugins:netbox_storage:drive", kwargs={"pk": self.pk})

    # this is not needed if small_image is created at set_image
    def save(self, *args, **kwargs):
        number_of_hard_drives = Drive.objects.filter(virtual_machine=self.virtual_machine).order_by("created").count()

        self.identifier = f"Festplatte {number_of_hard_drives + 1}"
        super(Drive, self).save(*args, **kwargs)


@register_search
class DriveIndex(SearchIndex):
    model = Drive
    fields = (
        ("size", 200),
    )


class Filesystem(NetBoxModel):
    filesystem = models.CharField(
        unique=True,
        max_length=255,
    )
    description = models.CharField(
        max_length=255,
        blank=True,
    )

    clone_fields = ["filesystem", "description"]

    def get_absolute_url(self):
        return reverse("plugins:netbox_storage:filesystem", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.filesystem}"

    class Meta:
        ordering = ("filesystem", "description")

# Produziert einen Fehler, weitere Untersuchungen notwendig
# @register_search
# class FilesystemIndex(SearchIndex):
#    model = Filesystem
#    fields = (
#        ("filesystem", 100)
#    )


class LinuxVolume(NetBoxModel):
    vg_name = models.CharField(
        max_length=255,
    )
    lv_name = models.CharField(
        max_length=255,
    )
    path = models.CharField(
        max_length=255,
    )
    fs = models.OneToOneField(
        Filesystem,
        on_delete=models.CASCADE,
        related_name="fs_linux",
        verbose_name="Filesystem",
    )
    description = models.CharField(
        max_length=255,
        blank=True,
    )

    clone_fields = [
            "vg_name",
            "lv_name",
            "path",
            "fs",
            "description",
        ]

    def get_absolute_url(self):
        return reverse("plugins:netbox_storage:linuxvolume", kwargs={"pk": self.pk})

    def __str__(self):
        return f"vg_{self.vg_name}-lv_{self.lv_name}"

    class Meta:
        ordering = ("vg_name", "lv_name", "path")


@register_search
class LinuxVolumeIndex(SearchIndex):
    model = LinuxVolume
    fields = (
        ("vg_name", 100),
        ("lv_name", 100),
        ("path", 100),
        ("fs", 100),
    )


class WindowsVolume(NetBoxModel):
    drive_name = models.CharField(
        max_length=255,
    )
    fs = models.ForeignKey(
        Filesystem,
        on_delete=models.CASCADE,
        related_name="fs_windows",
        verbose_name="Filesystem",
    )
    description = models.CharField(
        max_length=255,
        blank=True,
    )

    clone_fields = [
            "drive_name",
            "fs",
            "description",
        ]

    def get_absolute_url(self):
        return reverse("plugins:netbox_storage:linuxvolume", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Name: {self.drive_name} filesystem: {self.fs}"

    class Meta:
        ordering = ("drive_name", "fs")
