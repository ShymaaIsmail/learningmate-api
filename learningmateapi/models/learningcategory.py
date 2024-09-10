# This class definition is incomplete and lacks attributes and methods.
from django.db import models


class LearningCategory(models.Model):
    class Meta:
        db_table = 'learning_categories'
    name = models.CharField(max_length=100)