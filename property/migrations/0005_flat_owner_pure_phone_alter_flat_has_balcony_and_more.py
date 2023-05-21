# Generated by Django 4.2.1 on 2023-05-21 02:43

from django.db import migrations
import phonenumber_field.modelfields
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    flat = apps.get_model('property', 'Flat')

    for obj in flat.objects.all():
        only_digits = ''.join(c for c in obj.owners_phonenumber if c.isdigit())
        parsed_number = phonenumbers.parse(only_digits, 'RU')
        if only_digits.startswith('8'):
            only_digits = '7' + only_digits[1:]
        if phonenumbers.is_valid_number(parsed_number):
            obj.owner_pure_phone = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230521_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Номер владельца'),
        ),
        migrations.RunPython(normalize_phone_numbers),
    ]
