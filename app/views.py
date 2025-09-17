from django.http import JsonResponse

def ping(request):
    return JsonResponse({"message": "pong"})

def sum_numbers(request):
    a_raw = request.GET.get("a", "0")
    b_raw = request.GET.get("b", "0")
    try:
        a = int(a_raw)
        b = int(b_raw)
    except ValueError:
        return JsonResponse({"error": "Invalid numbers"}, status=400)
    
    return JsonResponse({"result": a + b})
