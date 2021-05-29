#1
리스트 = ["A", "b", "c", "D"]

for char in 리스트:
  if char.isupper() != True:
    print(char)

#2
리스트 = ["A", "b", "c", "D"]

for char in 리스트:
  if not char.isupper():
    print(char)