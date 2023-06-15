from django.contrib import messages
from django.shortcuts import render ,redirect ,get_object_or_404
from.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,authenticate
from foodmenu.models import Food

def signin(request):
    if request.method == 'POST' and 'signup' in request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not username:
            messages.error(request, 'Error in First Name !')
        elif not email:
            messages.error(request, 'Error in Email !')
        elif not password:
            messages.error(request, 'Error in password !')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'This Username is taken!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This Email is already registered!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Your account has been created successfully!')
            return render(request, 'registration/signin.html')
    elif request.method == 'POST' and 'signin' in request.POST:
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Go to'+email+'to active your account !')
                return redirect('/accounts/signin')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('/accounts/signin')
    return render(request, 'registration/signin.html')


def log_out(request):
    context ={'log_out' : log_out}
    return render(request, 'registration/log_out.html',context)

@login_required(login_url='/accounts/login/')
def product_favorites(request,slug):
    product_fav=Food.objects.get(slug=slug)
    if Profile.objects.filter(user=request.user,productfavorites=product_fav).exists():
        messages.error(request,'Product in favorite already')
        return redirect('/' + str(slug))
    else:
        userprofile=Profile.objects.get(user=request.user)
        userprofile.productfavorites.add(product_fav)
        messages.success(request,'Product has been favorite')
        return redirect('/' + str(slug))

@login_required(login_url='/accounts/login/')
def showproduct_favorites(request):
    userinfo=Profile.objects.get(user=request.user)
    product_list=userinfo.productfavorites.all()
    context={'product_list': product_list }
    return render(request,'favorite.html',context)