import re

import requests

from gdshoplib.packages.renderer import ImageRenderer
from gdshoplib.packages.s3 import S3
from gdshoplib.services.notion.block import Block
from gdshoplib.services.notion.page import Page


class ProductMedia(Block):
    def __init__(self, *args, **kwargs):
        super(ProductMedia, self).__init__(*args, **kwargs)
        self.response = None
        self.s3 = S3(self)

    @property
    def url(self):
        return self[self.type]["file"]["url"]

    @property
    def badges(self):
        result = []
        for badge in self.parent.badges:
            if not badge.work or not badge.file:
                continue
            result.append(badge)
        return result

    @property
    def key(self):
        return self.notion.get_capture(self) or f"{self.type}_general"

    def fetch(self):
        self.access() or self.refresh()
        self.s3.get() or self.s3.put()

        return self.s3.get()

    def get_url(self, file_key=None):
        return f"{self.s3.s3_settings.ENDPOINT_URL}/{self.s3.s3_settings.BUCKET_NAME}/{file_key or self.file_key}"

    @property
    def file_key(self):
        return f"{self.parent.sku}.{self.id}.{self.format}"

    def access(self):
        return requests.get(self.url).ok

    def exists(self):
        return self.s3.exists()

    @property
    def name(self):
        pattern1 = re.compile(r".*\/(?P<name>.*)")
        r = re.findall(pattern1, self.url)
        if not r or not r[0]:
            return None
        return r[0].split("?")[0]

    @property
    def format(self):
        pattern = re.compile(r"\/.*\.(\w+)(\?|$)")
        r = re.findall(pattern, self.url)
        return r[0][0] if r else None

    def request(self):
        response = requests.get(self.url)
        if not response.ok:
            raise MediaContentException
        return response

    def get_content(func):
        def wrap(self, *args, **kwargs):
            if not self.response:
                if not self.access():
                    self.refresh()
                self.response = self.request()
            return func(self, *args, **kwargs)

        return wrap

    @property
    @get_content
    def content(self):
        return self.response.content

    @property
    @get_content
    def hash(self):
        return self.response.headers.get("x-amz-version-id")

    @property
    @get_content
    def mime(self):
        return self.response.headers.get("content-type")

    def get_badge_coordinates(self, badge):
        assert isinstance(badge, Page)
        result = [int(point.strip()) for point in badge.coordinates.split(",")]
        return result

    def get_size(self, badge):
        assert isinstance(badge, Page)
        result = [int(point.strip()) for point in badge.size.split(",")]
        return result

    def apply_badges(self):
        if self.type not in ("image",):
            return self

        result = ImageRenderer(self.content)
        for badge in self.badges:
            if not requests.get(badge.file).ok:
                badge.refresh()

            _badge = ImageRenderer(badge.file)
            if badge.size:
                _badge.resize(self.get_size(badge))
            if badge.transparency:
                _badge.set_transparency(badge.transparency)
            result.paste(_badge, self.get_badge_coordinates(badge))
        return result


class MediaContentException(Exception):
    ...
