# Generated by Django 4.2.6 on 2023-11-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_alter_thought_advantages_alter_thought_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thought",
            name="emotion_intensity",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "No Intensity"),
                    ("low", "Low"),
                    ("medium", "Medium"),
                    ("high", "High"),
                    ("severe", "Severe"),
                ],
                max_length=20,
                null=True,
                verbose_name="Emotion Intensity",
            ),
        ),
    ]