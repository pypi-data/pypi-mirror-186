from .base_extension import BaseExtension
from conf.project import STATICFILES_PATH
import os
# from gsnail.exceptions.views.templates.templ_exceptions import StaticFileNotFound
# from gsnail.routing.route import get_redirect_url


class StaticExt(BaseExtension):
    """
    Extensions for outputting files to html template.
    """
    tags = ['static']
    request = None

    @classmethod
    def set_request(cls, request):
        cls.request = request

    def handler(self, filepath: str):
        for path in STATICFILES_PATH:
            p = os.path.join(path, filepath)
            if os.path.exists(p):
                return p
        # raise StaticFileNotFound('StaticExt.handler', p)
