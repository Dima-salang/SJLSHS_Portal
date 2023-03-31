from django.shortcuts import render
from wagtail.models import Page 

# Create your views here.
def home_page(request):
    home_page = Page.objects.get(slug='student-orgs')  # assuming 'home' is the slug for your home page
    return render(request, 'home_page.html', {'home_page': home_page})

def recent_links(request):
    ssg = Page.objects.get(slug='supreme-student-government')
    relevant_links = ssg.get_children().get_children()
    print(relevant_links)
    return render(request, "relevant_links.html", {'relevant_links': relevant_links})


def career_center_view(request):
    lac_pages = Page.objects.get(slug='litexian-achievers-club')
    print("got litexian pages")
    career_pages = lac_pages.get_children().filter(slug='career-center').first()
    print("got career pages")
    career_articles = career_pages.get_children().specific().live().order_by('-first_published_at')
    print("got articlces")
    
    context = {
        'career_articles' : career_articles
    }
    return render(request, 'career-center.html', context)