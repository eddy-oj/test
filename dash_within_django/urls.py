from django.urls import path, re_path
from . import views

from . import dash_app_base_generic # this loads the Dash app
from . import dash_layouts
from .dash_server import app, server


app_name = 'dash_within_django'

urlpatterns = [
                re_path('^_dash-', views.dash_ajax),

                path('home/', views.index, name='index'),
                path('skills/', views.skills, name='skills'),
                path('experience/', views.experience, name='experience'),
                path('education/', views.education, name='education'),
                path('ambitions/', views.ambitions, name='ambitions'),


                path('dashboard_example/', views.dashboard_example1, name='dashboard_example1'),
                path('dashboard_example2/', views.dashboard_example2, name='dashboard_example2'),

              ]
