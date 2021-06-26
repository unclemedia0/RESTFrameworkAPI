# testrequest.py
# pip install requests

import requests

def GetData():
	url = 'http://localhost:8000/api-task'
	r = requests.get(url=url)
	text_reponse = r.json() # r.text
	print(text_reponse, type(text_reponse))

def GetDataID(ID):
	url = 'http://localhost:8000/api/'+ID
	r = requests.get(url=url)
	text_reponse = r.json() # r.text
	print(text_reponse, type(text_reponse), r.status_code)


def PostData(data):
	url = 'http://localhost:8000/api-post'
	r = requests.post(url=url,data=data)
	text_reponse = r.json()
	if r.status_code == 201:
		print(text_reponse, type(text_reponse), r.status_code)
		print('บันทึกข้อมูลสำเร็จ')
	else:
		print('บันทึกข้อมูลไม่สำเร็จ')


def UpdateData(ID,data):
	url = 'http://localhost:8000/{}/api-edit'.format(ID)
	r = requests.put(url=url,data=data)
	text_reponse = r.json()
	if r.status_code == 201:
		print(text_reponse, type(text_reponse), r.status_code)
		print('แก้ไขข้อมูลสำเร็จ')
	else:
		print('แก้ไขข้อมูลไม่สำเร็จ')


def DeleteData(ID):
	url = 'http://localhost:8000/{}/delete'.format(ID)
	r = requests.delete(url=url,data=data)
	text_reponse = r.json()
	if r.status_code == 200:
		print(text_reponse, type(text_reponse), r.status_code)
		print('ลบข้อมูลสำเร็จ')
	else:
		print('ลบข้อมูลไม่สำเร็จ')

#GetData()
#GetDataID('1')
#data = {'task_name':'ปั่นจักรยานเสือภูเขา','task_detail':'เขาใหญ่'}
#PostData(data)
#UpdateData(6,data)
#DeleteData(6)

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('TEST REQUEST')
GUI.geometry('700x400')

L = ttk.Label(GUI,text='รายการ',font=('Angsana New',20)).pack()

v_taskname = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_taskname,font=('Angsana New',30))
E1.pack(pady=20)

L = ttk.Label(GUI,text='รายละเอียด',font=('Angsana New',20)).pack()

v_taskdetail = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_taskdetail,font=('Angsana New',30),width=50)
E2.pack(pady=20)

def SaveData():
	data = {'task_name':v_taskname.get(),'task_detail':v_taskdetail.get()}
	PostData(data)
	#clear data
	v_taskname.set('')
	v_taskdetail.set('')

B = ttk.Button(GUI,text='Save',command=SaveData)
B.pack(ipadx=20,ipady=10)

GUI.mainloop()