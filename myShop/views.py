from django.shortcuts import render, get_object_or_404
from .models import Product


# LIST VIEW — список всех товаров
def product_list_view(request):
    products = Product.objects.select_related('serial_number').all()
    return render(request, 'myShop/product_list.html', {'products': products})


# DETAIL VIEW — подробная информация о товаре
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serial = getattr(product, 'serial_number', None)   # один к одному (может не быть)
    comments = product.comments.all()                   # один ко многим
    return render(request, 'myShop/product_detail.html', {
        'product': product,
        'serial': serial,
        'comments': comments,
    })
