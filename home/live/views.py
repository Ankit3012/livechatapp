from django.shortcuts import render, HttpResponse, redirect
from .models import Userprofile,Messages,ticketprofile,openticket,closeticket,userlogin
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from rest_framework.parsers import JSONParser
from django.core import serializers
from django.db.models import Q
# Create your views here.
import pdb
import random
from uuid import getnode as get_mac
def index(request):

    mac = get_mac()

    try:
        iden = Userprofile.objects.get(uid=mac)
        username = Userprofile.objects.get(uid=111111).name
        name=Userprofile.objects.get(uid=mac).name

        ##
        messages = Messages.objects.filter(sender_name=iden, receiver_name=111111) | Messages.objects.filter(
            sender_name=111111, receiver_name=iden)
        message = []
        for i in messages:
            message.append(i)

        current = Userprofile.objects.filter(uid=mac)
        return render(request, 'chat.html', {'username': username,
                                             'name':name,
                                             'To': 111111,
                                             'messages': message,
                                             'current_user': iden,
                                             'current': current
                                             })
    except:
        if request.method == 'POST':
            if request.POST.get('name'):
                post = Userprofile()
                post.name = request.POST.get('name')
                post.uid = mac
                post.save()

                username=Userprofile.objects.get(uid=111111).name

                ##
                messages = Messages.objects.filter(sender_name=post.uid, receiver_name=111111) | Messages.objects.filter(
                    sender_name=111111, receiver_name=post.uid)
                message = []
                for i in messages:
                    message.append(i)
                # print(message)
                data = Userprofile.objects.all()
                current = Userprofile.objects.filter(uid=111111)
                print(type(current))
                return render(request,'chat.html',{'username':username,
                                                   'To':111111,
                                                   'messages': message,
                                                   'current_user':post.uid,
                                                   'current': current
                                                   })

        else:
            return render(request,'index.html')
def get(request,sender,receiver):
    if request.method == 'GET':
        print('get')
        messages = Messages.objects.filter(sender_name=sender, receiver_name=receiver) | Messages.objects.filter(
            sender_name=receiver, receiver_name=sender)


        message=serializers.serialize('json', messages)

        return JsonResponse({'messages':message},safe=False)
def login(request):
    if request.method == 'POST':
        if request.POST.get('uname'):
            name = request.POST.get('uname')
            uid=request.POST.get('psw')
            user=Userprofile.objects.get(name=name)
            id = Userprofile.objects.get(name=name).uid
            data=Userprofile.objects.all()

            current = Userprofile.objects.filter(uid=111111)
            if str(id) == str(123456):
                op=ticketprofile.objects.all()

                ocurrent = Userprofile.objects.filter(uid=123456)
                return render(request, 'openticket.html', {'username': user.name,
                                                     'To': id,
                                                     'current_user': id,
                                                     'current': ocurrent,
                                                     'all': op})
            elif str(uid) == str(id):
                return render(request, 'chat.html', {'username': user.name,
                                                     'To':id,
                                                     'current_user':id,
                                                     'current': current,
                                                     'all':data})
            else:
                return render(request, 'login.html', {'username': 'Wrong pass'})
    else:
        return render(request, 'login.html')

def chat(request, uid):
    """
    Get the chat between two users.
    :param request:
    :param username:
    :return:
    """
    friend = Userprofile.objects.get(uid=uid).name
    print(uid)
    messages = Messages.objects.filter(sender_name=111111, receiver_name=uid) | Messages.objects.filter(sender_name=uid, receiver_name=111111)

    data = Userprofile.objects.all()
    curr = Userprofile.objects.get(name='sachin').uid
    current=Userprofile.objects.filter(uid=111111)
    return render(request, "chat.html",{'username': friend,
                                        'messages': messages,
                                        'To': uid,
                                        'current_user': curr,
                                        'current':current,
                                        'all':data
                                        })
