from django.shortcuts import render

#Create your views here

def index(request):
	context = {
	'title':'Blog',
	'heading':'Blog',
	'subheading':'Perpustakan Berbasis Islam',
	}
	return render(request, 'blog/index.html',context)