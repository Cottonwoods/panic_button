from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render

from selenium import webdriver

def index(request):
  return render(request, 'panic/index.html')

def panic(request):
  options = webdriver.ChromeOptions()
  options.add_argument('--kiosk')

  driver = webdriver.Chrome(chrome_options=options)
  driver.get('http://dashboard.txssc.com')

  return HttpResponseRedirect(reverse('index'))
