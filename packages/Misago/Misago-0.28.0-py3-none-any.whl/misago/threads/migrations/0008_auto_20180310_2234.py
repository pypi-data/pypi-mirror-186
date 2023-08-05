# Generated by Django 1.11.9 on 2018-03-10 22:34
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("misago_threads", "0007_auto_20171008_0131"),
    ]

    operations = [
        migrations.AddField(
            model_name="thread",
            name="best_answer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="misago_threads.Post",
            ),
        ),
        migrations.AddField(
            model_name="thread",
            name="best_answer_is_protected",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="thread",
            name="best_answer_marked_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="marked_best_answer_set",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="thread",
            name="best_answer_marked_by_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="thread",
            name="best_answer_marked_by_slug",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="thread",
            name="best_answer_marked_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
