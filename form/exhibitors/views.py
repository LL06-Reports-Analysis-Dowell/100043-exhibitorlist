from django.shortcuts import render
from .models import Exhibitor
from event.models import Details
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mass_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from django.core.files.storage import FileSystemStorage
from pymongo import MongoClient
import gridfs
# Create your views here.
def index(request):
    return render(request, 'exhibitors/form1.html')

def multistepform1_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        email = request.POST.get("email")

        event = Details.objects.filter(exhibitor_creator_list = email)
        event_length = len(event)
        complete = 0
        # print(event)
        for eve in range(event_length):
            if event[eve].status == "Complete":
                complete = 1
            elif event[eve].status == "InProgress":
                complete = 0
                return render(request, 'exhibitors/form2.html',{'email':email,
                                                                'event':event[eve]})
            elif event[eve].status == "Error":
                messages.error(request,"Sorry Event status is Error, Exhibitor can not be created!")
                return HttpResponseRedirect(reverse('exhibitors:thanks'))
        if complete == 1:
            return render(request, 'exhibitors/event_details.html',{'obj':event[0]})
        # if event:
        #     if event[0].status == "Complete":
        #         return render(request, 'exhibitors/event_details.html',{'obj':event[0]})
        #     if event[0].status == "InProgress":
        #         return render(request, 'exhibitors/form2.html',{'email':email,
        #                                                         'event':event[0]})
        #     else:
        #         messages.error(request,"Sorry Event status is Error, Exhibitor can not be created!")
        #         return HttpResponseRedirect(reverse('exhibitors:thanks'))
        else:
            messages.error(request,"Sorry No record found, Exhibitor can not be created!")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))

def multistepform2_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        email = request.POST.get("email")
        name = request.POST.get("name")
        brand_name = request.POST.get("brand_name")
        name_incharge = request.POST.get("name_incharge")
        designation_incharge = request.POST.get("designation_incharge")
        exhibitor_page_link = request.POST.get("exhibitor_page_link")
        exhibitor_website = request.POST.get("exhibitor_website")
        exhibitor_email = request.POST.get("exhibitor_email")
        exhibitor_both_number = request.POST.get("exhibitor_both_number")
        exhibitor_city = request.POST.get("exhibitor_city")
        exhibitor_country = request.POST.get("exhibitor_country")
        exhibitor_address = request.POST.get("exhibitor_address")
        type = request.POST.get("type")
        exhibitor_product = request.POST.get("exhibitor_product")
        linkedin = request.POST.get("linkedin")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        youtube = request.POST.get("youtube")
        tiktok = request.POST.get("tiktok")
        hashtag = request.POST.get("hashtag")
        mention = request.POST.get("mention")
        description = request.POST.get("description")
        logo_image = request.FILES['logo'] if 'logo' in request.FILES else None

        if logo_image:
            # save attatched logo
            # create a new instance of FileSystemStorage
            # fs = FileSystemStorage()
            string = 'mongodb+srv://qruser:qr1234@cluster0.n2ih9.mongodb.net/DB_IMAGE?retryWrites=true&w=majority'
            connection = MongoClient(string)
            db = connection.exhibitor_details
            fs = gridfs.GridFS(db, collection='fs')
            # saving image in mongo db
            file = fs.put(logo_image, filename=logo_image.name, email = email,
            name = name,
            brand_name = brand_name,
            name_incharge = name_incharge,
            designation_incharge = designation_incharge,
            exhibitor_page_link = exhibitor_page_link,
            exhibitor_website = exhibitor_website,
            exhibitor_email = exhibitor_email,
            exhibitor_both_number = exhibitor_both_number,
            exhibitor_city = exhibitor_city,
            exhibitor_country = exhibitor_country,
            exhibitor_address = exhibitor_address,
            type = type,
            exhibitor_product = exhibitor_product,
            linkedin = linkedin,
            twitter = twitter,
            facebook = facebook,
            instagram = instagram,
            youtube = youtube,
            tiktok = tiktok,
            hashtag = hashtag,
            mention = mention,
            description = description)

        try:
            Exhibitor.objects.create(
            email = email,
            name = name,
            brand_name = brand_name,
            name_incharge = name_incharge,
            designation_incharge = designation_incharge,
            exhibitor_page_link = exhibitor_page_link,
            exhibitor_website = exhibitor_website,
            exhibitor_email = exhibitor_email,
            exhibitor_both_number = exhibitor_both_number,
            exhibitor_city = exhibitor_city,
            exhibitor_country = exhibitor_country,
            exhibitor_address = exhibitor_address,
            type = type,
            exhibitor_product = exhibitor_product,
            linkedin = linkedin,
            twitter = twitter,
            facebook = facebook,
            instagram = instagram,
            youtube = youtube,
            tiktok = tiktok,
            hashtag = hashtag,
            mention = mention,
            description = description,
            # logo = logo
            logo = logo_image
            )
            messages.success(request,"Exhibitor Saved Successfully, Thank you.")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))
        except:
            messages.error(request,"Error in Saving Exhibitor")
            return HttpResponseRedirect(reverse('exhibitors:thanks'))

def response_recorded(request):
    return render(request, 'exhibitors/thanks.html')

def event_details(request):
    return render(request, 'exhibitors/event_details.html')
@login_required
def create_email(request):
    return render(request, 'exhibitors/create_email.html')

@login_required
def send_email(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("exhibitors:main-view"))
    else:
        subject = request.POST.get("subject")
        content = request.POST.get("content")
        link = request.POST.get("link")
        email_list = list(Exhibitor.objects.values_list('exhibitor_email', flat=True))
        message = content +'\n'+ link
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_list
        # print(subject, content, link)
        mes = ()
        # print(email_list)
        for i in range(len(recipient_list)):
            mes = mes + ((subject, message, email_from, [recipient_list[i]]) , )
        # print(mes)
        # mes = mes + ((subject, message, email_from, ["anjanas@dowellresearch.in"]) , )
        send_mass_mail(mes, fail_silently=False)

    return render(request, 'exhibitors/send_email.html')
