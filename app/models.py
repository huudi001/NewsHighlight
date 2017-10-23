class Article:
    #class that defines news objects
    def __init__(self,author,title,description,url,urlToImage,published_at):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage =  urlToImage
        self.published_at = published_at
class Source:
    def __init__(self,id,name, description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
