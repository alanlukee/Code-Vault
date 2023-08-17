class Solution(object):
    def validIPAddress(self, queryIP):
        ipv4 = queryIP.split('.')
        ipv6 = queryIP.split(':')
        flag4 = False
        flag6 = False
        
        if len(ipv4) == 4:
            flag4 = True
            for i in ipv4:
                if not (i.isdigit() and 0 <= int(i) <= 255 and str(int(i)) == i):
                    flag4 = False
                    break
        elif len(ipv6) == 8:
            if "" in ipv6:
                return "Neither"
            flag6 = True
            for char in ipv6:
                if len(char) > 4 or not all(c.isdigit() or ('a' <= c <= 'f') or ('A' <= c <= 'F') for c in char):
                    flag6 = False
                    break

        if flag4:
            return "IPv4"
        elif flag6:
            return "IPv6"
        else:
            return "Neither"