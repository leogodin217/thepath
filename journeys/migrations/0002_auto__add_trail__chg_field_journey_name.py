# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trail'
        db.create_table(u'journeys_trail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('journey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['journeys.Journey'])),
        ))
        db.send_create_signal(u'journeys', ['Trail'])


        # Changing field 'Journey.name'
        db.alter_column(u'journeys_journey', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Deleting model 'Trail'
        db.delete_table(u'journeys_trail')


        # Changing field 'Journey.name'
        db.alter_column(u'journeys_journey', 'name', self.gf('django.db.models.fields.CharField')(max_length='50'))

    models = {
        u'journeys.journey': {
            'Meta': {'object_name': 'Journey'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'journeys.trail': {
            'Meta': {'object_name': 'Trail'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['journeys.Journey']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['journeys']