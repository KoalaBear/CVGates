from django.db import models

from accounts.models import CustomUser


class PlateNumber(models.Model):
    plate_number = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "platenumber"

    def __str__(self):
        return self.plate_number
