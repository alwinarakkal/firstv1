from django.shortcuts import render,redirect
from signin.models import UserProfile                   #neww222
from signin.forms import ExtendedUserCreationForm, UserProfileForm #neww222
from .models import Post,Item

# Create your views here.

from .forms import ser_req
from .forms import buy
from django.core.paginator import Paginator

#for email
from django.core.mail import send_mail
from django.conf import settings




def req(request):
    aut=request.user.username
    if request.method == "POST":
        form = ser_req(request.POST,initial={'aut':aut})
        if form.is_valid():
            form.save()
            return redirect('email')    
    else:
        form = ser_req(initial={'aut':aut})
    context = {
        'form':form
    }
    return render(request, 'Ask_form.html', context)
    



def shop(request):                                              #neww
    aut=request.user.username
    if request.method == "POST":
        form = buy(request.POST,initial={'aut':aut})
        if form.is_valid():
            form.save()
            return redirect('gmail')

    else:
        form = buy(initial={'aut':aut})
    context = {
        'form':form
    }
    return render(request, 'buy2.html', context)


def serv_mail(request):    

    current_user=request.user
    mail=request.user.email
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    x=str(flat_number)
    
    mobile_number=obj.mobile_number
    y=str(mobile_number)
    
    # obj2=Post.objects.filter(aut=current_user).order_by('created')[:1]
    obj2=Post.objects.last()
    msg=obj2.body
    p=str(msg)

    mg=obj2.flat_number
    s=str(mg)
    
    z="flat number :"+x+"\n"+"mobile number  :"+y+"\n"+"problem: "+p+"\n"+"Time: "+s

    subject = 'Service request posted'
    message=z
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['aalwinarakkal@gmail.com',mail] 
    send_mail( subject, message, email_from, recipient_list )    
    return redirect('show')


def shopmail(request):    
    
    current_user=request.user
    mail=request.user.email
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    x=str(flat_number)
    
    mobile_number=obj.mobile_number
    y=str(mobile_number)
    
    # obj2=Post.objects.filter(aut=current_user).order_by('created')[:1]
    obj2=Item.objects.last()

    sel1=obj2.bread
    if sel1 =='a':
        b= "Bread 1 packet ,"+"\n"
    elif sel1=='f':
        b="Bread 2 packet ,"+"\n"
    elif sel1=='g':
        b="Bread 3 packet ,"+"\n"
    else:
         b=""
    sel2=obj2.water
    if sel2=='b':
        w= "1 CAN-WATER  ,"+"\n"
    elif sel2=='h':
        w="2 CAN-WATER ,"+"\n"
    elif sel2=='i':
        w="3 CAN-WATER,"+"\n"
    else :
        w=""
    
    sel3=obj2.milk
    if sel3 == 'd':
        m= "milk 2 packet  "+"\n"
    elif sel3=='c':
        m="milk 1 packet"+"\n"
    elif sel3=='e':
        m="milk 3 packet"+"\n"
    else :
        m=""

    sel4=obj2.rice
    if sel4 == 'j':
        r= "Rice 1 kg  "+"\n"
    elif sel4=='k':
        r="Rice 3 kg "+"\n"
    elif sel4=='l':
        r="Rice 5 kg "+"\n"
    elif sel4=='z':
        r="Rice 10 kg "+"\n"
    else :
        r=""
    
    z="flat number :"+x+"\n"+"mobile number :"+y+"\n"
    
    
    shoppinglist=(z+"Item List :"+"\n"+b+w+m+r)
    
    context = {
        'details':shoppinglist
    }
    
    
   #email details---

    subject = 'You have orders'
    message=shoppinglist
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['aalwinarakkal@gmail.com',mail] 
    print (obj2.bread or obj2.bread )
    if (obj2.bread or obj2.water or obj2.milk or obj2.rice):
        send_mail( subject, message, email_from, recipient_list )    
    
   
    
    return redirect('list')


def Myreqview(request):              #display service requests

    query_results = Post.objects.all().order_by('-created')
    aut=request.user.username
                                                    #pagination
    paginator=Paginator(query_results,5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        query_results = paginator.page(page)
    except(EmptyPage, InvalidPage):
        query_results=paginator.page(paginator.num_pages)
                                                     #/pagination                   

    context = {
        'details':query_results,
        'aut':aut
    }
    return render(request, 'show.html',context)


def MyView(request):                #display ordered items

    query_results = Item.objects.all().order_by('-created')
    aut=request.user.username
                                                        #pagination
    paginator=Paginator(query_results,5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        query_results = paginator.page(page)
    except(EmptyPage, InvalidPage):
        query_results=paginator.page(paginator.num_pages)
                                                        #/pagination
    context = {
        'details':query_results,
        'aut':aut
    }
    return render(request, 'display.html',context)


