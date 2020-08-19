from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Product, Comment
from django.urls import reverse
from .forms import ProductForm
import datetime

def showcase(request):
    latest_product_list = Product.objects.order_by('-pub_date')
    return render(request, 'Shop/list.html', {'latest_product_list' : latest_product_list})

def detail(request, product_id):
    try:
        a = Product.objects.get(id = product_id )
    except:
        raise Http404("Товар не найден ^~^")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render (request, 'Shop/detail.html', {'product' : a, 'latest_comments_list' : latest_comments_list})

def leave_comment(request, product_id):
    try:
        a = Product.objects.get(id = product_id )
    except:
        raise Http404("Товар не найден ^~^")
    a.comment_set.create(
        author_name =  request.user.username,
        comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('shop:detail', args = (a.id,)))

#def leave_product(request):
#    try:
#        Product.objects.create(
#            product_title = request.POST['name'],
#            product_text = request.POST['text'],
#            product_image = request.FILES['image'],
#            product_image = request.POST['image'],
#            product_price = request.POST['price'],
#            pub_date = now
#            )
#    except:
#        pass
#    return render (request, 'Shop/leave.html')

def leave_product(request):
    try:
        form = ProductForm()
        form =ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if 'product_image' in request.FILES:
                form.product_image = request.FILES['product_image']
            form.save(commit=True)
            return HttpResponseRedirect('../')
        else:
            print(form.errors)
        return render(request, 'Shop/leave.html', {'form': form})
    except:
        raise Http404('Error')
# Create your views here.
