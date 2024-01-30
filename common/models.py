from django.db import models


# Create your models here.


class Member(models.Model):
    firs_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.firs_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Members"
        verbose_name = "Member"


class Prize(models.Model):
    money = models.IntegerField(default=2000)
    members_count = models.IntegerField(default=1000)
    min_age = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.money} {self.members_count}"

    class Meta:
        verbose_name_plural = "Prizes"
        verbose_name = "Prize"


