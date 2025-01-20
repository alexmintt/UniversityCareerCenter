from django import template

from vacancy.models import Vacancy

register = template.Library()

@register.simple_tag
def say_hello_world():
    return "Добро пожаловать"


@register.simple_tag
def show_name(username):
    return f" {username}"

@register.simple_tag
def get_size_of_vacancies():
    return len(Vacancy.objects.all())
