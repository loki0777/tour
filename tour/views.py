from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse



def landingPage(request):
	return render(request, 'tour/landingPage.html', {})