from django.db import models
from datetime import datetime

# Create your models here.

class Data(models.Model):
    MONTH_CHOICES = [
        ("", "-- Select Option --"),
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"),
        ("May", "May"),
        ("June", "June"),
        ("July", "July"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November", "November"),
        ("December", "December"),
    ]

    NEW_RENEW_CHOICES = [
        ("", "-- Select Option --"),
        ("New", "New"),
        ("Renew", "Renew")
    ]

    CATEGORY_CHOICES = [
        ("", "-- Select Option --"),
        ("Satisfactory", "Satisfactory"),
        ("Poor", "Poor")
    ]

    year_of_investment = models.IntegerField()
    name_of_doctor = models.CharField(max_length=255)
    tm_name = models.CharField(max_length=255)
    hq_name = models.CharField(max_length=255)
    month_of_investment = models.CharField(max_length=20, choices=MONTH_CHOICES)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    new_renew = models.CharField(max_length=20, choices=NEW_RENEW_CHOICES)
    roi_of_last_year = models.DecimalField(max_digits=10, decimal_places=2)

    # Add the following fields to store ROI for each month
    january_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    february_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    march_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    april_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    may_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    june_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    july_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    august_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    september_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    october_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    november_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    december_roi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    total = models.DecimalField(max_digits=10, decimal_places=2)
    times_of_roi = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)