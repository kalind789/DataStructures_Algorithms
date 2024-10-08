class LinkedList():

    def __init__(self, item):
        self.item = item
        self.next = None
    
    def LL_insert(self, new_list):
        self.next = new_list

    def LL_search(self, x):
        if self == None:
            return None
        
        if(x == self.item):
            return self
        else:
            return self.LL_search(self.next)
        
    def LL_print(self):
        if self == None:
            return None
        else:
            print(self.item)
            return self.LL_print(self.next)
        


if __name__ == '__main__':
    head = LinkedList(5)
    second = LinkedList(4)

    head.LL_insert(second)
    head.LL_print()


