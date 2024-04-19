from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .services.back import find_recipe
import json


def index(request):
    return JsonResponse({"value": "Hello, world. You're at the backend_app index"})


@csrf_exempt
def find(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            print(json_data)
            recipe = find_recipe(json_data["user_input"])
            return JsonResponse({"recipe": recipe})
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
    else:
        return HttpResponseBadRequest("Only POST method is supported")
