from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

import socket
def index(request):
    return render(request, "index.html", {"info":""})

def generateFun(name):
    try:
        string = name
        address = ("0.0.0.0", 2222)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.send(bytes(string, "utf-8"))
        data_hook = s.recv(1024)
        s.close()
    except:
         data_hook=b''
    if data_hook==b'':
        data_hook=bytes("无|无|无|无|请联系管理员开启服务",'utf-8')
    return data_hook.decode("utf-8")



def generate(request, name):
    if request.is_ajax():
        response = generateFun(name)
        return HttpResponse(response)
    else :
        return render(request, "index.html", {"info":""})
