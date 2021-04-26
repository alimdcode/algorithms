""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. """
class TwoSums:
    def __init__(self):
        pass

    def get_two_sum_indexes(self, elements, target):
        elements_map = dict()
        for index, element in enumerate(elements):
            other_part = target - element
            if elements_map.get(other_part) is not None:
                return (elements_map.get(other_part), index)
            else:
                elements_map[element] = target
        return -1

if __name__ == '__main__':
    elements = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    two_sums = TwoSums()
    target = int(input("Please Enter the Target"))
    indexes = two_sums.get_two_sum_indexes(elements, target)
    print(f'indexes for the target {target} are {indexes}')
