import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cinema_project.settings')
django.setup()

from app_user.models import User
from app_film.models import Film
from app_hall.models import Hall
from app_seat.models import Seat
from app_schedule.models import Schedule


def main():
    user_1 = User.create('u1', 'user1', 'user1', 'user1@gmail.com', '1111', '1111', False)
    film_1 = Film.create('film1', 'film1', 'language1', '2022-10-3', 5)
    hall_1 = Hall.create(5, 250)
    user_1.save()
    film_1.save()
    hall_1.save()

    seat_1 = Seat.create(hall_1, seating=2, is_free=True)
    seat_1.save()

    schedule_1 = Schedule.create(film_1, hall_1, '14:00:00', '15:30:00', '2022-10-24')
    schedule_1.save()

    print("\nALL CREATED USERS\n")
    print(User.objects.all()[0])
    print("\nALL CREATED FILMS\n")
    print(Film.objects.all()[0])
    print("\nALL CREATED HALLS\n")
    print(Hall.objects.all()[0])
    print("\nALL CREATED SEATING\n")
    print(Seat.objects.all()[0])
    print("\nALL CREATED SCHEDULES\n")
    print(Schedule.objects.all()[0])


if __name__ == '__main__':
    main()