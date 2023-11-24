from django.db import models
from django.contrib.auth.models import User

class Med(models.Model):
    id = models.AutoField(primary_key=True)
    compound_name = models.CharField(max_length=225, blank=True, null=True)
    compound_code = models.CharField(max_length=225, blank=True, null=True)
    product_code = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=225, blank=True, null=True)
    company_name = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'med'


class Medcontraindication(models.Model):
    med_id_a = models.ForeignKey(Med, models.DO_NOTHING, db_column='med_id_a', blank=True, null=True)
    med_id_b = models.ForeignKey(Med, models.DO_NOTHING, db_column='med_id_b', related_name='medcontraindication_med_id_b_set', blank=True, null=True)
    contraindicated_info = models.CharField(max_length=225, blank=True, null=True)
    notification_no = models.CharField(max_length=50, blank=True, null=True)
    notification_date = models.DateField(blank=True, null=True)
    detail_info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medcontraindication'

class UserMedication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    med = models.ForeignKey(Med, on_delete=models.CASCADE)
