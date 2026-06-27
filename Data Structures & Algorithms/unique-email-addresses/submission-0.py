class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for i in emails:
            name, domain = i.split('@') 
            real = name.split('+')[0].replace('.', '')
            seen.add(real + '@' + domain)
        return len(seen)