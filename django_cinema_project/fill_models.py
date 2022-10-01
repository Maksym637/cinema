import django
import os

from app_user.models import User


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cinema_project.settings')
django.setup()


def main():
    user1 = User(1, 'u1', 'user1', 'user1', 'user1@gmail.com', '1111', '1111', False)
    user2 = User(2, 'u2', 'user2', 'user2', 'user2@gmail.com', '2222', '2222', False)
    user3 = User(3, 'u3', 'user3', 'user3', 'user3@gmail.com', '3333', '3333', False)

    user1.save()
    user2.save()
    user3.save()

    print(User.objects.all())


if __name__ == '__main__':
    main()