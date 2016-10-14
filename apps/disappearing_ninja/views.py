from django.shortcuts import render, redirect
context = {}

# Create your views here.
def index(request):
	# if not 'path' in context:
		# context['path'] = 'disappearing_ninja/images/group.jpg'
	return render(request,'disappearing_ninja/index.html', context)

def ninja(request, ninjacolor="group"):
	if ninjacolor in ["group", "red", "blue", "purple", "orange"]:
		context['path'] = 'disappearing_ninja/images/{}.jpg'.format(ninjacolor)
	else:
		context['path'] = 'disappearing_ninja/images/{}.jpg'.format('april')
	return render(request, 'disappearing_ninja/ninja.html', context)