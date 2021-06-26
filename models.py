from django.db import models

# Create your models here.

class AllTask(models.Model):
	task_name = models.CharField(max_length=100)
	task_detail = models.TextField(null=True,blank=True)

	def __str__(self):
		return self.task_name
