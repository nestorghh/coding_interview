def numberUnique(emails):
    res=set()
    for e in emails:
        name, domain = e.split('@')

        if '+' in name:
            name = name[:name.index('+')]

        res.add(name.replace('.','')+'@'+domain)

    return res

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]


