from django.db import models

# Create your models here.

GENDER = (("M", "MALE"), ("F", "FEMALE"))


class Screening(models.Model):
    verbal_consent = models.BooleanField(default=False)
    hospital_id = models.CharField(max_length=20)
    initials = models.CharField(max_length=3)
    gender = models.CharField(max_length=15, choices=GENDER)
    age = models.CharField(max_length=3)
    ethnicity = models.BooleanField()
    hiv = models.BooleanField(default=False)
    arv = models.BooleanField(default=False)
    treatment = models.BooleanField(default=False)
    live_in_catchment = models.BooleanField(default=False)
    remain_in_catchment = models.BooleanField()
    pregnant = models.BooleanField(default=False)
    informed_consent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hospital_id} {self.initials} {self.gender} {self.age}"
