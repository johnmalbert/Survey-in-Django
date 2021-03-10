from django.shortcuts import render, HttpResponse, redirect


context = []
def main(request):
    return render(request, "index.html")

def result(request):
    print(request.POST)

    context = {
    	"first_name" : request.POST['first_name'],
    	"last_name" : request.POST['last_name'],
        "student_id" : request.POST['student_id'],
        "how_you_heard" : request.POST['survey1'],
        "interest" :  request.POST['survey2'],
        "pay" : request.POST['survey3'],
        "comments" : request.POST['comments']
    }
    return render(request, "success.html", context)

def success(request):
    print(f"Printing from success {context}")
    return render(request, "success.html")