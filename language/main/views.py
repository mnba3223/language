from django.shortcuts import render
import datetime

def main(request):
    context = {'message':'Django 很棒',"time":datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')}
    return render(request, 'main/main.html', context)