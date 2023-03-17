import uuid, json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie


from backend.models import Task

@ensure_csrf_cookie
@require_GET
def home(request):
    return render(request, 'backend/home.html', {'tasks': Task.objects.all()})


@ensure_csrf_cookie
@require_GET
def list_tasks(request):
    return JsonResponse({'tasks': [{
        'uuid': e.uuid,
        'createdAt': e.created_at.isoformat(),
        'updatedAt': e.created_at.isoformat(),
        'order': e.order,
        'title': e.title,
        'description': e.description,
        'completed': e.completed,
    } for e in Task.objects.all()]})


@require_POST
def edit_tasks(request):
    data = json.loads(request.body)
    try:
        task = Task.objects.get(uuid = data['uuid'])
        task.title = data['newTitle']
        task.save()
        return HttpResponse(content="Successful save",status=200)
    except Task.DoesNotExist:
        return HttpResponse(status=504)
