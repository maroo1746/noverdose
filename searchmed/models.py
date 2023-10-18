from django.db import models

class med_list(models.Model):
    compound_name = models.CharField(max_length=225)
    product_name = models.CharField(max_length=225)
    product_id = models.IntegerField()
    age_restriction = models.IntegerField(blank=True, null=True)
    age_restriction_type = models.CharField(max_length=225, blank=True)
    age_direction = models.CharField(max_length=225, blank=True)
    contraindicated_info = models.CharField(max_length=225, blank=True)
    contraindicated = models.ManyToManyField('self', blank=True, related_name="contradicated")
    

    def __str__(self):
        return self.product_name