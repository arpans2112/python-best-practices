'''
184 / 184 test cases passed.
Status: Accepted
Runtime: 52 ms
Memory Usage: 13.7 MB
Submitted: 0 minutes ago
'''

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()

        for email in emails:
            components = email.split('@')
            local_name = components[0]
            domain_name = components[1]
            valid_email = ""
            for c in local_name:
                if c != '.':
                    if c != '+':
                        valid_email += c
                    else:
                        break
            unique_emails.add(valid_email + '@' + domain_name)

        return len(unique_emails)

