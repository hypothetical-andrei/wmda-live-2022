class MyClass():
    def __init__(self, content):
        self.content = content
    def print_me(self):
        print('my content is ' + self.content)

o = MyClass('some content')
o.print_me()
