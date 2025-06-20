
def goodTentativas(string, char, tamanho):

    if (tamanho == 1):
        return 0 if string == char else 1
    
    else:
        q = tamanho//2

        left = string[:q]
        rigth = string[q:]

        custoLeft = 0
        custoRight = 0

        for i in left:
            if (i != char):
                custoLeft = custoLeft + 1

        for j in rigth:
            if (j != char):
                custoRight = custoRight + 1

        add_custo_right = goodTentativas(rigth, chr(ord(char) + 1), q)
        add_custo_left = goodTentativas(left, chr(ord(char) + 1), q)
        
    return min(custoLeft + add_custo_left, custoRight + add_custo_right)

n = int(input())

for _ in range(n):
    tamanho = int(input())
    string = input()
    print(goodTentativas(string, "a", tamanho))
