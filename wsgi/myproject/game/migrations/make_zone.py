from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.PositiveSmallIntegerField(default=0)),
                ('column', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField(default=1)),
                ('realm', models.ForeignKey(to='game.Realm')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
