# Generated manually to remove first_name column

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_name_fields'),
    ]

    operations = [
        migrations.RunSQL(
            sql='ALTER TABLE accounts_user DROP COLUMN IF EXISTS first_name;',
            reverse_sql='ALTER TABLE accounts_user ADD COLUMN first_name VARCHAR(30);',
        ),
    ]
