from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from ecomm_app.models import *
from django.contrib import messages


# Create your views here.
def landing_page(request):
    context = {

    }
    return render(request, 'landing.html')


def display_product(request, type):
    if type == "mens":
        request.session['type'] = 'M'
    elif type == "women":
        request.session['type'] = 'W'
    else:
        request.session['type'] = 'K'

    context = {
        'all_categories': Category.objects.all(),
        'all_prod': Product.objects.filter(shoe_type=request.session['type']),
    }
    return render(request, 'prod_display.html', context)

# Method to handle ajax request to filter products based on category .


def show_category(request, cat_id):
    if request.method == 'GET':
        category_with_id = Category.objects.filter(id=cat_id)
        if len(category_with_id) > 0:
            category_with_id = category_with_id[0]
            context = {
                'filtered_prod': Product.objects.filter(categories=category_with_id, shoe_type=request.session['type'])
            }
            return render(request, 'prod_partial.html', context)
    else:
        return redirect(f'/show_category/{cat_id}')

# Method to handle ajax request to display all products.


def show_all(request, all):
    if request.method == 'GET':
        all_prod = Product.objects.all().filter(
            shoe_type=request.session['type'])
        context = {
            'filtered_prod': all_prod
        }
        return render(request, 'prod_partial.html', context)


def show_item(request, type, id):
    if request.method == 'GET':
        prod_with_id = Product.objects.filter(id=id)
        if len(prod_with_id) > 0:
            prod_with_id = prod_with_id[0]
            context = {
                'one_prod': prod_with_id,
            }
            return render(request, 'prod_page.html', context)
    else:
        # Running into a loop. Need to make this work!!
        return redirect(f'/home/{type}/{id}')


def display_cart(request):
    return render(request, 'cart.html')


def add_to_cart(request, prod_id):
    if request.method == 'POST':
        if 'user_id' not in request.session:  # making sure only logged in users are able to see the cart
            # messages.error(request, "You need to register or log in if you already have an account!")
            return HttpResponse('fail!')

        prod_with_id = Product.objects.filter(id=prod_id)
        Cart.objects.create(
            user=request.session['user_id'],
            product=prod_with_id,
            quantity=request.POST['quantity']
        )
        context = {
            '' : 
        }
        #cart/quantity
    return render(request, '', context)
