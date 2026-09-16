class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            str_len_lst = []
            encoded = ''
            for string in strs:
                str_len_lst.append(len(string))
            for length in str_len_lst:
                encoded += str(length) + ','
            encoded += '#' + "".join(strs)
            return encoded
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        else:
            decoded = []
            hashtag = s.find('#')
            pre_hash = s[:hashtag-1].split(',')
            post_hash = s[hashtag+1:]
            idx = 0
            for i in range(len(pre_hash)):
                word = post_hash[idx:(idx+int(pre_hash[i]))]
                idx += int(pre_hash[i])
                decoded.append(str(word))
            return decoded


