from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .utils import func2


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        text = request.POST.get('text')
        tokens = func2(text)
        return JsonResponse({'status': 'success', 'tokens': tokens[0], 'error_tokens': tokens[1]})