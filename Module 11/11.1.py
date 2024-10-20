class Publication:
    
    def __init__(self,name):
        self.name = name

    def print_information(self):
        print(f"Name = {self.name}")

class Book(Publication):
    
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)
    
    def print_information(self):
        print(f"Name = {self.name}; Author = {self.author} and page number = {self.page_count}")

class Magzine(Publication):
    
    def __init__(self,name,chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)
    
    def print_information(self):
        print(f"Name = {self.name}; Chief editor = {self.chief_editor}")

magazine = Magzine('Donald Duck','Aki Hyyppä')
book = Book('Compartment No. 6','Rosa Liksom', 192)
magazine.print_information()
book.print_information() 