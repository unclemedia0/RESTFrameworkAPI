from django.shortcuts import render
from .models import *
from .serializers import AllTaskSerializer
from django.http import JsonResponse

##########django rest framework###########
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET']) #ฟังชั่นนี้อนุญาตสำหรับ GET เท่านั้น
def api_get_alltask(request):
	alltask = AllTask.objects.all().order_by('id').reverse() #ดึงข้อมูลทั้งหมดของ task
	serializer = AllTaskSerializer(alltask,many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET']) #ฟังชั่นนี้อนุญาตสำหรับ GET เท่านั้น
def api_get_alltask_id(request, pk):
	# ค้นหาด้วยรหัส id , pk = primary key
	try:
		task = AllTask.objects.get(id=pk) #ดึงข้อมูลทั้งหมดของ task
		serializer = AllTaskSerializer(task)
		return Response(serializer.data, status=status.HTTP_200_OK)
	except AllTask.DoesNotExist:
		error = {'status':'pk does not exist','message':'contact us: 080 123 4567'}
		return Response(status=status.HTTP_404_NOT_FOUND, data=error)


@api_view(['POST'])
def api_post_alltask(request):
	if request.method == 'POST':
		serializer = AllTaskSerializer(data=request.data)
		print('Data:',request.data)

		if serializer.is_valid():
			serializer.save() #ข้อมูลจะถูกบันทึกลงไปใน models
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

def post(self, request, format=None):
        self.http_method_names.append("GET")

        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
@api_view(['PUT'])
def api_put_alltask(request,pk):
	if request.method == 'PUT':
		edit = AllTask.objects.get(id=pk)
		serializer = AllTaskSerializer(edit,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete_alltask(request, pk):
	try:
		task = AllTask.objects.get(id=pk) #ดึงข้อมูลทั้งหมดของ task
		deleted = task.delete()
		data = {}

		if deleted:
			data['status'] = 'success'
		else:
			data['status'] = 'failed'
		return Response(data, status=status.HTTP_200_OK)
	except AllTask.DoesNotExist:
		error = {'status':'pk does not exist','message':'contact us: 080 123 4567'}
		return Response(status=status.HTTP_404_NOT_FOUND, data=error)




##########################################
def api_alltask(request):
	alltask = AllTask.objects.all() #ดึงข้อมูลทั้งหมดของ task
	serializer = AllTaskSerializer(alltask,many=True) # many=True คือ มีหลายข้อมูล (list)
	return JsonResponse(serializer.data, safe=False,json_dumps_params={'ensure_ascii': False})





