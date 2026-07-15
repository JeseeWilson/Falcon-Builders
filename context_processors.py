from django.conf import settings


def company_info(request):
    """Makes core company details available in every template without
    passing them explicitly from each view."""
    return {
        'COMPANY_NAME': settings.COMPANY_NAME,
        'COMPANY_PHONE': settings.COMPANY_PHONE,
        'COMPANY_EMAIL': settings.COMPANY_EMAIL,
        'COMPANY_ADDRESS': settings.COMPANY_ADDRESS,
        'COMPANY_YEARS': settings.COMPANY_YEARS,
    }
