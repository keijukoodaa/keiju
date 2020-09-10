from django.http import HttpRespose
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
	return "<h1>Hello Wordl</h1>" # string of HTML code
