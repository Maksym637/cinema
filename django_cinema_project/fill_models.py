import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cinema_project.settings')
django.setup()

from app_user.models import User


def main():
    user1 = User.create('u1', 'user1', 'user1', 'user1@gmail.com', '1111', '1111', False)
    # user2 = User(2, 'u2', 'user2', 'user2', 'user2@gmail.com', '2222', '2222', False)
    # user3 = User(3, 'u3', 'user3', 'user3', 'user3@gmail.com', '3333', '3333', False)

    user1.save()
    # user2.save()
    # user3.save()

    print(User.objects.all()[0])
    # for i in range(len(User.objects.all())):
    #     print(User.objects.all()[i])


if __name__ == '__main__':
    main()