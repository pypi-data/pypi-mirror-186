from django.db import migrations, models
import utilities.json


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name="Drive",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("size", models.PositiveIntegerField()),
                ('cluster',
                 models.ForeignKey(on_delete=models.deletion.PROTECT, related_name='drive',
                                   to='virtualization.cluster')),
                ('virtual_machine',
                 models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE,
                                   related_name='drive', to='virtualization.virtualmachine')),
                ("identifier", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("size", "id"),
            },
        ),
        migrations.CreateModel(
            name="Filesystem",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("filesystem", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("filesystem", "id"),
            },
        ),
        migrations.CreateModel(
            name="LinuxVolume",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("vg_name", models.CharField(max_length=255)),
                ("lv_name", models.CharField(max_length=255)),
                ("path", models.CharField(max_length=255)),
                ('fs',
                 models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE, related_name='fs_linux',
                                   to='netbox_storage.filesystem')),
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("lv_name", "id"),
            },
        ),
        migrations.CreateModel(
            name="WindowsVolume",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("drive_name", models.CharField(max_length=255)),
                ("fs",
                 models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE, related_name='fs_windows',
                                   to='netbox_storage.filesystem')),
                (
                    "drives",
                    models.ManyToManyField(
                        blank=True, related_name="drives", to="netbox_storage.drive"
                    ),
                ),
                ('virtual_machine',
                 models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE,
                                   related_name='drive_volume', to='virtualization.virtualmachine')),
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("drive_name", "id"),
            },
        ),
    ]
