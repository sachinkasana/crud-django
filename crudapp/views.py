from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm,AuthorForm

# Create your views here.
def bookList(request):  
    books = Book.objects.all()  
    return render(request,"book-list.html",{'books':books})  

def bookCreate(request):  
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('book-list')  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'book-create.html',{'form':form})  

def bookUpdate(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm(initial={'title': book.title, 'description': book.description, 'author': book.author, 'year': book.year})
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/book-list')  
            except Exception as e: 
                pass    
    return render(request,'book-update.html',{'form':form})  

def bookDelete(request, id):
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book-list')

def createAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Replace 'author-list' with your URL name for author list
    else:
        form = AuthorForm()
    return render(request, 'author-create.html', {'form': form})