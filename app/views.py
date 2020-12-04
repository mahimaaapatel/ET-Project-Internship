from django.shortcuts import render
import app.models as models

def signIn(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        if models.CustomUser.objects.filter(email=email).exists():
            user = models.CustomUser.objects.get(email=email)
            request.session['email'] = email
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

def logout(request):
    try:
        del request.session['email']
    except:
      pass
    return render(request,"signIn.html")

def application(request):
    if request.method=='POST':
        cname = request.POST.get('cname')
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        if models.Company.objects.filter(name=cname).exists():
            models.Application.objects.create(company=models.Company.objects.get(name=cname), user=models.CustomUser.objects.get(email=request.session['email']),
            q1=q1, q2=q2, q3=q3)
    return render(request,"application.html")
