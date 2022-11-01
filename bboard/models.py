from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price:')
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name='Published on:')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')

    class Meta:
        verbose_name_plural = 'Descriptions'
        verbose_name = 'Description'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']