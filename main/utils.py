from django.shortcuts import redirect

def custom_http404():
	return redirect('main:404')