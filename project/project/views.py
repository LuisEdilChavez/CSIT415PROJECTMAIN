from django.shortcuts import render

def home_view(request):
    return render(request, "home_page.html")
 # Renders the Home.html template I think
def login_view(request):
    return render(request, "login_page.html")
#renders login page // 
def registration_view(request):
    return render(request, "registration_page.html")