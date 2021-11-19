print("1st assignment\n")
def email_list(domains):
    emails = []
    for domain,users in domains.items():
        #print(domain,users)
        for user in users:
            emails.append(user + "@" + domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))



print("2st assignment\n")
def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            #user_groups[user] += group
            user_groups.setdefault(user, []).append(group)
    # Now add the group to the the list of
    # groups for this user, creating the entry
    # in the dictionary if necessary

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

print("3st assignment\n")
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
