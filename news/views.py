from django.shortcuts import (render, render_to_response)
from django.http import HttpResponse
import unirest
import urllib
import urllib2

# Create your views here.
def homepage(request):
    from xml.dom import minidom
    import urllib
    url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
    dom = minidom.parse(urllib.urlopen(url))
    itemlist = dom.getElementsByTagName('match')
    statelist = dom.getElementsByTagName('state')
    get_load = get_loadshedding()
    momlist = dom.getElementsByTagName('mom')
    kalimati_Info = kalimatiInfo(request)
    return render_to_response('news/index.html', {'itemlist': itemlist, 'statelist': statelist,
                                                          'momlist': momlist,'get_loadshedding':get_load,
                                                          'kalimati_Info':kalimati_Info,
                                                          })
def get_loadshedding():
	response = unirest.get("http://loadshedding.sparrowsms.com/?group=1");
	return response.body

def kalimatiInfo(request):
    params = urllib.urlencode({'cdate': '05/21/2014', 'pricetype': 'W'})
    response = urllib2.urlopen(kalimati_url(),params).read()
    response=response.replace('<center><table',"<table class='table  table-bordered'")
    return response

def kalimati_url():
    return 'http://kalimatimarket.com.np/priceinfo/dlypricebulletin'

def weather_present_location():
    response = unirest.get('http://api.worldweatheronline.com/free/v1/weather.ashx?q=Nepal&format=json&num_of_days=5&date=2014-05-26&key=rwj6dbhpzame5ka6mfyma2j9')
    

