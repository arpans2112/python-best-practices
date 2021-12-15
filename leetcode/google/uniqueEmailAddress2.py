'''
184 / 184 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 13.9 MB
Submitted: 0 minutes ago

Memory Usage is reduced when created one less variable.
184 / 184 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 13.6 MB

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
            index = local_name.find("+")
            if index != -1:
                valid_local_name = local_name[:index]
                valid_local_name = valid_local_name.replace(".", "")
            else:
                valid_local_name = local_name.replace(".", "")

            unique_emails.add(valid_local_name + '@' + domain_name)

        return len(unique_emails)

