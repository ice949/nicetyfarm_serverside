from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse(request, '<h1>hello world</h1>')

def user_profile(request):
    return JsonResponse({'name': 'John', 'age': 30, 'email': ''})



def filter_querries(request, id):
    queries = [
        {
            "id": 1,
            "title": "title1",
            "description": "description1",
            "status": "PENDING",
            "created_at": "created_at1",
            "submitted_by": "submitted_by1",
        },
        {
            "id": 2,
            "title": "title2",
            "description": "description2",
            "status": "APPROVED",
            "created_at": "created_at2",
            "submitted_by": "submitted_by2",
        },
        {
            "id": 3,
            "title": "title3",
            "description": "description3",
            "status": "DECLINED",
            "created_at": "created_at3",
            "submitted_by": "submitted_by3",
        }
    ]

    filtered_query = [query for query in queries if query["id"] == id]

    querry = filtered_query[0]

    return JsonResponse(querry, safe=False)

class QuerryView(View):
    def get(self, request, id):
        queries = [
            {
                "id": 1,
                "title": "title1",
                "description": "description1",
                "status": "PENDING",
                "created_at": "created_at1",
                "submitted_by": "submitted_by1",
            },
            {
                "id": 2,
                "title": "title2",
                "description": "description2",
                "status": "APPROVED",
                "created_at": "created_at2",
                "submitted_by": "submitted_by2",
            },
            {
                "id": 3,
                "title": "title3",
                "description": "description3",
                "status": "DECLINED",
                "created_at": "created_at3",
                "submitted_by": "submitted_by3",
            }
        ]

        filtered_query = [query for query in queries if query["id"] == id]

        querry = filtered_query[0]

        return JsonResponse(querry, safe=False)

    def post(self, request):
        return JsonResponse({'message': 'POST method is not allowed'}, status=405)

    def put(self, request):
        return JsonResponse({'message': 'PUT method is not allowed'}, status=405)

    def delete(self, request):
        return JsonResponse({'message': 'DELETE method is not allowed'}, status=405)
    
    def patch(self, request):
        return JsonResponse({'message': 'PATCH method is not allowed'}, status=405)


