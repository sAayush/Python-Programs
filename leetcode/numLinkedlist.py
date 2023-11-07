class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy_head = ListNode(-1)
    current = dummy_head

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Append any remaining nodes from list1 or list2
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy_head.next

# Create the linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge the lists
merged_list = mergeTwoLists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
