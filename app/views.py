from django.shortcuts import render
from django.contrib.auth.models import User
from .filters import table_filter_form  # Assuming you have defined the filter form in a filters.py file

def list(request):
    table_data = User.objects.all()
    table_filter = table_filter_form(request.GET, queryset=table_data)
    return render(request, 'list.html', {"table_data": table_data, "table_filter": table_filter})
