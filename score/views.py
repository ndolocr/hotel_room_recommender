from django.shortcuts import render
from django.http import JsonResponse

from score.models import Score

# Create your views here.

def ViewAll(request):
    if request.method == 'GET':
        try:
            scores  = Score.nodes.all()
            response = []
            context = {}
            for data in scores:
                obj = {
                    'uid': data.uid,
                    'score' : data.score,
                    'code' : data.code,
                    'score_for' : data.score_for,        
                    'created_on' : room.created_on,                                       
                }
                response.append(obj)
            context = {"data": response}
            return render(request, 'score/view_all.html', context)
        except Exception as e:
            response = {"Error": "Error occurred while getting room records - {}".format(e)}
            return JsonResponse(response, safe=False)