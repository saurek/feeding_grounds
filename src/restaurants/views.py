from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home(request):
    html_var = 'Tanks'
    html_ = f"""<!DOCTYPE html>
    <html lang=en>

    <head>
    </head>
    <body>
    <h1>Hail Satan!</h1>
    <p>{html_var} are coming through</p>
    </body>
    </html>
    """
    #f strings
    return HttpResponse(html_)
    #return render(request, "home.html", {})#response