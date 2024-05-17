from django.shortcuts import render,get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.contrib.auth.models import User

from django.core.paginator import Paginator
def index(request):
    print(request.user)
    contacts = Contact.objects.filter(show=True,owner_id=request.user.id).order_by('-id')
    # contacts = Contact.objects.filter(show=True,owner_id=request.user.id).order_by('-id')
    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'contacts':page_obj,
        'site_title':'Contatos - '
    }
    return render(request,'contact/index.html',context)

def search(request):
    search_value = request.GET.get('q','').strip()
    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(Q(first_name__icontains=search_value)|Q(first_name__icontains=search_value)).order_by('-id')
    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'contacts':page_obj,
        'site_title':'Contatos - '
    }
   
    return render(request,'contact/index.html',context)

def contact(request,contact_id):
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True)
    context = {
        'contact':single_contact,
        'site_title':f'{single_contact.first_name} {single_contact.last_name} -'

    }
    return render(request,'contact/contact.html',context)