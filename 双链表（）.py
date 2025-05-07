class DoublyListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

def createDoulblyLinkedList(arr: list[int]) -> DoublyListNode:
    if not arr:
        return None
    
    head = DoublyListNode(arr[0])
    cur = head

    # for 循环创建双链表
    for i in range(1,len(arr)):
        new_node = DoublyListNode(arr[i])
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next

    return head

# 双链表的查找修改
head = createDoulblyLinkedList([1, 2, 3, 4, 5])
tail = None

# 正向遍历所有节点
p = head
while p is not None:
    print(p.val)
    tail = p # 保证循环完成后记录末尾位置
    p = p.next
print("-------------------")
p = tail
while p is not None:
    print(p.val)
    p = p.prev
