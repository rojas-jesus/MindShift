# Generated by Django 4.2.6 on 2024-03-13 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_actiondate_emotion_actiondate_emotion_intensity_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Environment",
            fields=[
                (
                    "facilitator_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.facilitator",
                    ),
                ),
            ],
            bases=("core.facilitator",),
        ),
        migrations.AddField(
            model_name="action",
            name="environment_facilitator",
            field=models.ManyToManyField(
                blank=True,
                related_name="facilitator_environment",
                to="core.environment",
            ),
        ),
    ]