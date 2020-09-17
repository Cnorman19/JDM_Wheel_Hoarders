from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
								  DetailView,
								  CreateView,
								  UpdateView,
								  DetailView,
								  DeleteView,)
from .models import Sell
from django.contrib import messages
from django.urls import reverse_lazy
from users.forms import NewSalePostForm

class SellListView(ListView):
	model = Sell
	template_name = 'sell/home.html'
	context_object_name = 'sells'
	ordering = ['-date_posted']


class SellDetailView(DetailView):
	model = Sell


class SellCreateView(LoginRequiredMixin, CreateView):
	model = Sell
	fields = ['name' , 'diameter' , 'width' , 'offset' , 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form) 

class SellUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Sell
	fields = ['name' ,  'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form) 

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True

		return False

class SellDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	
	model = Sell
	
	def get_success_url(self):

		return reverse_lazy('sell-home')
		
		



	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True

		return False
