class LinkedList():
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def LL_insert(self, new_list):
        if self.next is None:  
            self.next = new_list
        else:
            self.next.LL_insert(new_list) 

    def LL_search(self, x):
        if(x == self.item):
            return self
        
        if self.next == None:
            return None
        
        return self.LL_search(self.next)
        
    def LL_print(self):
        print(self.item)
        
        if self.next is not None:
            self.next.LL_print()
        


if __name__ == '__main__':
    head = LinkedList(5)
    second = LinkedList(4)

    head.LL_insert(second)
    head.LL_print()


