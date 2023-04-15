class Post:
    def __init__(self, title:str, content: str) -> None:
        self.title = title
        self.content = content

    def __repr__(self):
        return f'Post({self.title}, {self.content})'

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }
