from django.utils.translation import gettext as _
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Comment
from .forms import CommentForm, ContactForm, ReservationForm
import numpy as np

# Create your views here.


def home(request):
    return render(request, 'apartmany/index.html')


def studios(request):
    ranges = {'range_s1': range(2, 6),
              'range_s2': range(2, 4),
              'range_s3': range(2, 6),
              'range_s4': range(2, 7),
              'range_s5': range(2, 8),
              'range_s6': range(2, 8),
              'range_s8': range(2, 4),
              'range_s9': range(2, 9),
              'range_s10': range(2, 5)}
    return render(request, 'apartmany/studios.html', ranges)


def apartments(request):
    ranges = {'range_a7': range(2, 8),
              'range_a11': range(2, 14),
              'range_a12': range(2, 10),
              'range_a13': range(2, 13),
              'range_a14': range(2, 17)}
    return render(request, 'apartmany/apartments.html', ranges)


def surroundings(request):
    return render(request, 'apartmany/surroundings.html')


def guestbook(request):

    comments = Comment.objects.all()
    temp_ratings = []

    for comment in comments:
        temp_ratings.append(comment.rating)

    average_rating = round(np.average(temp_ratings), 1)

    ratings = {
        "average": average_rating,
        "amount": len(temp_ratings),
        "summary": {"five": {"tag": _("Excellent"),
                             "amount": temp_ratings.count(5),
                             "percentage": str((temp_ratings.count(5) / len(temp_ratings)) * 100) + '%'},
                    "four": {"tag": _("Good"),
                             "amount": temp_ratings.count(4),
                             "percentage": str((temp_ratings.count(4) / len(temp_ratings)) * 100) + '%'},
                    "three": {"tag": _("Average"),
                              "amount": temp_ratings.count(3),
                              "percentage": str((temp_ratings.count(3) / len(temp_ratings)) * 100) + '%'},
                    "two": {"tag": _("Poor"),
                            "amount": temp_ratings.count(2),
                            "percentage": str((temp_ratings.count(2) / len(temp_ratings)) * 100) + '%'},
                    "one": {"tag": _("Terrible"),
                            "amount": temp_ratings.count(1),
                            "percentage": str((temp_ratings.count(1) / len(temp_ratings)) * 100) + '%'}
                    }
    }

    print(ratings)

    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        print(comment_form)
        print(comment_form['name'])
        print(comment_form['content'])
        if comment_form.is_valid():
            # Create Comment object and save it to database
            new_comment = comment_form.save()
        else:
            print('Not valid')
    else:
        comment_form = CommentForm()

    context = {
        'comments': Comment.objects.all().reverse(),
        'form': comment_form,
        'ratings': ratings
    }

    return render(request, 'apartmany/guestbook.html', context)


def gallery(request):
    return render(request, 'apartmany/gallery.html')


def prices_and_faqs(request):
    return render(request, 'apartmany/prices_and_faqs.html')


def contact(request):

    if request.method == 'POST':
        if 'Submit-Contact' in request.POST:
            # form = ContactForm(data=request.POST)
            # if form.is_valid():
            name = request.POST['Name']
            email = request.POST['Email']
            subject = request.POST['Subject']
            message = request.POST['Message']

            send_mail(f'Contact Request: {subject}',
                      f'From: {name}\nEmail: {email}\n\n\n{message}',
                      settings.EMAIL_HOST_USER,
                      ['kevin.riedlberger@novasbe.pt'],
                      fail_silently=False)

            message = f'Thank you very much for your contact request {name}! We will contact you as soon as possible.'
            return render(request, 'apartmany/contact.html', {'message': message})

        elif 'Submit-Reservation' in request.POST:
            # form = ReservationForm(data=request.POST)
            # if form.is_valid():
            name = request.POST['Name']
            email = request.POST['Email']
            type = request.POST['Type']
            number = request.POST['Number']
            start = request.POST['Start_Date']
            end = request.POST['End_Date']
            guests = request.POST['Guests']
            message = request.POST['Message']

            send_mail(f'Reservation Request: {name}',
                      f'From: {name}\nEmail: {email}\n\n\nAccomodation Type: {type}\nAccomodation Number: {number}\nDate: {start} - {end}\nNumber Of Guests: {guests}\n\n\n{message}',
                      settings.EMAIL_HOST_USER,
                      ['riedlberger.kevin@gmail.com'],
                      fail_silently=False)

            message = f'Thank you very much for your reservation request {name}! We will contact you as soon as possible.'

            return render(request, 'apartmany/contact.html', {'message': message})

    print('We went this route, without')
    return render(request, 'apartmany/contact.html')
