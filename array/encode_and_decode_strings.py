"""
https://leetcode.com/problems/encode-and-decode-strings/


Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

class Solution:

    def encode(self, strs: list[str]) -> str:
        delimiter = '|'
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}{delimiter}{s}'
        return encoded

    def decode(self, encoded: str) -> list[str]:
        delimiter = '|'
        strs = []
        cur_str = ''
        cur_count = ''
        i = 0

        while i < len(encoded):
            c = encoded[i]
            if c == delimiter:
                i += 1
                count = int(cur_count) + i
                while i < count:
                    cur_str += encoded[i]
                    i += 1
                strs.append(cur_str)
                cur_str = ''
                cur_count = ''
            else:
                cur_count += c
                i += 1
        return strs
