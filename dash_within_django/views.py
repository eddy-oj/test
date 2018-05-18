# Django related imports:
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author

# Dash related imports:
from .dash_server import dash_dispatcher, clean_dash_content
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print("Function: index()")
    return render(request, 'dash_within_django/index.html')

def skills(request):
    return render(request, 'dash_within_django/skills.html')

def experience(request):
    return render(request, 'dash_within_django/experience.html')

def education(request):
    return render(request, 'dash_within_django/education.html')

def ambitions(request):
    return render(request, 'dash_within_django/ambitions.html')

@csrf_exempt
def dash_ajax(request, **kwargs):
    print('Function: dash_ajax')
    return HttpResponse(dash_dispatcher(request,), content_type='application/json')

def dashboard_example1(request):

    # get the django context:
    # author = get_object_or_404(Author, pk=author_id)

    print("Function: dash_django_page(): Getting 'dash_content'")
    dash_content = HttpResponse(dash_dispatcher(request,), content_type='application/json').getvalue()
    # clean the dash html content (the content contains lots of unnecessary characters like '\n')
    dash_content = clean_dash_content(dash_content)
    print(dash_content)

    context = {'dash_content': dash_content}

    return render(request, 'dash_within_django/dashboard_example1.html', context=context)


def dashboard_example2(request):

    print("Function: dash_django_page2(): Getting 'dash_content'")
    dash_content = HttpResponse(dash_dispatcher(request,), content_type='application/json').getvalue()
    # clean the dash html content (the content contains lots of unnecessary characters like '\n')
    dash_content = clean_dash_content(dash_content)
    print(dash_content)

    context = {'dash_content': dash_content}

    return render(request, 'dash_within_django/dashboard_example2.html', context=context)
