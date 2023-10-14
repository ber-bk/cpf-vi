CPF Validation Instrument (vi). Simple tool made in python to check if a given CPF ("Cadastro de Pessoa Física") is valid.

It was made with python 3.11, but it should work without issues on older versions. In order to use it, simply download the .py file and run it.

It is licensed under the LGPL-2.1.

-

The brazillian government used to provide a simple javascript function to perform this check in one of their websites. Sadly, it seems that such information is no longer acessible. I've used the guide made by Gustavo Furtado de Oliveira Alves at https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/ (Acessed October 4th 2023) to write this program.

Note that a valid CPF might not be one that is in use.

-

A valid CPF must follow these rules:

1 - It must contain 11 digits.

2 - The 11 digits must not be the same (11111111111, 22222222222, etc).

3 - The first verification digit (the 10th digit) must be equal to the result of the following formula: 

FORMULA: The first 9 numbers are multiplied by a sequence of 10 to 2 (1st number gets multiplied by 10, the 2nd one gets multiplied by 9...the 9th number gets multiplied by 2). The sum of the resulting sequence is then multiplied by 10. The last step is to divide the resulting number by 11. The remainder of such division must be equal to the first verification digit (the 10th digit). In case the remainder is 10, you consider it to be 0.

4 - The second verification digit (the 11th digit) must be equal to the result of the following formula:

FORMULA: The first 10 numbers are multiplied by a sequence of 11 to 2 (1st number gets multiplied by 11, the 2nd one gets multiplied by 10...the 10th number gets multiplied by 2). The sum of the resulting sequence is then multiplied by 10. The last step is to divide the resulting number by 11. The remainder of such division must be equal to the second verification digit (the 11th digit). In case the remainder is 10, you consider it to be 0.
