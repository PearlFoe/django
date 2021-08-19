from django.db import models

from django.contrib.auth.models import User
'''
# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(null=True)
	creation_date = models.DateTimeField()

	class Meta:
		db_table = 'profiles'

	def __str__(self):
		return f'{self.user.username} profile'
'''


	