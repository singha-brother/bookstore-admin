from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render, redirect 
import cloudinary

from .models import Book
from .forms import BookCreateForm, BookEditForm

class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

class BookListView(ListView):
    model = Book    
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    ordering = ['-time_posted']

class BookDetailView(DetailView):
    model = Book 
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book 
    template_name = 'books/book_edit.html'
    form_class = BookEditForm
    success_message = "စာအုပ်အချက်အလက် ပြင်ဆင်ပြီးပါပြီ။"

    def get_success_url(self):
        book = self.get_object()
        return reverse('book_detail', kwargs={"pk": book.pk})


class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Book 
    template_name = 'books/book_new.html'
    form_class = BookCreateForm
    success_url = reverse_lazy('book_list')
    success_message = "စာအုပ်အသစ်ထည့်ပြီးပါပြီ။"


class BookDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Book 
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")
    success_message = "စာအုပ်စာရင်းမှ ဖျက်ပြီးပါပြီ။"


