class Solution(object):
    import re
    def isPalindrome(self, s):
        st = re.sub(r'[^a-zA-Z0-9]', '', s)
        if st.lower()==st[::-1].lower():
            return True
        else:
            return False