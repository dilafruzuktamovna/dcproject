import datetime as datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def get_new_slider(request):
    header = Header.objects.all().order_by('-id')[:3]
    ser = HeaderSerializer(header, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_video(request):
    video = Video.objects.all().order_by('-id')[:4]
    ser = VideoSerializer(video, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_players(request):
    team = Players.objects.all()
    data = {
        'time': datetime.datetime.now().time(),
        'date': datetime.datetime.now().date(),
        'team': TeamSerializer(team, many=True).data,
        'team_count': team.count(),
        'last_player': TeamSerializer(team, many=True).data,
    }
    return Response(data)


@api_view(['GET'])
def get_shop(request):
    shop = Shop.objects.all()
    ser = ShopSerializer(shop, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_information(request):
    info = Information.objects.all()
    ser = InformationSerializer(info, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_partners(request):
    partner = Partners.objects.all().order_by('-id')[:5]
    ser = PartnersSerializer(partner, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_news(request):
    news = News.objects.last().order_by('-id')
    ser = NewsSerializer(news).data
    return Response(ser)


@api_view(['GET'])
def get_club(request):
    club = Club.objects.all()
    ser = ClubSerializer(club, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_academy(request):
    academy = Academy.objects.all()
    ser = AcademySerializer(academy, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_arena(request):
    arena = Arena.objects.all()
    ser = ArenaSerializer(arena, many=True).data
    return Response(ser)
