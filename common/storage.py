from django.core.files.storage import Storage
from django.conf import settings

class MyStorage(Storage):
    """自定义文件存储类"""
    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content, max_length=None):
        pass

    def url(self, name):
        # name 就是图片的名字，
        return settings.QN_BASE_URL + name