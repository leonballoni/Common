import regex as re
nums = list()
print(sum([int(num) for num in (re.findall('[0-9]+',(open("C:\\Users\\Pandinha\\Desktop\\Projects\\Python\\ReGeX\\test2.txt").read())))]))

"""
nums = []
file = open("C:\\Users\\Pandinha\\Desktop\\Projects\\Python\\ReGeX\\test1.txt")
for texts in file:
    text = re.findall('[0-9]+', texts)
    if len(text) != 0:
        for num in text:
            number = int(num)
            nums.append(number)
print(sum(nums))
"""
# result test1 : 445833
# result test2 : 369277
