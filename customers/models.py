from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="%(class)s_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="%(class)s_updated")

    class Meta:
        abstract = True


class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
