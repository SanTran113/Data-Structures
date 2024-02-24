import random

List = ['Yes - def','Very doubtful', 'It is decided on']
int = random.randint(0, len(List) - 1)
q = input("Question: ")
print(q)
print("Magic 8 Ball")
# print(int)
print(List[int])