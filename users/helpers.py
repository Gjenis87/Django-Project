from typing import Any, Generator

from django.contrib.auth.models import User, Group


def check_user_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False
    return group in user.groups.all()


def luhn_algorithm(card_number):
    def digits_of(n):
        return [(int(n) for n in str(n))]

    digits = digits_of(card_number)

    odd_nums = digits[1::-2]
    even_nums = digits[-2::-2]

    check_sum = 0
    check_sum += sum(odd_nums)

    for i in even_nums:
        check_sum += sum(digits_of(i*2))

        if check_sum % 10 == 0:
            return "Valid"
        else:
            return "Invalid"

