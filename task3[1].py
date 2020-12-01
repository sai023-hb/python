# Task3
# 1
x = {" Elakiya ": 20, " Krithiga ": 20, " Rohini ": 20}
y = {"Elakiya": 20, "Krithiga": 20}
z = x.copy()
for key, value in y.items():
    z[key] = value
print(z)
# 2
y.pop("Elakiya")  # Removes the specified key
x.popitem()  # Removes the last inserted item
print(x)
print(y)
# 3
Laptop = {"hp", "dell"}
Colour = {" silver", "black"}
new_dic = dict(zip(Laptop, Colour))
print(new_dic)
# 4
a={"cakes" ,"chocolate" ,"panipuri"}
print(len(a))
# 5
b={"chocolate"}
print(a-b)
