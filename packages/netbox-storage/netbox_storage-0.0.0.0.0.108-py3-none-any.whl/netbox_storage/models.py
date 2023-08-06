from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel


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

    clone_fields = ["size", "identifier", "cluster", "virtual_machine", "description"]

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

    def save(self, *args, **kwargs):
        is_already_implemented = Drive.objects.filter(id=self.pk).count()
        if is_already_implemented == 0:
            number_of_hard_drives = Drive.objects.filter(virtual_machine=self.virtual_machine).order_by("created")\
                .count()

            self.identifier = f"Hard Drive {number_of_hard_drives + 1}"

        super(Drive, self).save(*args, **kwargs)

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/drive/'


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
    fs = models.ForeignKey(
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

    prerequisite_models = (
        'dcim.platform'
    )

    def get_absolute_url(self):
        return reverse("plugins:netbox_storage:linuxvolume", kwargs={"pk": self.pk})

    def __str__(self):
        return f"vg_{self.vg_name}-lv_{self.lv_name}"

    class Meta:
        ordering = ("vg_name", "lv_name", "path")


class LinuxVolumeDrive(NetBoxModel):
    drive = models.ForeignKey(
        Drive,
        on_delete=models.CASCADE,
        related_name='drive',
    )
    linuxvolume = models.ForeignKey(
        LinuxVolume,
        on_delete=models.CASCADE,
        related_name='linuxvolume',
    )
    allocation = models.PositiveIntegerField(
        verbose_name="Allocation"
    )
    description = models.CharField(
        max_length=255,
        blank=True,
    )

    clone_fields = [
            "drive",
            "linuxvolume",
            "allocation",
            "description",
        ]

    def get_absolute_url(self):
        return reverse("plugins:netbox_storage:linuxvolumedrive", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.drive}-{self.linuxvolume}"

    class Meta:
        ordering = ("drive", "linuxvolume")