def ticket_user(request, tid):
    """
    Get the chat between two users.
    :param request:
    :param username:
    :return:
    """
    print('tickeuser')
    from uuid import getnode as get_mac
    mac = get_mac()
    friend = ticketprofile.objects.get(tid=tid).tname
    iden = Userprofile.objects.get(uid=mac)
    username = Userprofile.objects.get(uid=123456).name
    name = Userprofile.objects.get(uid=mac).name

    messages = openticket.objects.filter(osender_name=123456, oreceiver_name=tid) | openticket.objects.filter(osender_name=tid, oreceiver_name=123456)
    # print(messages)
    data = ticketprofile.objects.all()
    curr = Userprofile.objects.get(name='rfmnarveer').uid
    current = Userprofile.objects.filter(uid=mac)
    print(current)
    return render(request, "openticket.html",{'username': username,
                                             'name':name,
                                             'To': 123456,
                                             'messages': messages,
                                             'current_user': iden,
                                             'current': current
                                             })
def ticket(request, tid):
    """
    Get the chat between two users.
    :param request:
    :param username:
    :return:
    """

    friend = ticketprofile.objects.get(tid=tid).tname
    # print(tid)
    messages = openticket.objects.filter(osender_name=123456, oreceiver_name=tid) | openticket.objects.filter(osender_name=tid, oreceiver_name=123456)
    # print(messages)
    data = ticketprofile.objects.all()
    curr = Userprofile.objects.get(name='rfmnarveer').uid
    current=Userprofile.objects.filter(uid=123456)
    print(current)
    return render(request, "openticket.html",{'username': friend,
                                        'messages': messages,
                                        'To': tid,
                                        'current_user': curr,
                                        'current':current,
                                        'all':data
                                        })
@csrf_exempt
def openusersave(request):
    print('saving')
    id = request.POST['id']




    if request.method == "POST":
        try:
            userlogin.objects.get(lid=id)
            ac=userlogin.objects.get(lid=id).access
            print('...........',ac)
            if ac == True:
                mydata='......hello'
                s='save'
            else:
                mydata = '........error'
                s=0
        except:
            mydata='........error'
            s=0
        print(mydata)
        return JsonResponse({'data':mydata, 'status' : s})
@csrf_exempt
def open_message_list(request):
    print('openmessage')
    sender = request.POST['sender_name']
    receiver = request.POST['receiver_name']
    message = request.POST['description']
    mydata='{"sender_name": "' + sender + '", "receiver_name": "' +receiver + '","description": "' + message + '" }'

    if request.method == "POST":
        omsg = openticket()
        omsg.description=message
        omsg.osender_name=Userprofile.objects.get(uid=int(sender))
        omsg.oreceiver_name=Userprofile.objects.get(uid=int(receiver))
        omsg.seen=True
        omsg.save()
        print('........osave')
        return JsonResponse({'data':mydata, 'status' : 'save'})
@csrf_exempt
def message_list(request):
    print('mess')
    sender = request.POST['sender_name']
    receiver = request.POST['receiver_name']
    message = request.POST['description']
    mydata='{"sender_name": "' + sender + '", "receiver_name": "' +receiver + '","description": "' + message + '" }'

    if request.method == "POST":
        print('post')
        msg = Messages()
        msg.description=message
        msg.sender_name=Userprofile.objects.get(uid=int(sender))
        msg.receiver_name=Userprofile.objects.get(uid=int(receiver))
        msg.seen=True
        msg.save()
        print('save')
        return JsonResponse({'data':mydata, 'status' : 'save'})
@csrf_exempt
def registration(request):
    mac=get_mac()
    name = Userprofile.objects.get(uid=int(mac)).name
    if request.method == 'POST':
        if request.POST.get('email'):
            post = userlogin()
            post.lid = mac
            post.lname = name
            post.email=request.POST.get('email')
            post.password=request.POST.get('psw')
            post.save()
            return render(request, "user_login.html", {'name': name})
    else:
        return render(request, "user_login.html",{'name':name})
@csrf_exempt
def update(request):
    if request.method=='POST':
        if request.POST.get('access'):
            uid=request.POST.get('access')
            print(uid)
            up = userlogin()
            up.lid = uid
            name = userlogin.objects.get(lid=uid).lname
            email = userlogin.objects.get(lid=uid).email
            password = userlogin.objects.get(lid=uid).password
            up.lname = name
            up.email = email
            up.password = password
            up.access = True
            up.save()
            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 0})
    else:
        return JsonResponse({'status': 0})