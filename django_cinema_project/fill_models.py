import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cinema_project.settings')
django.setup()

from app_user.models import User
from app_film.models import Film
from app_hall.models import Hall
from app_seat.models import Seat
from app_schedule.models import Schedule
from app_booking.models import Booking


def main():
    user_1 = User.create('u1', 'user1', 'user1', 'user1@gmail.com', '1111', '1111', False)
    film_1 = Film.create('film1', 1, 1, None, '2022-10-3', 5)
    hall_1 = Hall.create(5, 250)
    hall_2 = Hall.create(10, 500)

    user_1.save()
    film_1.save()
    hall_1.save()
    hall_2.save()

    seat_1 = Seat.create(hall_1, seating=Seat.CLS, is_free=True)
    seat_2 = Seat.create(hall_1, seating=Seat.CLS, is_free=True)
    seat_3 = Seat.create(hall_1, seating=Seat.VIP, is_free=True)

    seat_1.save()
    seat_2.save()
    seat_3.save()

    schedule_1 = Schedule.create(film_1, hall_1, '14:00:00', '15:30:00', '2022-10-24')
    schedule_1.save()

    booking_1 = Booking.create(150, user_1, seat_2, schedule_1)
    booking_1.save()

    print("\nALL CREATED USERS\n")
    print(User.objects.all()[0])
    print("\nALL CREATED FILMS\n")
    print(Film.objects.all()[0])
    print("\nALL CREATED HALLS\n")
    print(Hall.objects.all()[0])
    print("\nALL CREATED SEATINGS\n")
    for i in range(len(Seat.objects.all())):
        print(Seat.objects.all()[i], '\n')
    print("ALL CREATED SCHEDULES\n")
    print(Schedule.objects.all()[0])
    print("\nALL CREATED BOOKINGS\n")
    print(Booking.objects.all()[0])


if __name__ == '__main__':
    main()
