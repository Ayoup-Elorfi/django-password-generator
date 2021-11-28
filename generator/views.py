from django.shortcuts import render
import random
# Create your views here.


def home_view(request):

    # for dropdown menu this will help user to select password length
    length = list(range(8, 31))
    context = {
        'length': length,
    }
    return render(request, 'generator/home.html', context)


def password_generator(request):

    # This list for characters used in the password
    chars_list = list('abcdefghijklmnopqrstuvwxyz')
    # here we take the length from the user input
    pass_lenght = int(request.GET.get('length'))
    generated_password = ''

    # here we check if the user select uppercase from the checkbox in the home view
    # if True we will add to the chars_list new items
    if request.GET.get('uppercase'):
        chars_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # here we check if the user select numbers from the checkbox in the home view
    # if True we will add to the chars_list new items
    if request.GET.get('numbers'):
        chars_list.extend(list('0123456789'))

    # here we check if the user select special characters from the checkbox in the home view
    # if True we will add to the chars_list new items
    if request.GET.get('special'):
        chars_list.extend(list('-*_+=#@$%^&*()?>!'))

    # here we loop based on the length requested from the user to add characters used in the password
    for i in range(pass_lenght):
        generated_password += random.choice(chars_list)

    context = {
        'generated_password': generated_password
    }
    return render(request, 'generator/password.html', context)


def about_view(request):
    return render(request, 'generator/about.html')
