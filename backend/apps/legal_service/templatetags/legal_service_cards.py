from django import template

from ..models import LegalService

register = template.Library()


@register.inclusion_tag("templatetags/legal-service-cards.html")
def legal_service_cards() -> dict:
    objects = LegalService.objects.filter(is_published_landing=True)

    return {
        "objects": objects,
    }
