from django.contrib.postgres.fields import JSONField
from django.core.mail import send_mail
from django.db import models
from uuid import uuid4
from users.models import User
from stores.models import Store


class Sale(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	buyer = models.ForeignKey(User, on_delete=models.CASCADE)
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	products = JSONField()
	status = models.CharField(max_length=10, default="PENDING")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified = models.DateTimeField(auto_now_add=False, auto_now=True)


	def set_approved(self):
		self.status = "ACCEPTED"
		return True

	def set_refused(self):
		self.status = "REFUSED"
		return True

	def send_email_notification(self, subject, message, recipients):
		send_mail(
    		subject,
    		message,
    		'notifications@labdii.com',
    		recipients,
    		fail_silently=False,
		)

	def __str__(self):
		return self.id.__str__()