from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here. # this is an App / Module


# this is a function which takes request from user and send a response
# def january(request):
#     return HttpResponse("This works! Ha ha")

# def febraury(request):
#     return HttpResponse("This is a February page")

monthly_challenge_dic = {
    "january": "This works Ha Ha",
    "febrauy": "This is a Febraury page",
    "march": "I have to learn Django at leat 1h each day",
    "april": "I have to exercise myself in the driving app atleast 1 hour a day",
    "may": "This is the month of may",
    "june": "I love the sun during summer ",
    "jully": "this is a period of holiday",
    "August": " Its my birthday month",
    "september":"School resum",
    "october": "number 10h month",
    "november": "last but one moth of the year",
    "December": "christmas month"
    }

def index(request):
    list_items= ""
    months = list(monthly_challenge_dic.keys())

    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href= \"{month_path}\">{capitalize_month}</a><li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse (response_data)



def monthly_challenge_number(request, month):
    months_list = list(monthly_challenge_dic.keys()) # it returns all the item bzw months from the dic in oder

    if month > len(months_list):
        return HttpResponseNotFound("<h1>Invalid month<h1>")
    
    forward_month = months_list[month-1] # it gives out the index of the given month and select it directly in the dic
    redirect_path = reverse("month-challenges",args=[forward_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path) # just add the path to the specified month in the dic

    



def monthly_challenge(request,month):
    try:
        response_text = monthly_challenge_dic[month]
        response_datat = f"<h1>{response_text}<h1>"
    except:
        return HttpResponseNotFound("<h1>This month is not valid !<h1>")

    return HttpResponse(response_datat)