# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def hashFunc(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key) % self.capacity

    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass

    # def _hash_mod(self, key):
    #     '''
    #     Take an arbitrary key and return a valid integer index
    #     within the storage capacity of the hash table.
    #     '''
    #     return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        index = self.hashFunc(key)
        node = self.storage[index]
        if node is None:
            self.size += 1
            self.storage[index] = LinkedPair(key, value)
            return
        prev = node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            prev.next = LinkedPair(key, value)
        else:
            node.value = value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self.hashFunc(key)
        node = self.storage[index]

        while node is not None and node.key != key:
            # prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if node.next is None:
                node.value = None
            else:
                # prev.next = prev.next.next
                node.value = None
            return result

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self.hashFunc(key)
        node = self.storage[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        self.capacity *= 2
        temp_storage = self.storage
        self.storage = [None]*self.capacity
        for i in temp_storage:
            while i is not None:
                self.insert(i.key, i.value)
                i = i.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
