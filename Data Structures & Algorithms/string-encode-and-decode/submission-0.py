class Solution:

    def encode(self, strs: List[str]) -> str:
        # putting the length of each sting part in front of it. 
        encoded_string = ""
        
        for s in strs:
            l = len(s)
            encoded_string += str(l) + "#" + s

        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i=0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            print(word)
            decoded_strs.append(word)
            i = j+1+length
        return decoded_strs;