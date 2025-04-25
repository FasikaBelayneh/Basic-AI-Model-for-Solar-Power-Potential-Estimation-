from django.db import models
import uuid
from django.contrib.gis.db import models as gis_models

class RegionalAverage(models.Model):
    location = gis_models.PointField()
    average_irradiance = models.FloatField()
    month = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class SolarIncentive(models.Model):
    country = models.CharField(max_length=2)
    region = models.CharField(max_length=100)
    incentives = models.JSONField()
    effective_from = models.DateField()
    effective_to = models.DateField()

class SolarReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = gis_models.PointField()
    month = models.IntegerField()