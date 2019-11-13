from django.shortcuts import render, redirect
from app.models import DogProduct, Purchase, DogTag
from datetime import datetime
from app.forms import NewDogTagForm
from django.contrib import messages

# Create your views here.
def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


def dog_product_detail(request, dog_product_id):
    dog_product = DogProduct.objects.get(id=dog_product_id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})


def purchase_dog_product(request, dog_product_id):
    dog_prod = DogProduct.objects.get(id=dog_product_id)
    if dog_prod.quantity >= 1:
        dog_prod.quantity -= 1
        dog_prod.save()
        purchase = Purchase.objects.create(
            dog_product=dog_prod, purchased_at=datetime.now()
        )
        messages.success(request, f"Purchased {dog_prod.name}")
        purchase.save()
        return redirect("purchase_detail", purchase.id)
    elif dog_prod.quantity < 1:
        messages.error(request, f"{dog_prod.name} is out of stock")
        return redirect("dog_product_detail", dog_prod.id)


def purchase_detail(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    return render(request, "purchase_detail.html", {"purchase": purchase})


def new_dog_tag(request):
    dog_tag = DogTag.objects.all()
    form = NewDogTagForm(request.POST)
    if request.method == "GET":
        return render(request, "new_dog_tag.html", {"dog_tag": dog_tag})
    elif request.method == "POST":
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            dog_name = form.cleaned_data["dog_name"]
            dog_birthday = form.cleaned_data["dog_birthday"]
            new_dog_tag = DogTag.objects.create(
                owner_name=owner_name, dog_name=dog_name, dog_birthday=dog_birthday
            )
            return redirect("dog_tag_list")
        elif not form.is_valid():
            return render(request, "new_dog_tag.html", {"form": form})


def dog_tag_list(request):
    dog_tags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags": dog_tags})

