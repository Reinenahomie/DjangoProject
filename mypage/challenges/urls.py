from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january), # if something is inputed as a request, it should trigger the january() function found in views
    # path("february", views.febraury),
    path("", views.index, name= "index"),
    path("<int:month>", views.monthly_challenge_number),
    path("<str:month>", views.monthly_challenge, name= "month-challenge") # name= "anny thing" can be used to contruct Urls pointing at that main url
    
]

