from datetime import datetime

from pydantic import BaseModel, Field

from typing import Optional


class Article(BaseModel):
    id: str = Field(..., alias="uuid")
    url: str = Field(..., alias='url')
    domain: str = Field(..., alias='domain')
    title: str = Field(..., alias='title')
    category: str = Field(..., alias='category')
    category_url: str = Field(..., alias='category_url')
    time: datetime = Field(..., alias='time')
    content: str = Field(..., alias='content')
    img_urls: Optional[str] = Field(alias='img_urls', default=None)


class ArticleShow(BaseModel):
    id: str
    url: str
    domain: str
    title: str
    category: str
    time: datetime
    content: str
    img_urls: Optional[str]
