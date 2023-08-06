from typing import List

from pydantic import BaseModel

from gdshoplib.apps.platforms.base import Platform
from gdshoplib.packages.feed import Feed


class VKProductModel(BaseModel):
    ...


class VKManager(Platform, Feed):
    DESCRIPTION_TEMPLATE = "vk.txt"
    KEY = "VK"

    # def get_products(self) -> List[VKProductModel]:
    #     ...

    # def push_feed(self):
    #     # Обновить товары в VK
    #     ...
