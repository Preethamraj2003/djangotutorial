from django.shortcuts import render
from product.models import Product, Category, Brand
from django.http import HttpResponse, Http404
from django.template import loader
from django.http import Http404
from django.core.paginator import Paginator


def product_detail(request, pr_id):
    category = Category.objects.filter(id=pr_id).first()
    
    if not category:
        raise Http404('Category not found')

    products = Product.objects.filter(category_id=pr_id)
    
    paginator = Paginator(products, 3)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request, 'productinfo.html', {
        'category': category,
        'page_obj': page_obj,
    })


def product_index(request):
    product_list = Category.objects.all()
    template = loader.get_template("product.html")
    context = {
        "latest_question_list": product_list,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    leaf = Category.objects.get(name='cname6')
    cat_list = Category.objects.all()
    sub_categories=[]
    for cat in cat_list:
        if cat.id == leaf.parent_cat_id_id:
            sub_categories.append(cat.name)
            pass
    context = {
        'sub_categories': sub_categories,
    }
    return HttpResponse (sub_categories)
