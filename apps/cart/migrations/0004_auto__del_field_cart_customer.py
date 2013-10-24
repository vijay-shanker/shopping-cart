# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cart.customer'
        db.delete_column(u'cart_cart', 'customer_id')


    def backwards(self, orm):
        # Adding field 'Cart.customer'
        db.add_column(u'cart_cart', 'customer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'cart.base': {
            'Meta': {'object_name': 'Base'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cart.cart': {
            'Meta': {'object_name': 'Cart', '_ormbases': [u'cart.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cart.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'cart_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cartitems': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['cart.CartItem']", 'null': 'True', 'blank': 'True'}),
            'customer_ip': ('django.db.models.fields.IPAddressField', [], {'default': 'None', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'num_cartitem': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subtotal': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'cart.cartitem': {
            'Meta': {'object_name': 'CartItem', '_ormbases': [u'cart.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cart.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'unit_price': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cart']