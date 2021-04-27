class LongestCommonSub:
    def __init__(self):
        pass

    def get_max_common_sub(self, str_one, str_two):
        self.memoize = dict()
        max_len = self.get_max_common_len(str_one, str_two, 0, 0)
        print(self.memoize)
        return max_len



    def get_max_common_len(self, str_one, str_two, index_one, index_two):
        if index_one >= len(str_one) or index_two >= len(str_two):
            return 0
        if str_one[index_one] == str_two[index_two]:
            if self.memoize.get((index_one, index_two)) is None:
                self.memoize[(index_one, index_two)] = 1 + self.get_max_common_len(str_one, str_two, index_one+1, index_two+1)

            return self.memoize.get((index_one, index_two))


        self.memoize[(index_one, index_two)] =  max(self.get_max_common_len(str_one, str_two, index_one+1, index_two), self.get_max_common_len(str_one, str_two, index_one, index_two+1))
        return self.memoize.get((index_one, index_two))


if __name__ == '__main__':
    l_common_sub = LongestCommonSub()
    str_one = input('Enter String One: ')
    str_two = input('Enter String Two: ')
    max_len = l_common_sub.get_max_common_sub(str_one, str_two)
    print(f'max len is {max_len}')
