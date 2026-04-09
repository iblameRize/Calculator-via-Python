#calculator By daddy ;0
print("'/' = division and '*' = Multification")

opa = input("use + or - or my dih or / or * :")

if opa in ["my dih", "dih","ma dih", "your dih", "yo dih",]:
    print("fuck You Diddy")
    opa = input("use + or - or / or * :")


value1 = float(input("enter your First value lil bro!:"))
value2 = float(input("enter your Second value lil bro!:"))

sol = F" count it your self lil bro: {value1}  {opa}  {value2}"

if opa == "+": realsol = value1 + value2
elif opa == "-": realsol = value1 - value2
elif opa == "*": realsol = value1 * value2
elif opa == "/": realsol = value1 / value2


print(sol)
answer = str(input("say Pls:"))
if answer in ["Pls","pls","please","Please"]:
    print(f"good boy Here Is Yo Answer: {realsol}")
elif answer == "my dih":
    print("fuck you Diddy")
else:
    print("fuck you you aint geting no answers")

