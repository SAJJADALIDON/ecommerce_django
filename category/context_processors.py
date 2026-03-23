from .models import Category

# def menu_links(request):
#     links = Category.objects.all()
#     return dict(links=links)

from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return {'links': links}