import json
from django.http import HttpResponse
from .models import Pitches, Object
from django.views.decorators.csrf import csrf_exempt


def pict(post):
    ans = {"id": str(post.id),

           "entrepreneur": str(post.entrepreneur),

           "pitchTitle": str(post.pitchTitle),

           "pitchIdea": str(post.pitchIdea),

           "askAmount": float(post.askAmount),

           "equity": float(post.equity),

           "offers": [
               {"id": str(i["id"]),
                "investor": str(i["investor"]),
                "amount": float(i["amount"]),
                "equity": float(i["equity"]),
                "comment": str(i["comment"])
                } for i in Object.objects.filter(pitches_id=post.id).values()]
           }
    return ans


@csrf_exempt
def pitches(request, *args, **kwargs):
    if len(kwargs) == 0:
        if request.method == 'GET':
            pic = Pitches.objects.all()
            response = [pict(post) for post in pic]
            return HttpResponse(json.dumps(response))
        elif request.method == 'POST':
            response = request.body.decode('utf-8')
            body = json.loads(response)
            u = Pitches(entrepreneur=body["entrepreneur"], pitchTitle=body["pitchTitle"],
                        pitchIdea=body["pitchIdea"], askAmount=body["askAmount"], equity=body["equity"])
            u.save()
            ans = {'id': u.id}
            ans = json.dumps(ans)
            return HttpResponse(ans)
    else:
        if request.method == 'GET':
            pic = Pitches.objects.filter(id=kwargs['id_p'])
            response = [pict(post) for post in pic][0]
            return HttpResponse(json.dumps(response))
        elif request.method == 'POST':
            response = request.body.decode('utf-8')
            body = json.loads(response)
            u = Object(investor=body["investor"], amount=body["amount"], equity=body["equity"],
                       comment=body["comment"], pitches_id=kwargs["id_p"])
            u.save()
            ans = {'id': u.id}
            ans = json.dumps(ans)
            return HttpResponse(ans)
