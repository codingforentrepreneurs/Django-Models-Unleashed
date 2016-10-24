from django.core.exceptions import ValidationError

def validate_author_email(value):
    if not "@" in value:
        raise ValidationError("Not a valid email")
    return value
        

def validate_justin(value):
    if not "justin" in value:
        raise ValidationError("Not justin")
    return value