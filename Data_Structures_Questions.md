Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1) because adding to end of queue doesn't require shifting elements
2. What is the runtime complexity of `dequeue`?
   O(n) because deleting start of queue requires shifting n-1 elements up
3. What is the runtime complexity of `len`?
   O(1) since len is internally updated as the list grows/shrinks

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   O(log(n)) because at each decision point half of search space is eliminated
2. What is the runtime complexity of `contains`?
   O(log(n)) same reason as above
3. What is the runtime complexity of `get_max`?
   O(log(n)) because one check per level

## Heap

1. What is the runtime complexity of `_bubble_up`?
   O(log(n)) because one check per level
2. What is the runtime complexity of `_sift_down`?
   O(log(n)) because one check per level
3. What is the runtime complexity of `insert`?
   O(log(n)) because it relies on bubble_up
4. What is the runtime complexity of `delete`?
   O(log(n)) because it relies sift_down
5. What is the runtime complexity of `get_max`?
   O(1) because it's the root_value

## Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`?
    O(1) because no iteration or recursion
2.  What is the runtime complexity of `ListNode.insert_before`?
    O(1) because no iteration or recursion
3.  What is the runtime complexity of `ListNode.delete`?
    O(1) because no iteration or recursion
4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(1) because no iteration or recursion
5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(1) because no iteration or recursion
6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(1) because no iteration or recursion
7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(1) because no iteration or recursion
8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    O(1) because no iteration or recursion
9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    O(1) because no iteration or recursion
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1) because no iteration or recursion

        a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
        Array.splice works as O(n) so DLL .delete() is better at O(1)
