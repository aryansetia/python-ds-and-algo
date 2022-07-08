
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0: 
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index > self.length:
            return None 
        temp = self.head