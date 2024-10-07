class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for char in s:
            if char == 'B':
                if len(st)>0 and st[-1] == 'A':
                    st.pop()               
                    continue
            if char == 'D':
                if len(st)>0 and st[-1] == 'C':
                    st.pop()               
                    continue
            st.append(char)
        return len(st)
