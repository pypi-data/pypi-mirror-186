# Generated by Django 1.10.5 on 2017-03-04 22:06
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("misago_users", "0007_auto_20170219_1639")]

    operations = [
        migrations.AddField(
            model_name="ban",
            name="registration_only",
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name="ban",
            name="check_type",
            field=models.PositiveIntegerField(
                choices=[(0, "Username"), (1, "E-mail address"), (2, "IP address")],
                db_index=True,
                default=0,
            ),
        ),
    ]
