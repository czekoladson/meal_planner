from django.shortcuts import render

from .models import Day
# Create your views here.

def index(request):
    return render(request, 'meal_plans_app/index.html')

def days(request):
    days = Day.objects.order_by('date_added')
    context = {'days': days}
    return render(request, 'meal_plans_app/days.html', context)

def day(request,day_id):
    day = Day.objects.get(id = day_id)
    entries = day.entry_set.order_by('-date_added')
    context = {'day': day, 'entries':entries}
    return render(request, 'meal_plans_app/day.html', context)