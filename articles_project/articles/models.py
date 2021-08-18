from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=300)
	body = models.TextField()
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #if user is deleted it will set author fiedl empty
	creation_date = models.DateTimeField()

	class Meta:
		db_table = 'articles'
		ordering = ['-creation_date']

	def __str__(self):
		return self.title

	def get_url(self):
		return f'articles/{self.id}'