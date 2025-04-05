class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
        keyingi = None
        boshi = head

        while boshi: # 1-> 2
            keyingi_node = keyingi # none-> 1
            keyingi = boshi # 1-> 2
            boshi = boshi.next # 2-> 3
            keyingi.next = keyingi_node # 1 -> 2 
        return keyingi

def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Natijani chiroyli chiqarish uchun
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# === Test ===
nums = [1, 2, 3, 4, 5]
head = to_linked_list(nums)  # LinkedList yaratish
reversed_head = reverseList(head)  # Reversing
print_linked_list(reversed_head)  # Natijani chiqarish