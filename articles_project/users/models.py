from werkzeug.security import generate_password_hash, check_password_hash

from django.db import models

class User(models.Model):
	name = models.CharField('User name', max_length=255)
	email = models.EmailField('Email')
	password = models.CharField('Password', max_length=255)

	class Meta:
		db_table = 'users'

	def __str__(self):
		return f'{self.__class__.__name__}(name={self.name})'

	def set_password(password):
		return generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)
