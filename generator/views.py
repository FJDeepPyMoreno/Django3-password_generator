from django.shortcuts import render
from django.http import HttpResponse
import random as rd

# Create your views here.
def home(request):
##    return HttpResponse('Hola qué te cuentas.')
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')
def password(request):

    characters = [chr(i) for i in range(ord('a'), ord('z')+1)]

    if request.GET.get('uppercase'):
        characters.extend([chr(i) for i in range(ord('A'), ord('Z')+1)])
        # Con esto añadimos la lista de mayúsculas a las minúsculas, 
        # generándose una lista nueva. 

    if request.GET.get('numbers'):
        characters.extend(list("0123456789"))
    
    if request.GET.get('special_caharacters'):
        characters.extend(list('@#%&_-*()'))

    # longitud = 10 , en realidad no queremos una longitud fija, sino
    # la determinada por nuestra elección en el website. Esta lonfitud
    # está referenciada en el documento 'home.html', dentro del bloque
    # <select name = length> . Entonces, usaremos 'render':
    longitud = int((request.GET.get('length', 12)))
    #'request.GET.get()' devuelve una cadena, pero como queremos que sea
    # un 'int', lo convertimos.
    # El segundo argumento, 12, es opcional, e indica el valor por defecto.

    thepassword = ''
    for x in range(longitud):
        thepassword += rd.choice(characters)

    return render(request,'generator/password.html', 
            {'passwordP' : thepassword})
    # this is passing the dictionary key and value to the template:
    # 'generator/password.html'.
    # Remember that 'render' is a Django method that allows communication
    # between the Python code and html files on the project.
