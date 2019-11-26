from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    test1 = models.IntegerField(blank=True, null=True,)
    redirect = models.ForeignKey(
        "home.HomePage",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_redirect",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
