from django.shortcuts import render
import app.models as models

def signIn(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        if models.CustomUser.objects.filter(email=email).exists():
            user = models.CustomUser.objects.get(email=email)
            cname = []
            stipend = []
            field = []
            duration = []
            location = []
            if user.password == request.POST.get('pass'):
                companies = models.Company.objects.filter().values()
                for i in range(len(companies)):
                    cname.append(companies[i]['name'])
                    stipend.append(companies[i]['stipend'])
                    duration.append(companies[i]['duration'])
                    field.append(companies[i]['field'])
                    location.append(companies[i]['location'])
                comblist = zip(cname, stipend, field, duration, location)
                return render(request, "home.html", {'comblist':comblist})
    return render(request,"signIn.html")
