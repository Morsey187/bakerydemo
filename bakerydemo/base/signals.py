import logging
import requests

from django.conf import settings
from wagtail.signals import page_published


logger = logging.getLogger(__name__)


def page_revalidation(**kwargs):
    instance = kwargs['instance']
    url_path = instance.url
    if instance.url != '/':
        url_path = instance.url.rstrip("/")

    url = f"http://localhost:3000/api/revalidate?secret={settings.MY_SECRET_NEXT_JS_REVALIDATION_TOKEN}&urlpath={url_path}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        logger.exception("Page '%s' failed to revalidate: %s", instance.url,  e)
        # Do nothing, perhaps add to 'messages' middleware to notify content editor
        pass

# Register a receiver
page_published.connect(page_revalidation)
