class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        for a in self.posts:
            print(a)
h=SocialMediaProfile("'johndoe")
h.add_post('Hello, world!')
h.add_post('Had a great day at the park!')
h.add_post('What\'s up, Natalie? How are you?')



