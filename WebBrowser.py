from LinkedList import Linked_List

#methods of necessary commands
class Web_Browser:

#initalizes linked list, uses position to keep track of which website is being looked at
    def __init__(self):
        self.linkedlist = Linked_List()
        self.position = 0

#adds on websites to linked list and removes websites from list if current website is before other websites
    def navigate_to(self, url):
        if self.position < self.linkedlist.length():
            for i in range(self.linkedlist.length()-1, self.position-1, -1):
                self.linkedlist.remove(i)
        self.linkedlist.insert(self.position, url)
        self.position +=1

#moves position of website forward by one and ensure position does not go past length of linked list
    def forward(self):
        self.position +=1
        if self.position > self.linkedlist.length():
            self.position = self.linkedlist.length()

#backwards in website location relative to linked list
    def back(self):
        self.position -=1
        if self.position <1:
            self.position =1

#Prints linked list and where user is at in the websites they are looking at
    def history(self):
        print(f"Oldest\n========")
        count = 0
        for i in range(self.linkedlist.length()):
            if count == self.position-1:
                print(f"<{self.linkedlist.get_entry(i)}>  <==current")
            else:
                print(f"<{self.linkedlist.get_entry(i)}>")
            count+=1
        print("========\nNewest")