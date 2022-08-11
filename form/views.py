from django.shortcuts import render, redirect




# Create your views here.
def index(request):
    try:
        patha = request.path
        if "login_success" in patha:
            return render(request, 'exhibitors/form1.html')

        return redirect("https://100014.pythonanywhere.com/d_login")
    except:

        return redirect("https://100014.pythonanywhere.com/d_login")