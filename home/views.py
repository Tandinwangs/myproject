from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForms, ImageForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Session, User, Background, Equipments, Footer, Video

# Create your views here.
# Index page Views
def home(request):
    desob = Background.objects.all()
    equipob = Equipments.objects.all()
    footerob = Footer.objects.all()
    context = {'desob': desob, 'equipob': equipob, 'footerob': footerob}
    return render(request, 'home/index.html', context)


#User Views
def success(request):
    return render(request, 'home/success.html')

def userLogin(request):
    desob = Background.objects.all()
    equipob = Equipments.objects.all()
    footerob = Footer.objects.all()
    context = {'desob': desob, 'equipob': equipob, 'footerob': footerob}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('profile')
        
        else:            
            messages.error(request, 'Username OR password do not exist')
            return redirect('user-login')

    else:
        return render(request, 'home/untitled.html', context )


def userRegister(request):
    form = UserRegisterForms()
    desob = Background.objects.all()
    equipob = Equipments.objects.all()
    footerob = Footer.objects.all()
    context = {'form': form, 'desob': desob, 'equipob': equipob, 'footerob': footerob}


    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'home/untitled-1.html', context)

# def logoutUser(request):
#     logout(request)
#     return redirect('home')


def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login')  
def userProfile(request):
    objec = User.objects.all()
    context = {'objec': objec}
    return render(request, 'home/profile.html', context)

# @login_required(login_url='/login') 
# def userTable(request):
#     queues = Number.objects.all()
#     context = {'queues': queues}
#     return render(request, 'home/table.html', context)    

@login_required(login_url='/login') 
def userSession(request):
    obj = Session.objects.all()
    context = {'obj': obj}
    return render(request, 'home/session.html', context)    

@login_required(login_url='/login') 
def userUpdate(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Succesfully')
            return redirect('profile')

    context = {'form': form}
    return render(request, 'home/user_update.html', context) 

# @login_required(login_url='login')
# def deleteQueue(request, queue_id):
#     queue = Number.objects.get(pk=queue_id)

#     if request.user != queue.host:
#         return HttpResponse('You are not allowed here')

#     if request.method == 'POST':
#         queue.delete()
#         return redirect('profile')

#     return render(request, 'home/delete.html', {'obj':queue})

# @login_required(login_url='login')
# def generateQueue(request):
#     form = NumberForm()
#     obj = Number.objects.all()

#     if request.method == 'POST':
#         form = NumberForm(request.POST)

#         for ob in obj:
#             if ob.id >= 7:
#                 messages.error(request, "Full")
#                 # return HttpResponse('<h1 style="text-decoration: dotted; text-align: center; color: red;">No queue available</h1><a href="queueform.html">Back</a>')

#     if form.is_valid():
#         number = form.save(commit=False)
#         number.host = request.user
#         form.save()
#         return redirect('queue')

#     context = {'form': form, 'obj': obj}
#     return render(request, 'home/queueform.html', context)

@login_required(login_url='login')
def reserveSession(request):
    obj = Session.objects.all()
    session_count = obj.count()
    session_available = 20 - session_count
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
    

        if session_count == 20:
            messages.error(request, 'The reservation is no more available')
            return HttpResponseRedirect('/session/')
        

        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            form.save()
            return redirect('session')
    else:
        form = ImageForm()
    
    context = {'form': form, 'session_count': session_count, 'session_available': session_available}
    return render(request, 'home/sessionform.html', context)

@login_required(login_url='login')
def deleteSession(request, session_id):
    gym = Session.objects.get(pk=session_id)

    if request.user != gym.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        gym.delete()
        return redirect('session')

    return render(request, 'home/delete.html', {'obj':gym})

@login_required(login_url='/login') 
def video(request):
    
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'home/table.html', context)
