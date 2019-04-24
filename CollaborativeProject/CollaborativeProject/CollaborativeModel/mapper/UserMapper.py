from CollaborativeProject.CollaborativeModel.models import Song, User


def get_user_by_name(name):
    result = User.objects.filter(name=name)
    return result
