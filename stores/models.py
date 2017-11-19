from django.contrib.postgres.fields import JSONField
from django.db import models
from uuid import uuid4
from users.models import User

class Store(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=250, null=False, blank=False)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	products = JSONField()

	def __str__(self):
		return self.name