def arithmetic_arranger(problemas, mostrar_resp=False):
   #Limita a quantidade de problemas por vez
    if len(problemas) > 5:
        return "Erro: apenas cinco problemas"

    problemas_arr = {"topo": [], "base": [], "linha": [], "resultado": []}

    for problema in problemas:
        operand1, operador, operand2 = problema.split()
        
        if operador not in ('+', '-'):
            return "apenas '+' ou '-'"
        
        if not operand1.isdigit() or not operand2.isdigit():
            return "apenas digitos"
        
        if len(operand1) > 4 or len(operand2) > 4:
            return "numeros podem ter apenas até 4 digitos"
        
        width = max(len(operand1), len(operand2)) + 2
        problemas_arr["topo"].append(operand1.rjust(width))
        problemas_arr["base"].append(operador + operand2.rjust(width - 1))
        problemas_arr["linha"].append("-" * width)
        if mostrar_resp:
            if operador == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            problemas_arr["resultado"].append(result.rjust(width))

    problemas_arr = list(map("    ".join, problemas_arr.values()))
    
    if mostrar_resp:
        return "\n".join(problemas_arr)
    else:
        return "\n".join(problemas_arr[:-1])

problem1 = ["30 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problem1, True))

