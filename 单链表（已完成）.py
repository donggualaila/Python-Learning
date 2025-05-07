class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
# 输入一个数组，转化为一条单链表
def createLinkedList(arr: list[int]) -> 'ListNode':
    if arr == None or len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head 

    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

# 在单链表访问每一个节点并返回数值 
head = createLinkedList([1, 2, 3, 4, 5])

p = head
while p is not None:
    print(p.val)
    p = p.next
print("----------------------")

# 在单链表头部插入新元素
head = createLinkedList([1, 2, 3, 4, 5])
newNode = ListNode(0)
newNode.next = head
head = newNode
# head 变为 0 -> 1 -> 2 -> 3 -> 4 -> 5

# 在单链表尾部插入新元素
head = createLinkedList([1, 2, 3, 4, 5])
p = head
while p.next is not None: 
    p = p.next # 先走到链表的最后一个节点
p.next = ListNode(6) #在最后一个节点之后加入新节点6
head = p
# head 变为 1 -> 2 -> 3 -> 4 -> 5 -> 6

# 在单链表中间插入新元素
# 在第3个节点后面插入一个新节点66
head = createLinkedList([1, 2, 3, 4, 5])
p = head
for _ in range(2):
    p = p.next
# 组装新节点的后驱指针
newNode = ListNode(66)
newNode.next = p.next
p.next = newNode
head = p
# head 变为 1 -> 2 -> 3 -> 66 -> 4 -> 5

# 在单链表删除任意一个节点
head = createLinkedList([1, 2, 3, 4, 5])
# 删除第4个节点，调整前驱节点
p = head
for i in range(2):
    p = p.next
p.next = p.next.next
head = p
# head 变为 1 -> 2 -> 3 -> 5

# 在单链表删除末尾节点
head = createLinkedList([1, 2, 3, 4, 5])
p = head
while p.next.next is not None:
    p = p.next
p.next = None
head = p
# head 变为 1 -> 2 -> 3 -> 4

# 在单链表删除头部节点
head = createLinkedList([1, 2, 3, 4, 5])
head = head.next
# head 变为 2 -> 3 -> 4 -> 5
