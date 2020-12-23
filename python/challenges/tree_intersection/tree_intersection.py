from challenges.hashtable.hashtable import Hashtable

def find_intersection(tree1,tree2):
    answer = list()
    temp_table = Hashtable()
    current1 = tree1.root

    def first_walk(current1):
        if not current1:
            return
        temp_table.add(f'random hashing data {current1.value}', current1.value)
        first_walk(current1.left)
        first_walk(current1.right)
    first_walk(current1)

    current2 = tree2.root

    def second_walk(current2, current_answer):
        if not current2:
            return
        if temp_table.contains(f'random hashing data {current2.value}'):
            current_answer += [current2.value]
        second_walk(current2.left, current_answer)
        second_walk(current2.right, current_answer)

    second_walk(current2, answer)
    return answer

