tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\n on a line"
backlash_cat = "I'm \\ a \\ cat."
formatter = "{} {} {}"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip
\t* Grass
'''
print(tabby_cat.format('fat_cat'))
print(persian_cat)
print(backlash_cat)
print(fat_cat)
print(formatter.format(tabby_cat,persian_cat,\nbacklash_cat))