from challenges.linked_list.linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):

        self._size = size
        self._buckets = size * [None]

    def _hash(self, key):

        sum = 0

        for char in key:
            sum += ord(char)

        primed = sum * 37
        index = primed % self._size
        return index

    def add(self, key, value):

        hash_index = self._hash(key)

        if not self._buckets[hash_index]:
            self._buckets[hash_index] = LinkedList()

        if self._buckets[hash_index].head:
            self._buckets[hash_index].append((key,value))
        else:
            self._buckets[hash_index].insert((key, value))

    def get(self, request):

        hash_index = self._hash(request)
        bucket = self._buckets[hash_index]
        if not bucket:
            return 'Null'
        current = bucket.head

        while current:
            pair = current.value
            key = pair[0]
            value = pair[1]

            if key == request:
                return value

            current = current.next_node

    def contains(self, request):

        hash_index = self._hash(request)
        bucket = self._buckets[hash_index]
        if bucket:
            return True
        else:
            return False
