from app1.views import ViewSerializer
from rest_framework import routers
from django.urls import include, path
from app1 import views


router = routers.DefaultRouter()
router.register('AllData', ViewSerializer, basename='AllData')

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='index'),
    path('itemForm', views.itemForm, name='itemForm'),
    path('deleteItems/<int:item_id>', views.deleteItems, name='deletes'),
    path('updateItems/<int:item_id>', views.updateItems, name='updates'),
    path('descriptionForm/', views.descForm, name='descform'),

    path('api/', include(router.urls)),
    path('aboutUs/', views.aboutUs, name='aboutUS'),
    path('contactUs/',views.contact, name='contact'),

    path('food/', views.food, name='food'),
    path('dairy/', views.dairy, name='dairy'),
    path('meat/', views.meat, name='meat'),
    path('vegetable/', views.vegetable, name='vegetable'),
    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kids/', views.kids, name='kids'),
]