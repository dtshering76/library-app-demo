from django.shortcuts import render
from .models import Book,BookInstance
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.   
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()
    
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail
    }
    
    return render(request,'catalog/index.html',context=context)

class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    fields = "__all__"

class BookDetailView(DetailView):
    model = Book

@login_required
def mysite(request):
    return render(request,'catalog/mysite.html')

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "catalog/signup.html"
    success_url = reverse_lazy('login')

class BookInstanceView(ListView,LoginRequiredMixin):
    model = BookInstance
    template_name = "catalog/book_list.html"
    context_object_name = "books"
    paginate_by = 5
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).all()