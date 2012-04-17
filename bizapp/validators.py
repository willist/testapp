from django.core.validators import RegexValidator

pattern = (
    # Country code and zip code optional
    '(' +
    # Country code (us only for now)
    '1?' + 
    # Separator
    '([-\.]?)' +
    # Zip code
    '\d{3}' + 
    # /Country code and zip code optional
    ')?' + 
    # Separator
    '([-\.]?)' +
     # Local prefix
    '\d{3}' + 
    # Separator
    '([-\.]?)' +
     # Line number
    '\d{4}'
)


validate_phone = RegexValidator(pattern, "Must be a valid phone number.")
