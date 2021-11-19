mailsdict = {}
mail = "rshams@mail.ru"
mailsdict[mail] = mailsdict.get(mail, 0) + 1
print(mailsdict)
mailsdict[mail] = mailsdict.get(mail, 0) + 1
print(mailsdict)
