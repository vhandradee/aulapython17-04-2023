num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print ('''(1) soma
          (2) subtraçao
          (3) multiplicação
          (4) divisão''')

calculo = float(input('selecione a operaçao que deseja realizar: '))
match calculo : 
   case 1:
        soma= (num1 + num2)
        print('a soma é: ', soma)
        
    
   case 2:
        subtração = (num1 - num2)
        print('a sub é: ', subtração)
    
   case 3:
        multiplicação = (num1 * num2)
        print('a mult é: ', multiplicação)
    
   case 4:
        divisão = (num1 / num2)
        print('a divisão é: ', divisão)
    
   case _:
       print('opcao inválida')