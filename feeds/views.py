from IPython import embed
from django.shortcuts import render, redirect
from .models import Feed

# Create your views here.
def index(request):
    feeds = Feed.objects.all()
    context = {
        'feeds': feeds,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        # 파일을 가져올때는 'FILES'를 사용한다.
        image = request.FILES.get('image')

        feed = Feed.objects.create(content=content, image=image)
        # embed() # ipython을 사용할 때 사용

        return redirect('feeds:index')
    else:
        return render(request, 'form.html')