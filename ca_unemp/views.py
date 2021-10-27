from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StatSerializer
from .models import Unemployment



# Create your views here.
@api_view(['GET'])
def county_stats(request):
    print('county_stats(request)')
    geoid = request.GET.get('geoid', '')
    year = request.GET.get('year', 0)
    try:
        if geoid != "" and year != 0:
            query = Unemployment.objects.filter(geoid=geoid).filter(year=year)
        
        elif geoid != "":
            query = Unemployment.objects.filter(geoid=geoid)
        elif year != 0:
            print('county_stats(request) year != 0')
            query = Unemployment.objects.filter(year=year)
        else:
            query = Unemployment.objects.all()
        
    except Unemployment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StatSerializer(query, many=True)
    return Response(serializer.data)