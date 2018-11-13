from django.shortcuts import render

def index(request):
	context = {
		'title':'Perpustakaan Berbasis Islam',
		'heading':'Selamat Datang',
		'subheading':'In Yayang Library',
	}
	return render(request,'index.html',context)