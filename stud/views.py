from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'./myapp/index.html')


def about(request):
    return render(request,'./myapp/about.html')


from .models import user_login

def admin_login(request):
      if request.method == 'POST':
        uname=request.POST.get('uname')
        password = request.POST.get('password')
        # select query
        user_list = user_login.objects.filter(uname=uname, password=password, utype='admin')

        if len(user_list) == 1:
            #setting session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            context = {'uname': user_list[0].uname.upper()}
            return render(request,'./myapp/admin_home.html',context)
        else:
            context = {'msg':'Invalid Credentials'}
            return render(request,'./myapp/admin_login.html',context)
      else:
        return render(request,'./myapp/admin_login.html')


def admin_home(request):
    context = {'uname': 'admin'}
    return render(request,'./myapp/admin_home.html')


def admin_change(request):
    if request.method == 'POST':
        opassword = request.POST.get('opassword')
        npassword = request.POST.get('npassword')
        try:

            uname = request.session['user_name']
        except:
            return render(request, './myapp/admin_login.html')

        try:
            user1 = user_login.objects.get(uname=uname, password=opassword, utype='admin')
            # update query
            user1.password = npassword
            user1.save()
            context = {'msg':'password change'}
            return render(request, './myapp/admin_change.html',context)
        except user_login.DoesNotExist:
            context = {'msg':'invalid password'}
            return render(request, './myapp/admin_change.html',context)
    else:
        return render(request,'./myapp/admin_change.html')


def admin_logout(request):
    try:

        del request.session['user_name']
        del request.session['user_id']
        return admin_login(request)
    except:
        return admin_login(request)

from .models import user

def admin_users_view(request):
    user_list = user.objects.all()
    context = {'user_list':user_list}
    return render(request,'./myapp/admin_users_view.html',context)


####user##
def user_reg(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        rollno = request.POST.get('rollno')
        course = request.POST.get('course')
        utype = 'user'

    ####insert query
        user1 = user_login(uname=uname, password=password, utype=utype)
        user1.save()
        user1 = user(uname=uname,rollno=rollno,course=course)
        user1.save()
        context = {'msg':'user registered'}
        return render(request,'./myapp/user_reg.html',context)
    else:
        return render(request,'./myapp/user_reg.html')


def user_validation(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        # select query
        user_list = user_login.objects.filter(uname=uname, password=password, utype='user')

        if len(user_list) == 1:
            # setting session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            context = {'uname': user_list[0].uname.upper()}
            return render(request, './myapp/user_home.html')
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, './myapp/user_login.html', context)
    else:
        return render(request, './myapp/user_login.html')


def user_home(request):
    try:
        uname = request.session['user_name']
        context = {'uname': 'uname'}

        return render(request, './myapp/user_home.html')
    except:
        return render(request, './myapp/user_login.html')


def user_change(request):
    if request.method == 'POST':
        opassword = request.POST.get('opassword')
        npassword = request.POST.get('npassword')
        try:

            uname = request.session['user_name']
        except:
            return render(request, './myapp/user_login.html')

        try:
            user1 = user_login.objects.get(uname=uname, password=opassword, utype='user')
            # update query
            user1.password = npassword
            user1.save()
            context = {'msg':'password change'}
            return render(request, './myapp/user_change.html',context)
        except user_login.DoesNotExist:
            context = {'msg':'invalid password'}
            return render(request, './myapp/user_change.html',context)
    else:
        return render(request,'./myapp/user_change.html')


def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
        return user_validation(request)
    except:
        return user_validation(request)




from .models import student_details

def admin_add(request):
    if request.method == "POST":
        sname =request.POST.get('sname')
        subject = request.POST.get('subject')
        course = request.POST.get('course')
        user_list = student_details(sname=sname,subject=subject,course=course)
        user_list.save()
        context={'msg':'Subject Added Successfully'}
        return render(request,'./myapp/admin_add.html',context)
    else:
        return render(request,'./myapp/admin_add.html')


def admin_studdetails_view(request):
    stud_list = student_details.objects.all()
    context = {'stud_list': stud_list}
    return render(request, './myapp/admin_studdetails_view.html', context)


def admin_delete_stud(request):
    id = request.GET.get('id')
    stud_del = student_details.objects.get(id=int(id))
    stud_del.delete()
    stud_list = student_details.objects.all()
    context = {'uname': 'admin'.upper(), 'user_list': stud_list, 'msg': 'One Deleted'}
    return render(request, './myapp/admin_studdetails_view.html', context)



def user_home(request):
    try:
        uname = request.session['uname']
        context = {'uname':uname}
        return render(request,'./myapp/user_home.html',context)
    except:
        return render(request, './myapp/user_login.html')

