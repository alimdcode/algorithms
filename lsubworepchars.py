"""Given a string s, find the length of the longest substring without repeating characters."""
class LongestSubstring:
    def __init__(self):
        pass

    def get_lsub_wo_rep_chars(self, string):
        if len(string) <= 1:
            return len(string)
        start = 0
        end = 0
        max_len = 1
        char_index = dict()
        while end < len(string):
            # print(start, end)
            if start == end:
                char_index[string[start]] = start
                end += 1
            elif char_index.get(string[end]) is None or char_index.get(string[end]) < start:
                max_len = max(max_len, end-start+1)
                char_index[string[end]] = end
                end += 1
            else:
                start += 1
                char_index[string[end]] = end

        return max_len


if __name__ == '__main__':
    string = input('Please Enter the String: ')
    longest_sub = LongestSubstring()
    max_len_sub = longest_sub.get_lsub_wo_rep_chars(string)
    print(f'Length of longest substring is: {max_len_sub}')



