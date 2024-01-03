from django.db import models

class City:
  name = models.CharField(max_length=50)
  slug = models.CharField(max_length=50, blank=True)

  class Meta:
    verbose_name_plural = 'Cities'

  def __str__(self) -> str:
    return self.name

  