from django.db import models

# Create your models here.
class Usera(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
        (2, "other")
    )

    username = models.CharField(max_length=80)
    password = models.CharField(max_length=64, blank=True, null=True)
    gender = models.SmallIntegerField(choices=gender_choices, default=1,null=False)

    class Meta:
        db_table = "ba_user"
