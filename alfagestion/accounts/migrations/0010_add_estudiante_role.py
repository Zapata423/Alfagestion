# Generated manually to add estudiante role

from django.db import migrations


def add_estudiante_role(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')
    Role.objects.get_or_create(
        name='estudiante',
        defaults={
            'description': 'Rol para estudiantes del sistema'
        }
    )


def remove_estudiante_role(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')
    Role.objects.filter(name='estudiante').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_add_docente_role'),
    ]

    operations = [
        migrations.RunPython(add_estudiante_role, remove_estudiante_role),
    ]
