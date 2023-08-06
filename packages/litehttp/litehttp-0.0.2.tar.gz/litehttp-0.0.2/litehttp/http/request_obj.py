from cgi import FieldStorage


class Request:
    def __init__(self, response):
        self.response = response
        self.url = ''
        self.form: FormData = None
        self.url_arguments = {}

    def set_url_arguments(self, **kwargs):
        self.url_arguments.update(kwargs)

    def set_form_data(self, field_storage: FieldStorage):
        self.form = FormData(field_storage)

    def set_url(self, url: str):
        self.url = url


class FormData:
    def __init__(self, form_data):
        self.form_data: FieldStorage = form_data

    def get(self, key, default=None):
        return {'filename': self.form_data[key].filename, 'value': self.form_data.getvalue(key, default)}

    def get_value(self, key, default=None):
        return self.form_data.getvalue(key, default)

    def get_name(self, key):
        return self.form_data[key].filename

    def get_keys(self):
        return self.form_data.keys()
