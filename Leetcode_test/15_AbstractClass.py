from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(self):pass


class MyBook(Book):
    price = 0
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title,author)
        #ps:上面那句和下面注释的句子意义相同，注意super内Book和MyBook的区别
        #super(Book, self).__init__()
        self.price = price

    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()