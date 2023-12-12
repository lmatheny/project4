from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import NewDay
from .forms import NewDayForm  # Import the form you created for NewDay
from .forms import EditNewDayForm
from .models import StopwatchEntry
from .forms import UserAccountForm
from .models import UserAccount
from django.http import JsonResponse
from .forms import PersonForm
from .models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.



# def home_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if username == 'test' and password == 'pass':
#             return render(request, 'home.html')  # Change 'base.html' to 'logo.html'
#         else:
#             return HttpResponse('Invalid credentials. Please try again.')
#     else:
#         return render(request, 'login.html')

def home_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'GET':
        # Assuming you have a dynamic way to generate the links
        new_video_links = [

            "https://www.youtube.com/embed/jfKfPfyJRdk",
            "https://www.youtube.com/embed/6H-PLF2CR18",
            "https://www.youtube.com/embed/CfPxlb8-ZQ0",
            "https://www.youtube.com/embed/Na-YCNomwVw",
         
            "https://www.youtube.com/embed/X28GzyyN6G4",
            "https://www.youtube.com/embed/EilXptlNHPc",
            "https://www.youtube.com/embed/dKvJPrGN2zo",
            "https://www.youtube.com/embed/ySmjheVxYc4",


            "https://www.youtube.com/embed/n61ULEU7CO0",
            "https://www.youtube.com/embed/sca4VG9b0NY",
            "https://www.youtube.com/embed/GcUF2z_Yt5Y",
            "https://www.youtube.com/embed/5zTANw0sevA",


            "https://www.youtube.com/embed/0mtcvqslhIA",
            "https://www.youtube.com/embed/EHnStnU90Ww",
            "https://www.youtube.com/embed/VSlEbE4SvLk",
            "https://www.youtube.com/embed/4xCRgK79DJ4",


        ]
        return JsonResponse({'new_video_links': new_video_links})

    # Render the home page template for non-AJAX requests
    return render(request, 'home.html')



def stopwatch_view(request):
    # Retrieve existing entries from the database
    entries = StopwatchEntry.objects.all()

    # Pass the entries to the template
    return render(request, 'stopwatch.html', {'entries': entries})

def newDay_view(request):
    if request.method == 'POST':
        form = NewDayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')  # Update to the correct name
    else:
        form = NewDayForm()

    return render(request, 'newDay.html', {'form': form})

def success_page_view(request):
    return render(request, 'success_page.html')


def calendar_view(request):
    calendar_data = NewDay.objects.all()

    # Set the number of entries per page
    entries_per_page = 10

    # Use Django's Paginator to paginate the queryset
    paginator = Paginator(calendar_data, entries_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the current page
        calendar_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        calendar_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        calendar_data = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = EditNewDayForm(request.POST)
        if 'delete_entry' in request.POST:
            # Handle deletion
            entry_id = request.POST.get('delete_entry')
            entry = get_object_or_404(NewDay, id=entry_id)
            entry.delete()
            return redirect('calendar_view')
        elif form.is_valid():
            # Handle editing
            entry_id = form.cleaned_data['id']
            new_day_entry = get_object_or_404(NewDay, id=entry_id)
            form = EditNewDayForm(request.POST, instance=new_day_entry)
            if form.is_valid():
                form.save()
                return redirect('calendar_view')
    else:
        form = EditNewDayForm()

    return render(request, 'calendar.html', {'calendar_data': calendar_data, 'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Hardcoded values for testing
        hardcoded_username = 'Matheny'
        hardcoded_password = 'password'

        if username == hardcoded_username and password == hardcoded_password:
            # Login successful
            return redirect('home')  # Redirect to the home page or wherever you want

        else:
            # Login failed
            return render(request, 'login.html', {'login_failed': True})

    return render(request, 'login.html', {'login_failed': False})


def person_view(request):
    # Try to get the existing person object with ID=1 or create it if it doesn't exist
    person, created = Person.objects.get_or_create(id=1, defaults={'nickname': 'Bon', 'bio': 'Lives in Tampa', 'age': 22})

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person.html')  # Redirect to the same page after form submission
    else:
        form = PersonForm(instance=person)

    return render(request, 'person.html', {'person': person, 'form': form})