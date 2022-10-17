from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from app_film.models import Film
from app_hall.models import Hall
from .models import Schedule

from .serializers import ScheduleSerializer
from datetime import datetime


def time_is_correct(time_start_checked, time_end_checked, hall):
    flag = False
    schedules = Schedule.objects.all()
    for schedule in schedules:
        if schedule.hall == hall:
            if time_start_checked <= schedule.time_start and schedule.time_end <= time_end_checked:
                return flag
            elif time_start_checked > schedule.time_start and schedule.time_end > time_end_checked:
                return flag
            elif time_start_checked < schedule.time_start and time_end_checked > schedule.time_start:
                return flag
            elif time_start_checked < schedule.time_end and time_end_checked > schedule.time_end:
                return flag
    return True


class ScheduleView(APIView):
        
    # get all schedules | schedule by id
    def get(self, request, id=None):
        if id:
            schedule = get_object_or_404(Schedule.objects.all(), pk=id)
            serializer = ScheduleSerializer(schedule, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # create a new schedule
    def post(self, request):
        request_data = request.data
        time_start = request_data['time_start']
        time_end = request_data['time_end']
        date = request_data['date']
        film = get_object_or_404(Film.objects.all(), pk=request_data['film_id'])
        hall = get_object_or_404(Hall.objects.all(), pk=request_data['hall_id'])

        try:
            time_start_checked = datetime.strptime(time_start, '%H:%M:%S').time()
            time_end_checked = datetime.strptime(time_end, '%H:%M:%S').time()
            date_checked = datetime.strptime(date, '%Y-%m-%d').date()

            if time_is_correct(time_start_checked, time_end_checked, hall):
                Schedule.create(film, hall, time_start_checked, time_end_checked, date_checked).save()
                return Response({'success': 'Object is created.'}, status=status.HTTP_201_CREATED)
            return Response({'detail': 'This time is forbidden.'}, status.HTTP_403_FORBIDDEN)

        except ValueError:
            return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # delete schedule by id
    def delete(self, request, id=None):
        schedule = get_object_or_404(Schedule.objects.all(), pk=id)
        schedule.delete()
        return Response({'success': 'Object is deleted.'}, status=status.HTTP_204_NO_CONTENT)
    
    # update schedule by id
    def put(self, request, id=None):
        schedule = get_object_or_404(Schedule.objects.all(), pk=id)

        request_data = request.data
        time_start = request_data['time_start']
        time_end = request_data['time_end']
        date = request_data['date']

        try:
            time_start_checked = datetime.strptime(time_start, '%H:%M:%S').time()
            time_end_checked = datetime.strptime(time_end, '%H:%M:%S').time()
            date_checked = datetime.strptime(date, '%Y-%m-%d').date()
            
            if time_is_correct(time_start_checked, time_end_checked, schedule.hall):
                schedule.time_start, schedule.time_end, schedule.date = str(time_start_checked), str(time_end_checked), str(date_checked)
                schedule.save()
                return Response({'success': 'Object is updated.'}, status=status.HTTP_200_OK)
            return Response({'detail': 'This time is forbidden.'}, status.HTTP_403_FORBIDDEN)

        except ValueError:
            return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)
