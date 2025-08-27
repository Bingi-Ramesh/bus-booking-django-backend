from django.db import migrations

def create_admin(apps, schema_editor):
    from django.contrib.auth.models import User
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),  # adjust based on your app’s last migration
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
