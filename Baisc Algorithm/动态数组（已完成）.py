class MyArrayList:
    
    #初始化数组容量
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        if init_capacity==None:
            self.data = [None] * self.__class__.INIT_CAP
        else:
            self.data = [None] * init_capacity
        self.size = 0

    #工具方法
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    # 扩充数组并迁移数据
    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(0, self.size):
            temp[i] = self.data[i]
        self.data = temp
    
    def is_element_index(self, index):
        return 0 <= index < self.size
    
    def is_position_index(self, index):
        return 0 <= index <= self.size
    
    def _check_element_index(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
    
    def _check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
        
    def display(self):
        print(f"Size = {self.size}, Capcity = {len(self.data)}")
        print(self.data)

    # 查 时间复杂度为O(1) (根据元素值查找索引 时间复杂度为O(N))
    def get(self, index):
        # 检查索引是否越界
        self._check_element_index(index)
        return self.data[index]
    
    # 改 时间复杂度为O(1)
    def set(self, index, element):
        # 检查索引是否越界
        self._check_element_index(index)
        # 对数据进行修改
        old_val = self.data[index]
        self.data[index] = element
        return old_val
    
    # 末位增 时间复杂度为O(1)
    def add_last(self, element):
        # 检查数组容量并扩容（达到上限后扩容1倍）
        cap = len(self.data)
        if self.size == cap:
            self._resize(cap * 2)
        self.data[self.size] = element
        self.size = self.size + 1

    # 增 时间复杂度为O(N)
    def add(self, index, element):
        # 检查索引是否越界
        self._check_position_index(index)
        # 检查数组容量并扩容（达到上限后扩容1倍）
        cap = len(self.data)
        if cap == self.size:
            self._resize(self.size * 2)
        # 为数组进行移位
        for i in range(self.size-1, index-1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index] = element
        self.size = self.size + 1

    # 末位删
    def remove_last(self):
        # 检查数组是否为空
        if self.size == 0:
            raise Exception("No elements in the array")
        # 检查数组容量并缩容（达到容量的1/4后缩容一半）
        cap = len(self.data)
        if self.size == cap // 4:
            self._resize(cap // 2)
        
        deleted_val = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size = self.size - 1

        return deleted_val
    
    # 删
    def remove(self, index):
        # 检查数组是否为空
        if self.size == 0:
            raise Exception("No elements in the array")
        # 检查索引是否越界
        self._check_element_index(index)
        # 检查数组容量并缩容（达到容量的1/4后缩容一半）
        cap = len(self.data)
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_val = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size = self.size - 1

        return deleted_val
    
    def add_first(self,element):
        self.add(0,element)

# Usage example
if __name__ == "__main__":
    arr = MyArrayList(init_capacity=3)

    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)

    arr.remove(3)
    arr.add(1, 9)
    arr.add_first(100)
    val = arr.remove_last()
    arr.set(3,200)

    # 100 1 9 2 3
    for i in range(arr.get_size()):
        print(arr.get(i))

    