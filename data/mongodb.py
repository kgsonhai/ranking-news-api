from datetime import datetime, timedelta, timezone

from pymongo import MongoClient
from settings import BaseConfig as Conf
from models.articles import Article


class MongoDB:
    myclient = MongoClient(Conf.MONGO_URI)
    mydb = myclient[Conf.MONGO_DATABASE]
    mycol = mydb[Conf.MONGO_COLLECTION]
    time = (datetime.now() - timedelta(days=1)).replace(hour=17,
                                                        minute=0, second=0, microsecond=0)

    # time = datetime.now().replace(
    #     day=datetime.now().day - 1, hour=17, minute=0, second=0)

    iso_date_string = (datetime.now() - timedelta(days=1)).replace(hour=17,
                                                                   minute=0, second=0, microsecond=0).strftime(
        '%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+00:00'

    def get_articles_by_category(self, category: str):
        query = {"category": category, "time": {
            "$gt": datetime.fromisoformat(self.iso_date_string)}}
        articles = self.mycol.find(query)
        response = []
        try:
            for item in articles:
                response.append(Article(**item))
        except (Exception,) as ex:
            print(f'Error append article: {ex}')
        return response

    def get_articles_by_domain(self, domain: str):
        query = {"domain": domain, "time": {"$gt": self.time}}

        articles = self.mycol.find(query)
        response = []
        for item in articles:
            response.append(Article(**item))
        return response

    def get_articles_by_domain_category(self, domain: str, category: str):
        query = {"domain": domain, "category": category,
                 "time": {"$gt": self.time}}

        articles = self.mycol.find(query)
        response = []
        for item in articles:
            response.append(Article(**item))
        return response

    def get_article_by_url(self, url: str):
        query = {"url": {"$regex": url}}
        return Article(**self.mycol.find_one(query))

    def get_article_by_uuid(self, uuid: str):
        query = {"uuid": uuid}
        return Article(**self.mycol.find_one(query))


if __name__ == '__main__':
    # data = MongoDB().get_articles_by_category(category="the-thao")
    # data = MongoDB().get_articles_by_domain(domain="vnexpress")
    # data = MongoDB().get_articles_by_domain_category(domain="vnexpress", category="chinh-tri")
    # data = MongoDB().get_articles_by_url(url='1370159.html')
    data = MongoDB().get_article_by_uuid('076c804a-c0ee-5e0d-9811-119a2d9a18ed')
    print(data)
    # if data is None:
    #     print("None")
    # else:
    #     print(len(data))
    #     for i in data:
    #         print(i)
