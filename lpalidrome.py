"""Given a string s, return the longest palindromic substring in s"""

class LongestPalindrome:
    def __init__(self):
        pass

    def get_longest_palindrome_sub(self, string):
        if len(string) < 1:
            return string

        self.max_palindrome_len = 0
        self.max_palindrome_string = ''
        index = 0
        while index < len(string)-1:
            self.get_expanded(string, index, index)
            self.get_expanded(string, index, index+1)
            index += 1

        return self.max_palindrome_string

    def get_expanded(self, string, start, end):

        while start >= 0 and end < len(string) and string[start] == string[end]:
            # self.max_palindrome_len = max(palindrome_len, end-start+1)
            start -= 1
            end += 1
        cur_len = end - start -1
        if cur_len > self.max_palindrome_len:
            self.max_palindrome_len = max(cur_len, self.max_palindrome_len)
            self.max_palindrome_string = string[start+1: start+1+self.max_palindrome_len]


if __name__ == '__main__':
    l_palindrome = LongestPalindrome()
    string = input('Enter the String: ')
    l_substring = l_palindrome.get_longest_palindrome_sub(string)
    print(f'Longest palidrome sub: {l_substring}')


