# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
Used Algorithm: Floyd’s Cycle-Finding Algorithm
Other solutions: Hashing Approach, Adding a flag to the data structure of linked list, Store length
"""
def findLoop(head):
	first_pointer = head
	second_pointer = head
    while(True):
		first_pointer = first_pointer.next
		second_pointer = second_pointer.next.next
		if first_pointer == second_pointer:
			first_pointer = head
			while(True):
				if  first_pointer == second_pointer:
					return first_pointer
				first_pointer = first_pointer.next
				second_pointer = second_pointer.next
