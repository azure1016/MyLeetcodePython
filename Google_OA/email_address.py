class EmailParser:
    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split("+")[0].replace(".", "")
            result.add(local+'@'+domain)

        return len(result)

sol = EmailParser()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
res = sol.numUniqueEmails(emails)
print(res)

