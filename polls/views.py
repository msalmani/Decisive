from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
class UploadView(View):

	def get(self, request, *args, **kwargs):
		print 'get'
		return render(request, 'polls/index.html', {})
	def post(self, request, *args, **kwargs):
		print 'in post'
		myfile = request.FILES.get('file')
		if not myfile:
			return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)
		return ""

		