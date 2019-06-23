from django.shortcuts import render,redirect
from .forms import BookForms,ModelBookForms,SearchForm
from .models import Book
# from django.utils import timezone

from django.contrib import messages

# Create your views here.

def form_view(request):
    msg=''
    if request.method =='POST':
        form = BookForms(request.POST)
        if form.is_valid():
            book = Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('pur_date'),
                author=form.cleaned_data.get('author')
            )
            book.save()
            msg = 'Book Added Successfully!!!'
        else:
            msg = form.errors
    else:
        form = BookForms()
    return render(request,'form.html',{"msg":msg,"forms":form})


def model_form(request):
    msg =''
    if request.method =='POST':
        form = ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Book Added Successfully!!!'
        else:
            msg = form.errors
    else:
        form = ModelBookForms()
    return render(request,'form.html',{"msg":msg,"forms":form})

def html_form(request):
    value =''
    if request.method=='POST':
        value = request.POST.get('name')
        print('name',value)
        return render(request,'values.html',{'value':value})
    else:
        return render(request,'design.html')


def booksearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data.get('q')
            # book = Book.objects.filter(name__contains=q,purchase_date__lte=timezone.now)
            book = Book.objects.filter(name__contains=q)
            # form = None
            return render(request,'showtables.html',{'book':book,'form':SearchForm()})
    else:
        form = SearchForm()
        book = Book.objects.all()
    return render(request,'showtables.html',{'book':book,'form':form})


def deletebook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted #'+str(id)+' Succcessfully!!')
    return redirect('/')

def editbook(request, id):
    book = Book.objects.get(id = id)
    if request.method == 'POST':
        form = ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Updated Successfully!!!')
            return redirect('/')
    else:
        form = ModelBookForms(instance=book)
    return render(request,'editbook.html',{'form':form})

