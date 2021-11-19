toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc['Epilogue'] = 39 # Epilogue starts on page 39
toc['Chapter 3'] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
if 'Chapter 5' in toc:
    print('True')
else:
    print('False') # Is there a Chapter 5?

print("")
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
del wardrobe["jeans"]
wardrobe["boots"] = ["black", "white"]
for k,v in wardrobe.items():
    #print(k,v)
    for color in v:
        #print(color)
        print("{} {}".format(k,color))
print(wardrobe.get("boots",0))#dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
garbage = {"papers":["archives","newspapers"], "garbage":["dust","cs"]}
wardrobe.update(garbage)
print(wardrobe)
del wardrobe["garbage"]
print(wardrobe)
