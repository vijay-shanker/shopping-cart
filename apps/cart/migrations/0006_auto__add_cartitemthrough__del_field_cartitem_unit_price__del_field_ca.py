# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CartItemThrough'
        db.create_table(u'cart_cartitemthrough', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cart.Cart'])),
            ('cartitem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cart.CartItem'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('unit_price', self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True)),
        ))
        db.send_create_signal(u'cart', ['CartItemThrough'])

        # Deleting field 'CartItem.unit_price'
        db.delete_column(u'cart_cartitem', 'unit_price')

        # Deleting field 'CartItem.quantity'
        db.delete_column(u'cart_cartitem', 'quantity')

        # Removing M2M table for field cartitems on 'Cart'
        db.delete_table(db.shorten_name(u'cart_cart_cartitems'))


    def backwards(self, orm):
        # Deleting model 'CartItemThrough'
        db.delete_table(u'cart_cartitemthrough')

        # Adding field 'CartItem.unit_price'
        db.add_column(u'cart_cartitem', 'unit_price',
                      self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True),
                      keep_default=False)

        # Adding field 'CartItem.quantity'
        db.add_column(u'cart_cartitem', 'quantity',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding M2M table for field cartitems on 'Cart'
        m2m_table_name = db.shorten_name(u'cart_cart_cartitems')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cart', models.ForeignKey(orm[u'cart.cart'], null=False)),
            ('cartitem', models.ForeignKey(orm[u'cart.cartitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cart_id', 'cartitem_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'cartitems': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['cart.CartItem']", 'null': 'True', 'through': u"orm['cart.CartItemThrough']", 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'customer_ip': ('django.db.models.fields.IPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'num_cartitem': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subtotal': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'cart.cartitem': {
            'Meta': {'object_name': 'CartItem', '_ormbases': [u'cart.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cart.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'cart.cartitemthrough': {
            'Meta': {'object_name': 'CartItemThrough'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cart.Cart']"}),
            'cartitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cart.CartItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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