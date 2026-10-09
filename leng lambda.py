strings = ["python","c","java","programming","ai"]
print("original list:")
print(strings)
strings.sort(key=lambda x: len(x))
print("sorted by length:")
print(strings)
