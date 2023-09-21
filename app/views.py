import json
from django.utils import timezone
from .models import Kanban
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse


# Inicializa Verificação Ajax
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


def kanban(request):
    return render(request, 'app/kanban.html', {})


def update_kanban(request):

    context = {}
    kanban = get_object_or_404(Kanban, pk=1)
     
    if is_ajax(request=request) and request.method == "GET":

        kanban.data = request.GET.get("data", None)
        if not kanban.created_date:
            kanban.created_date = timezone.now()
        kanban.published_date = timezone.now()
        kanban.save()

        data = json.loads(kanban.data)
        data = len(data["cards"])

        context['maxid'] = data
        context['valid'] = True
        return JsonResponse(context, status=200)

    return JsonResponse({}, status=400)


def kanban_data(request):

    context = {}
    kanban = get_object_or_404(Kanban, pk=1)
     
    if is_ajax(request=request):

        data = kanban.data

        context['data'] = data
        return JsonResponse(context, status=200)

    return JsonResponse({}, status=400)


def testes(request):

    context = {}
    kanban = get_object_or_404(Kanban, pk=1)

    if is_ajax(request=request):

        data = kanban.data
        data = json.loads(data)
        context['dcount'] = len(data["cards"])

        return JsonResponse(context, status=200)

    return JsonResponse({}, status=400)
