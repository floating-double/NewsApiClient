import json


class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()


class News(JsonSerializable):
    def __init__(self, title, source, author, description, url, urlToImage, publishedAt, content):
        self.title = title
        self.source = source
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    def __repr__(self):
        return json.dumps(self.__dict__)

    def to_json(self):
        return {'title': self.title,
                'source': self.source,
                'author': self.author,
                'description': self.description,
                'url': self.url,
                'urlToImage': self.urlToImage,
                'publishedAt': self.publishedAt,
                'content': self.content}
