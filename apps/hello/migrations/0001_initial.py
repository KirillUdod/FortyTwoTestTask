# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainInfo'
        db.create_table('hello_maininfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('other_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('hello', ['MainInfo'])

        # Adding model 'WebRequest'
        db.create_table('hello_webrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('hello', ['WebRequest'])


    def backwards(self, orm):
        # Deleting model 'MainInfo'
        db.delete_table('hello_maininfo')

        # Deleting model 'WebRequest'
        db.delete_table('hello_webrequest')


    models = {
        'hello.maininfo': {
            'Meta': {'object_name': 'MainInfo'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'hello.webrequest': {
            'Meta': {'object_name': 'WebRequest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['hello']