from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse

from score.models import Score

# Create your views here.

def viewAll(request):
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
                    'created_on' : data.created_on,                                       
                }
                response.append(obj)
            context = {"data": response}
            return render(request, 'score/view_all.html', context)
        except Exception as e:
            response = {"Error": "Error occurred while getting score records - {}".format(e)}
            return JsonResponse(response, safe=False)

def addScore(request):
    if request.method == 'POST':
        try:
            code = request.POST["code"]
            score = request.POST["score"]
            score_for = request.POST["score_for"]            
            
            query = Score(
                code = code,
                score = score,
                score_for = score_for,
                created_on = datetime.now()
            )

            query.save()
            return render(request, 'score/add.html')
        except Exception as e:
            response = {"ERROR": "Error while saving score information- {}".format(e)}
            return JsonResponse(response)
    else:
        return render(request, 'score/add.html')