from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView,ListView,UpdateView,CreateView,DeleteView
from .models import Book
from django.urls import reverse_lazy

# Create your views here.
# def hello(request):
#   context={
    
#   }
#   return render(request,'index.html',context=context)

class MyView(TemplateView):
  template_name='index.html'


  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    context['company_name']= 'Nepller Technology'
    return context
class MySecondView(TemplateView):
  template_name='index2.html'  
class MyRedirectView(RedirectView):
  permanent=False
  def get_redirect_url(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return '/mysecond'
    else:
      return '/'
    

class BookListView(ListView):
  model=Book
  template_name='book_list.html'
  context_object_name='books'
  ordering=['title']
  paginate_by=5
  
  def get_ordering(self):
    order=self.request.GET.get('order','title')
    return order
  
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['extra_info']='This is list view'
    return context

class BookUpdateView(UpdateView):
  model=Book
  fields=['title','author']
  template_name='book_update.html'
  success_url=reverse_lazy('book-list')
  
class BookCreateView(CreateView):
  model=Book
  fields=['title','author']
  template_name='book_form.html'
  success_url=reverse_lazy('book-list')

class BookDeleteView(DeleteView):
  model=Book
  template_name='book_confirm_delete.html'
  success_url=reverse_lazy('book-list')
