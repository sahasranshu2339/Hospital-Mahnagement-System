from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def patient_register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        if User.objects.filter(username=username).exists():

            messages.error(request, 'Username already exists.')
            return redirect('patient_registration')


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create UserProfile with role
        UserProfile.objects.create(
            user=user,
            role=role
        )

        messages.success(request, 'Registration successful')
        return redirect('login')


    return render(request, 'register.html')

from Hospital_app.models import UserProfile

def patient_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.userprofile.role == "DOCTOR":
                return redirect('doctor_dashboard')

            elif user.userprofile.role == "PATIENT":
                return redirect('patient_dashboard')

            else:
                return redirect('index')

        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")

from django.contrib.auth import logout


def user_logout(request):
    logout(request)
    return redirect('login')




# dashboard_views
def patient_dashboard(request):
    return render(request, "patient_dashboard.html")


def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html")


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")





# doctersdashboard
from .models import Doctor


def patient_dashboard(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        "patient_dashboard.html",
        {"doctors": doctors}
    )




# Patient dashboard


from .models import Patient


def doctor_dashboard(request):

    patients = Patient.objects.all()

    return render(
        request,
        "doctor_dashboard.html",
        {"patients": patients}
    )