from django.urls import include, path
from django.urls import path
from . import views

urlpatterns = [
    path('best/region', views.best_region, name='best_region'),
    path('recommend/type', views.recommend_by_type, name='recommend_by_type'),
    path('recommend/type/<int:number>', views.recommend_by_type_one, name='recommend_by_type_one'),
    path('recommend/age', views.recommend_by_age, name='recommend_by_age'),
]