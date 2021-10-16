from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
	text = request.POST['text']
	tList = text.split(" ")
	numberOfWords = len(tList)
	return render(request, 'counter.html', {"words": numberOfWords})

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')