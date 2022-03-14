from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render(request,'index.html')
def developer_Dashboard(request):
    return render(request,'developer\developer_Dashboard.html')