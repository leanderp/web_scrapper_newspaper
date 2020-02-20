from sqlalchemy import Integer, String, Column

from base import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(String, primary_key=True)
    body = Column(String)
    host = Column(String)
    title = Column(String)
    newspaper_uid = Column(String)
    n_tokens_body = Column(Integer)
    n_tokens_title = Column(Integer)
    url = Column(String, unique=True)

    def __init__(self, uid, body, title, url, newspaper_uid, host, n_tokens_title, n_tokens_body):
        self.id = uid
        self.body = body
        self.title = title
        self.url = url
        self.newspaper_uid = newspaper_uid
        self.host = host
        self.n_tokens_title = n_tokens_title
        self.n_tokens_body = n_tokens_body
        

