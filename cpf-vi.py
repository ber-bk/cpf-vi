'''
CPF Validation Instrument
Copyright (C) 2023 ber-bk (https://github.com/ber-bk/cpf-vi)

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 
USA
'''


print()
print("--------------------CPF Validation Instrument--------------------")


#verification of the first verification digit
def AlgorithmFirstNine(): 
  MultiplicationFactorsList = [10,9,8,7,6,5,4,3,2]
  MultipliedCPF = []
  for x in range(9):
    MultipliedCPF.append(MultiplicationFactorsList[x]*MappedCPF[x]) 
  if sum(MultipliedCPF)*10%11 == 10:
    return 0
  else:
    return sum(MultipliedCPF)*10%11


#verification of the second verification digit
def AlgorithmFirstTen(): 
  MultiplicationFactorsList = [11,10,9,8,7,6,5,4,3,2]
  MultipliedCPF = []
  for x in range(10):
    MultipliedCPF.append(MultiplicationFactorsList[x]*MappedCPF[x])
  if sum(MultipliedCPF)*10%11 == 10:
    return 0
  else:
    return sum(MultipliedCPF)*10%11


while True:
  
  #keeps trying if user mistakenly inputs something other than a number
  while True:
    try:
      print()
      print("Insert the CPF with digits only:")
      InputCPF = input()
      MappedCPF = list(map(int,InputCPF)) #transforming input (string) into a list of integers
    except:
        print()
        input("The CPF must only contain digits. Press Enter to try again.")
        print()
    else:
      break

  #in case the number of digits isn't 11, the CPF is invalid
  if len(InputCPF) != 11:
    print()
    print("The CPF is Invalid (The number of digits isn't 11)")
    print()
    input("Press Enter to do it once more, or Control+C to end")

  #in case all digits are the same, the CPF is invalid
  elif MappedCPF[0] == MappedCPF[1] and MappedCPF[2] and MappedCPF[3] and MappedCPF[4] and MappedCPF[5] and MappedCPF[6] and MappedCPF[7] and MappedCPF[8] and MappedCPF[9] and MappedCPF[10]:
    print()
    print("The CPF is Invalid (All digits are the same)")
    print()
    input("Press Enter to do it once more, or Control+C to end")

  #valid CPF
  elif AlgorithmFirstNine() == MappedCPF[9] and AlgorithmFirstTen() == MappedCPF[10]:
    print()
    print("The CPF is Valid")
    print()
    input("Press Enter to do it once more, or Control+C to end")

  #in case the verification fails, the CPF is invalid
  else:
    print()
    print("The CPF is Invalid")
    print()
    input("Press Enter to do it once more, or Control+C to end")
