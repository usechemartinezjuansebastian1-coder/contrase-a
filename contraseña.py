print ("verificador de contraseñas")

contraseña = "1234"

ingreso =  input ("ingrese su contraseña de 4 digitos: ")

while ingreso != contraseña:
    print ("contraseña incorrecta")
    ingreso = input ("ingrese su contraseña de 4 digitos: ")

print ("contraseña correcta, bienvenido")
