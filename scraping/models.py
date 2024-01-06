from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    salary = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    lang = models.ForeignKey('Language', on_delete=models.CASCADE)
    city = models.ForeignKey('city', on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Vacancies'
