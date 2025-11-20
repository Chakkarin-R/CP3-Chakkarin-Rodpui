LB = int(input())
for x in range(LB):
    text = " "
    py = text*(LB-x) + "* "*(x+1) + text*x
    print(py)