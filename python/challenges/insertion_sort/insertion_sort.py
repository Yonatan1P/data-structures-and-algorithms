def insertion_sort(list):
    for index in range(1, len(list)):
        index_position = index
        temporary_position = list[index]

        while index_position > 0 and temporary_position < list[index_position - 1]:
            list[index_position] = list[index_position - 1]
            index_position -= 1
        list[index_position] = temporary_position
    return list

    # arr_length = len(array)

    # for i in range(1, arr_length):

    #     temp_index = i
    #     current_position = array[temp_index]

    #     while temp_index > 0 and current_position < array[temp_index - 1]:
    #         array[i] = array[temp_index - 1]
    #         temp_index -= 1
    #     array[temp_index] = current_position

    # return array



