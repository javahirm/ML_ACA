def quantity_of_emails(emails):
    local = [i[:i.index("@")] for i in emails]
    domain = [i[i.index("@"):] for i in emails]
    correct_local = []
    for mail in local:
        if "." in mail:
            mail = mail.replace(".", "")
        if "+" in mail:
            mail = mail[:mail.index("+")]
        correct_local.append(mail)
    i = 0
    all_emails = []
    while i < len(correct_local):
        all_emails.append(correct_local[i] + domain[i])
        i += 1
    all_emails = set(all_emails)
    return len(all_emails)


emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]

print(quantity_of_emails(emails))
