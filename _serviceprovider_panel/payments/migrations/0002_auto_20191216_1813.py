# Generated by Django 2.2.1 on 2019-12-16 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0002_auto_20191216_1813'),
        ('uaccounts', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetail',
            name='serv_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sp_pay', to='uaccounts.RegisteredUser'),
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='subscription_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='splan_pay', to='offer.SubscriptionPlan'),
        ),
    ]
