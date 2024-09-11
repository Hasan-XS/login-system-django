from django.shortcuts import render, redirect

# from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import User


def register_system(request):
    context = {}
    if request.method == "POST":

        """Getting user information to register in this system"""
        username = request.POST.get("username", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        """In this section, we tried to save the new user in the database"""
        try:
            # password_hash = set_password(password)
            users = User(
                username=username,
                firstname=first_name,
                lastname=last_name,
                email=email,
                # password=password_hash,
            )

            # encrypt new user password
            users.set_password(password)

            # save new user in database
            users.save()
            context["result"] = "Register successful, Please Login!"
            return redirect("login_sys")

        except IntegrityError as ie:

            """
            In this section, I tried to take the entire error text and cut the
            main reason of the error text and show it to the user
            """
            IE_SYS = str(ie)  # getting error text

            """
            There is only one error in the original text. There was,
            then. It said how many times we have logged in and what is the
            main reason for the error, we were able to find it with the help of
            this line of code. Find and put in IE_SYS_index"""
            IE_SYS_index = IE_SYS.find(".")

            """
            In this section after finding . In the error text,
            with this line of code, we cut the original text such
            as email or user and put it in error_sys."""
            error_sys = IE_SYS[IE_SYS_index + 1 :]
            context["result"] = (
                f"Error: {error_sys} is already in the system, please choose another one."
            )
            return render(request, "login_system/register-sys.html", context)

    return render(request, "login_system/register-sys.html", context)


# login user
def login_sys(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(f"username: {username} and password: {password}")

        # user authentication
        user = authenticate(request, username=username, password=password)

        print(f"Authenticated User: {user.username}")

        if user is not None:
            # login user
            login(request, user)
            return redirect("welcome")
        else:
            context["result"] = "Invalid email or password"

    return render(request, "login_system/login.html", context)


# welcome view function
def welcome_view(request):
    return render(request, "welcome.html")
