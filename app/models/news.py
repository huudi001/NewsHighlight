class News:
    def __init__(self,source,author,title,description,url,url_to_image,published_at):

        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = 'https://newsapi.org//t/p/w500'+url_to_image
        self.published_at = published_at
cvfvf
