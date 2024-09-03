sports = ["soccer", "baseball", "basketball", "hockey"]
sports.append("baseball")
cnt = sports.count("baseball")
print("Count: " + str(cnt))

sports2 = sports.copy()
sports2.clear()
sports2.append("rugby")
sports.extend(sports2)
print(sports)

insert = sports.insert(4, "golf")
indx = sports.index("golf")
print(indx)


sports.pop()
sports.remove("baseball")
sports.reverse()
print("Reversed: " + str(sports))
sports.sort()
print("Sorted: " + str(sports))