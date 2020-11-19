from django import template

register = template.Library()

def mult(value, arg):
    "Multiplies the arg and the value"
    return int(value) * int(arg)
mult.is_safe = False

register.filter("mul",mult)