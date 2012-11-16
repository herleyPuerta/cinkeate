from django.shortcuts import render_to_response
from django.template import RequestContext


def index_view(request):
	return render_to_response('index.html',context_instance = RequestContext(request))