from django.http import JsonResponse

def ping(request):
    return JsonResponse({"message": "pong"})

def sum_numbers(request):
    result = 2 + 3
    return JsonResponse({"result": result})