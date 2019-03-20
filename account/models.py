from django.db import models
from django.conf import settings
from decimal import Decimal


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    virtual_asset = models.PositiveIntegerField(default=17)
    real_asset = models.DecimalField(default=Decimal(0), decimal_places=2, max_digits=13)

    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)