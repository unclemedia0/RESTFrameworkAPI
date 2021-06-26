
from rest_framework import serializers
from .models import *

class AllTaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = AllTask
		fields = ('id','task_name','task_detail')