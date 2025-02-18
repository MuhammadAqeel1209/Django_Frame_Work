from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect('netflixapp:profile-list')
        return render(request, 'index.html')