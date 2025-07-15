from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie
from .models import Cast
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required(login_url='login')


def show_movies(request):
    movies = Movie.objects.all()
    return render(request,'posts/show_movie.html', {'movies': movies})


def login(request):
    if request.method== 'POST':
        username=request.POST.get('email')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'User does not exist')
            return render(request,'authentication/login.html')
        
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful')
            return redirect('show_movies')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request,'authentication/login.html')
           
       
    return render(request,'authentication/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('email')
        email=request.POST.get('email')
        password=request.POST.get('password') 

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return render(request,'authentication/register.html')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,                        
        )  
        user.set_password(password)
        user.save()
        messages.success(request, 'account created successfully')
        return redirect('login')

       
    return render(request,'authentication/register.html')





def show_details(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'posts/show_details.html', {'movie': movie})

def search_movie(request):
    if request.method == "POST":
        title = request.POST.get('title')
        movie = Movie.objects.filter(title__icontains=title).first()
        if movie:
            return render(request, 'posts/show_details.html', {'movie': movie})
    return render(request, 'posts/no_movie.html')



def add_movie(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_superuser:  # or use `user.is_staff`
        return HttpResponseForbidden("You are not authorized to add movies.")

    if request.method == "POST":
       title=request.POST.get('title')
       description=request.POST.get('description')
       release_date=request.POST.get('release_date')
       rating=request.POST.get('rating')
       poster1=request.FILES.get('poster1')
       poster2=request.FILES.get('poster2')
       cast_ids = request.POST.getlist('cast')


       movie = Movie.objects.create(
            user=request.user,
            title=title,
            description=description,
            release_date=release_date,
            rating=rating,
            poster1=poster1,
            poster2=poster2
        )
       movie.cast.set(cast_ids)
       movie.save()
       return redirect('show_movies')
    casts = Cast.objects.all()
    
    return render(request, 'forms/add_movie.html')


def delete_movie(request, id):
    if not request.user.is_superuser: 
        return HttpResponseForbidden("You are not authorized to delete movies.")
    
    Movie.objects.filter(id=id).delete()
    return redirect('show_movies')


def add_cast(request):
    if request.method == "POST":
        name = request.POST.get('name')
        character = request.POST.get('character')
        cast_image = request.FILES.get('cast_image')

        casts=Cast.objects.create(
            name=name,
            character=character,
            cast_image=cast_image
        )
        casts.save()
        return redirect('add_movie')

    return render(request, 'forms/add_cast.html')

