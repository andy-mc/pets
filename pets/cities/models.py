from django.db import models

from common import utils


class State(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State)
    code = models.IntegerField()
    name = models.CharField(max_length=80)
    search_name = models.CharField(db_index=True, max_length=80)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.search_name = utils.clear_text(self.name).lower()
        super(City, self).save(*args, **kwargs)