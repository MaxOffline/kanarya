from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import AddCustomerForm, Login_Form,SearchForm, BuggyForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import newcustomer,Item, Cart
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from CusApp.forms import Register







class index(View):
    form = BuggyForm
    model = newcustomer.objects.all()
    template_name = "CusAppTemp/index.html"



    def get(self, request):

        form = self.form(None)
        return render(request, self.template_name,{ "customers":self.model, "form":form})

    def post(self,request):
        form = self.form(request.POST)
        findcart = Cart.objects.filter(user=request.user)
        if not findcart:
            createcart = Cart(user=request.user).save()
        if form.is_valid():
            form.save(commit=False)
            findlastcart = Cart.objects.filter(user=request.user).last()
            form.instance.cart = findlastcart.id
            form.instance.itemuser = request.user
            url = form.cleaned_data["url"]

            color = form.cleaned_data["color"]

            weight = form.cleaned_data["weight"]
            submitted = form.cleaned_data["submitted"]

            form.save()


            return redirect("CusApp:index")


class Submitted_View(View):
    template_name = "CusAppTemp/Summary.html"

    def post(self,request):
        finditems = Cart.objects.filter(user=request.user).last()
        findcart = Item.objects.filter(itemuser=request.user, cart= finditems.id)
        updateitem = Item.objects.filter(itemuser=request.user).update(submitted=True)
        createcart = Cart(user=request.user).save()
        return render(request,self.template_name,{"user":findcart})









class Cart_View(View):


    template_name = "CusAppTemp/Cart.html"

    def get(self,request):
        filtered_items = Item.objects.filter(itemuser=request.user, submitted=False)

        return render(request, self.template_name,{"cart":filtered_items})




class DeleteItem(DeleteView):

    model = Item
    success_url = reverse_lazy("CusApp:index")






class Customer_View(generic.DetailView):
    model = newcustomer

    template_name = "CusAppTemp/Customerinfo.html"


class Search_View(View):
    template_name = "CusAppTemp/search.html"
    form = SearchForm
    model = newcustomer.objects.all()


    def get(self, request):
        return render(request, self.template_name, {"search":self.form(None)})

    def post(self, request):

        form = self.form(request.POST)
        if form.is_valid():
            CustomerName=form.cleaned_data["Customer_Name"]
            try:
                Find_Customer = newcustomer.objects.get(Customer_Name__startswith=CustomerName)
            except:
                return render(request, self.template_name, {"error": "Customer not found!", "search": self.form(None)})
            else:
                Customer_Id = Find_Customer.id
                return render(request, self.template_name, {"id": Customer_Id,"name":CustomerName,"search":self.form(None)})


class AddCustomer(View):
    form = AddCustomerForm
    template_name = "CusAppTemp/CustomerAdd.html"

    def get(self,request):
        form = self.form(None)
        return render(request, self.template_name,{"form":form})

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():

            CustomerName = form.cleaned_data["Customer_Name"]
            Clothesprice = form.cleaned_data["Clothes_Price"]
            ClothesKilos = form.cleaned_data["Clothes_Kilos"]
            form.save()
            updateCustomer = newcustomer.objects.filter(Customer_Name= CustomerName).update(user=request.user)
            return redirect("index")

        return render(request, self.template_name,{"form":form})


class Login_View(View):
    form = Login_Form
    template_name = "CusAppTemp/login.html"
    def get(self,request):
        return render(request, self.template_name,{"form":self.form} )

    def post(self, request):
        form = self.form(request.POST)


        if form.is_valid():
            username = form.cleaned_data["username"]
            passcode = form.cleaned_data["password"]


            user = authenticate(username=username, password=passcode)
            if user is not None :
                if user.is_active:#and user.has_perm('CusApp.can_view')
                    login(request, user)
                    return redirect("CusApp:index")

        return render(request, self.template_name,{"form":self.form(request.POST),"error":"Username and/or password didn't match."})


class Logout_View(View):
    def get(self, request):
        logout(request)
        return redirect("CusApp:index")


class Sigup_View(View):

    model = Register

    allusers = User.objects.all()


    template_name = "CusAppTemp/signup.html"

    registered = "CusAppTemp/registered.html"


    def get(self, request):
        return render(request, self.template_name, {"form":self.model(None)})



    def post(self, request):
        form = self.model(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            for i in self.allusers:
                if i.email == email or i.username == username:
                    return render(request, self.registered,{"registered":"User is already registered","form":self.model(None)})

            else:
                user.set_password(password)
                user.save()
                login(request,user)
                return redirect("CusApp:index")
        else:
            return render(request, self.template_name,{"registered":"x","form":self.model(None)})
