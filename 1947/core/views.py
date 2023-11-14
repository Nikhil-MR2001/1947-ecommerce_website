from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):

    visit_count = request.COOKIES.get('visit_count', 0)   # to calculate visit count
    visit_count = int(visit_count) + 1

    total_products = Item.objects.count()   # to calculate total products

    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    response = render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'visit_count': visit_count,
        'total_products' : total_products,
    })

    response.set_cookie('visit_count', visit_count, max_age=86400)
    return response

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def category(request):
    category_name = request.GET.get('category_name')

    if category_name:
        items = Item.objects.filter(category__name=category_name)
    else:
        items = Item.objects.all()

    return render(request, 'core/formal.html', {
        'category_name': category_name,
        'items': items
    })