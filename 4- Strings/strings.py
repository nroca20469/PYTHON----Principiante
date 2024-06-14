# STRINGS

my_string = "My string";
my_other_string = 'My other string';

print(len(my_string));
print(len(my_other_string));

# Concatenar string
print(my_string + my_other_string);
print(my_string + ' ' + my_other_string);

my_new_line_string = 'Este es un string \ncon salto de linea';
print(my_new_line_string);

my_new_tabulated_string = 'Este es un string \tcon tabulacion';
print(my_new_tabulated_string);

my_new_scaped_string = '\\Este es un string \ncon escapado';
print(my_new_scaped_string);

# Formateo 
name, surname, age = 'Brais', 'Moure', 30;
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age));  # --> Formateo directo
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)); # --> Formateo no directom, sino con variables, busca el 1º y 2º string y luego el 1º digito numerico

# Mala praxis
print("Mi nombre es " + name + " " + surname  + " y mi edad es " + str(age)); # --> NO USAR, LE CUESTA EN ESTE LENGUAJE --> y age tiene que ser con str(age)