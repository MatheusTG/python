import urllib
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Deu certo: ')
else:
    print('Tudo Ok')
