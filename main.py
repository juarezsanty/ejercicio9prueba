from src.limpiar import limpiar_espacios, formato_titulo

clients = [
" Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
" Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
"luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
" ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
"carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
"alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
"patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
"MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
"SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
"Damián Castillo ", None, "", " "
]

clientes_limpios = []

for cliente in clients:
    if cliente and cliente.strip():  # Verificar que no sea None o vacío
        cliente = limpiar_espacios(cliente)
        cliente = formato_titulo(cliente)
        clientes_limpios.append(cliente)
clientes_limpios = list(set(clientes_limpios))  # Eliminar duplicados

print(clientes_limpios)
