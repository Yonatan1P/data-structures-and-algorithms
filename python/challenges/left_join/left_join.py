from challenges.hashtable.hashtable import Hashtable

def left_join(hashmap1, hashmap2):
    output = [ ]
    # print(print.__dir__())
    for bucket in hashmap1._buckets:
        if bucket:
            current_output =[]
            current_node = bucket.head
            while current_node:
                key = current_node.value[0]
                value = current_node.value[1]
                current_output += [key, value]
                if hashmap2.contains(key):
                    current_output += [hashmap2.get(key)]
                else:
                    current_output += ['Null']
                output += [current_output]
                current_node = current_node.next_node
    return output
