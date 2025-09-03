# Generated manually to add docente role

from django.db import migrations


def add_docente_role(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')
    Role.objects.get_or_create(
        name='docente',
        defaults={
            'description': 'Rol para docentes del sistema'
        }
    )


def remove_docente_role(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')
    Role.objects.filter(name='docente').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_boolean_fields'),
    ]

    operations = [
        migrations.RunPython(add_docente_role, remove_docente_role),
    ]
