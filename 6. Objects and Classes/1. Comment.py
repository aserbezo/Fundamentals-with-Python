class Comment: # tova e shablona ili template
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book") # tova e obeckta , instancii
print(comment.username)
print(comment.content)
print(comment.likes)
