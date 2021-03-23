class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def insert_at_the_beginning(self, data):
        if self._head == None:
            self._head = Node(data)
            return
        temp_n = Node(data)
        temp_n._next = self._head
        self._head = temp_n

    def insert_after(self, prev, data):
        if self._head == None:
            print('list is empty.')
            return
        temp_n = self._head
        while (temp_n != None):
            if temp_n._data == prev:
                new_node = Node(data)
                post_node = temp_n._next
                temp_n._next = new_node
                new_node._next = post_node
                return
            temp_n = temp_n._next
        print('there\'s no node exist with data {} to insert after it.'.format(prev))

    def insert_at_the_end(self, data):
        if self._head == None:
            self._head = Node(data)
            return
        temp_n = self._head
        while(temp_n._next != None):
            temp_n = temp_n._next
        temp_n._next = Node(data)

    def print_list_asc(self):
        if self._head == None:
            print('list is empty.')
            return
        temp_n = self._head
        while (temp_n != None):
            print(temp_n._data)
            temp_n = temp_n._next

    def print_list_desc(self):
        pass

    def delete_node_by_value(self, data):
        temp_n = self._head

        if self._head == None:
            print('list is empty.')
            return

        if temp_n._data == data:
            self._head = self._head._next
            return

        while (temp_n._next != None):
            if temp_n._next._data == data:
                break
            temp_n = temp_n._next

        if temp_n._next == None:
            print('data not present in the list.')
            return
        else:
            pre_node = temp_n
            post_node = temp_n._next._next
            pre_node._next = post_node

    def delete_node_by_position(self, pos):
        temp_n = self._head

        if self._head == None:
            print('list is empty.')
            return

        if pos == 0:
            self._head = self._head._next
            return

        _index = 0
        while (temp_n._next != None):
            if pos == _index-1:
                break
            _index += 1
            temp_n = temp_n._next

        if temp_n.next == None:
            print('position is out of range.')
            return
        else:
            pre_node = temp_n
            post_node = temp_n._next._next
            pre_node._next = post_node
    
    def reverse_the_list(self):
        _current = self._head
        _prev = None
        while _current != None:
            _next = _current._next
            _current._next = _prev
            _prev = _current
            _current = _next
        self._head = _prev

if __name__ == '__main__':
    _linked_list = SinglyLinkedList()
    _linked_list.insert_at_the_beginning(10)
    _linked_list.insert_at_the_end(20)
    _linked_list.insert_at_the_end(35)
    _linked_list.insert_at_the_end(58)
    _linked_list.insert_at_the_end(73)
    _linked_list.insert_at_the_end(99)
    _linked_list.insert_after(20, 88)
    _linked_list.print_list_asc()
    print('----------------------')
    _linked_list.delete_node_by_value(88)
    _linked_list.delete_node_by_position(0)
    _linked_list.print_list_asc()
    _linked_list.reverse_the_list()
    print('----------------------')
    _linked_list.print_list_asc()
