from django.http import HttpResponse
from django.template import Template, context
from django.template.loader import get_template
#import os

#pagina = 

def index(request):
	pagina = get_template('index.html')
	p2 = pagina.render()
	return HttpResponse(p2)

"""def login(request):
	pagina = get_template('index.html')
	p2 = pagina.render()
	return HttpResponse(p2)"""

#def test1 (request):
	#mypath = os.getcwd()
	#maindir = os.path.dirname(os.path.dirname(mypath))
	#indexdir = maindir + '\\SistemaWebElectivo5\\index.html'
	#os.chdir(indexdir)
	#os.getcwd()
	#return HttpResponse()