import io
from pathlib import PosixPath

import requests
import validators
from PIL import Image


class ImageRenderer:
    # TODO: Если это не изображение
    # TODO: Проверка формата
    # TODO: Проверка размера

    def __init__(self, content):
        self.read_content(content)

    @classmethod
    def new(cls, size, color=(255, 255, 255, 0)):
        image = Image.new("RGBA", size, color=color)
        return cls(image)

    @property
    def info(self):
        return {
            "format": self.image.format,
            "size": self.image.size,
            "mode": self.image.mode,
            "mime": self.image.get_format_mimetype(),
        }

    def read_content(self, content):
        if isinstance(content, str) and validators.url(content):
            self.image = Image.open(io.BytesIO(requests.get(content).content))
        elif isinstance(content, str) or isinstance(content, PosixPath):
            self.image = Image.open(content)
        elif isinstance(content, io.BufferedReader):
            self.image = Image.open(content)
        elif isinstance(content, bytes):
            self.image = Image.open(io.BytesIO(content))
        elif isinstance(content, Image.Image):
            self.image = content

        if not self.image:
            return

        if self.image.format != "PNG" or self.image.mode != "RGBA":
            self.convert()

    def set_transparency(self, transparency=127):
        assert self.image.mode == "RGBA", "Изображение не в RGBA"
        self.image.putalpha(transparency)

    def paste(self, im2, position=(0, 0)):
        assert isinstance(
            im2, self.__class__
        ), f"Объект долженн быть класса {self.__class__.__name__}"
        self.image.paste(im2.image, position, im2.image)

    @property
    def content(self):
        with io.BytesIO() as f:
            self.image.save(f, format=self.image.format, quality=100, subsampling=0)
            return f.getvalue()

    def resize(self, size):
        self.image.thumbnail(size)

    def convert(self, format="PNG"):
        with io.BytesIO() as f:
            self.image = self.image.convert("RGBA")
            self.image.save(f, format=format, quality=100, subsampling=0)
            self.read_content(f.getvalue())
