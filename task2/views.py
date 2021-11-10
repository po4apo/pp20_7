from django.shortcuts import render
from django.views.generic import CreateView, FormView





def show_employees(request):
    if request.method == 'GET':

        return render(request,template_name='index.html')
