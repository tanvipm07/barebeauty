from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class IndexR(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('res')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/result{request.get_full_path()[1:]}')

def result(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    problem = request.session.get('problem','No')
    print('Problem: ',problem)
    categories = Category.get_all_categories()
    
    products = Products.get_products_by_problem(problem)

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'result.html', data)