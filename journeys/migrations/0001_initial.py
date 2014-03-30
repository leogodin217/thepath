# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Journey'
        db.create_table(u'journeys_journey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='50')),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'journeys', ['Journey'])


    def backwards(self, orm):
        # Deleting model 'Journey'
        db.delete_table(u'journeys_journey')


    models = {
        u'journeys.journey': {
            'Meta': {'object_name': 'Journey'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        }
    }

    complete_apps = ['journeys']