from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def homepage(request):
    return render(request,'index.html')

def signup_page(request):
    return render(request,'signup.html')

def login_page(request):
    return render(request, 'login.html')



def check_username(request):
    if request.method == 'GET' and 'username' in request.GET:
        username = request.GET['username']
        user_exists = User.objects.filter(username=username).exists()
        return JsonResponse({'exists': user_exists})
    return JsonResponse({'error': 'Invalid request'})




"""def signup_view(request):
    if request.method == 'POST':
        # Process form data and retrieve user details
        fullname = request.POST.get('fullname')
        print(fullname)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Display user details (you can customize this as needed)
        return render(request, 'user_details.html', {'fullname': fullname, 'username': username, 'email': email})
    else:
        return render(request, 'signup.html')  # Render the signup form page"""


def signup_view(request):
    if request.method == 'POST':
        # Process form data and retrieve user details
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = fullname.split()[0]  # Assuming the first part of full name is first name
            user.last_name = ' '.join(fullname.split()[1:])  # Assuming the remaining part of full name is last name
            user.save()

            # Display success message
            #messages.success(request, 'Registration successful. You can now login.')
            
            # Redirect to the home page
            return render(request,'login.html',{'msg':'Registered Succesfully. You Can Login Now'})
        except IntegrityError:
            # Handle unique constraint violation (username already exists)
            print(request, 'Username already exists. Please choose a different username.')
            return render(request, 'signup.html', {'error_message': 'Username already exists. Please choose a different username.'})
    else:
        return render(request, 'signup.html')  # Render the signup form page

    



def login_view(request):
    if request.method == 'POST':
        # Process form data and retrieve user details
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            fname = user.first_name
            # Redirect to the dashboard or any other appropriate page
            return redirect('/dashboard')
        else:
            # Authentication failed, show error message or handle as needed
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # GET request, render the login form
        return render(request, 'login.html')
    
@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'fname':request.user.first_name})


@login_required
def meeting(request):
    return render(request,'meetingscreen.html',{'fullname':request.user.get_full_name()})

@login_required
def joinmeeting(request):
    if request.method == 'POST':
        roomID=request.POST['roomID']
        return redirect("/meeting?roomID="+roomID)

@login_required
def logout_view(request):
    # Log the user out
    logout(request)
    
    # Redirect to the homepage or any other appropriate page
    return redirect('/')
