--divisible por los 9 primeros numeros naturales
divisible::Int->String
divisible a = if mod a 9 == 0 then "divisible por 9"              
              else if mod  a 8 == 0 then "divisible por 8"              
              else if mod  a 7 == 0 then "divisible por 7"              
              else if mod  a 6 == 0 then "divisible por 6"              
              else if mod  a 5 == 0 then "divisible por 5"              
              else if mod  a 4 == 0 then "divisible por 4"              
              else if mod  a 3 == 0 then "divisible por 3"              
              else if mod  a 2 == 0 then "divisible por 2"              
              else "no es divisible"
              
              
