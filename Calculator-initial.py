Eqn = input("Give input: ")
Eqn_0 = list(Eqn.split("**"))
Eqn_1 = list(Eqn.split("/"))
Eqn_2 = list(Eqn.split("*"))
Eqn_3 = list(Eqn.split("+"))
Eqn_4 = list(Eqn.split("-"))
def calculator(N):
    if len(Eqn_0) == 2:
        result = float(Eqn_0[0])**float(Eqn_0[1])
    elif len(Eqn_1) == 2:
        result = float(Eqn_1[0])/float(Eqn_1[1])
    elif len(Eqn_2) == 2:
        result = float(Eqn_2[0])*float(Eqn_2[1])
    elif len(Eqn_3) == 2:
        result = float(Eqn_3[0])+float(Eqn_3[1])
    elif len(Eqn_4) == 2:
        result = float(Eqn_4[0])-float(Eqn_4[1])
    return result

print(calculator(Eqn))