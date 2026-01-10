from rest_framework.exceptions import ValidationError

def validate_youtube_url(value):
    if not value.startswith("https://www.youtube.com"):
        raise ValidationError('Ссылка должна вести на YouTube')
