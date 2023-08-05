from dataclasses import dataclass

from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.forms import ValidationError
from django.utils.crypto import get_random_string
from unidecode import unidecode

from ..hooks import oauth2_user_data_filters
from ..users.validators import (
    validate_new_registration,
    validate_username_content,
    validate_username_length,
)
from .exceptions import OAuth2UserDataValidationError

User = get_user_model()


class UsernameSettings:
    username_length_max: int = 200
    username_length_min: int = 1


def validate_user_data(request, user, user_data):
    filtered_data = filter_user_data(request, user, user_data)

    try:
        errors_list = []

        def add_error(_field_unused: str | None, error: str | ValidationError):
            if isinstance(error, ValidationError):
                error = error.message

            errors_list.append(str(error))

        validate_username_content(user_data["name"])
        validate_username_length(UsernameSettings, user_data["name"])
        validate_email(user_data["email"])

        validate_new_registration(request, filtered_data, add_error)
    except ValidationError as exc:
        raise OAuth2UserDataValidationError(error_list=[str(exc.message)])

    if errors_list:
        raise OAuth2UserDataValidationError(error_list=errors_list)

    return filtered_data


def filter_user_data(request, user, user_data):
    if oauth2_user_data_filters:
        return filter_user_data_with_filters(
            request, user, user_data, oauth2_user_data_filters
        )
    else:
        user_data["name"] = filter_name(user, user_data["name"])

    return user_data


def filter_user_data_with_filters(request, user, user_data, filters):
    for filter_user_data in filters:
        user_data = filter_user_data(request, user, user_data) or user_data
    return user_data


def filter_name(user, name):
    if user and user.username == name:
        return name

    clean_name = "".join(
        [c for c in unidecode(name.replace(" ", "_")) if c.isalnum() or c == "_"]
    )

    if user and user.username == clean_name:
        return clean_name  # No change in name

    if not clean_name.replace("_", ""):
        clean_name = "User_%s" % get_random_string(4)

    clean_name_root = clean_name
    while True:
        try:
            db_user = User.objects.get_by_username(clean_name)
        except User.DoesNotExist:
            return clean_name

        if not user or user.pk != db_user.pk:
            clean_name = f"{clean_name_root}_{get_random_string(4)}"
        else:
            return clean_name
