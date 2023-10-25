# Generated by Django 4.2.3 on 2023-10-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App01", "0003_webcamsnapshot_video_alter_webcamsnapshot_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="webcamsnapshot",
            name="video",
        ),
        migrations.AlterField(
            model_name="webcamsnapshot",
            name="image",
            field=models.ImageField(upload_to="webcam_snapshots/"),
        ),
    ]
