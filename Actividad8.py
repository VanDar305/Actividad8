import PySimpleGUI as sg

# Crear el layout de la ventana
layout = [
    [sg.TabGroup([
        [sg.Tab('Eventos', [
            [sg.Text('Nombre del Evento:'), sg.InputText(key='-NOMBRE_E-', size=(21, 1)), sg.Text('Lugar:', size=(6, 1)), sg.InputText(key='-LUGAR-', size=(20, 1))],
            [sg.Text('Fecha:', size=(15, 1)), sg.InputText(key='-FECHA-', size=(20, 1)), sg.Text('Hora:', size=(6, 1)), sg.InputText(key='-HORA-', size=(20, 1))],
            [sg.Text('Cupo:', size=(15, 1)), sg.InputText(key='-CUPO-', size=(20, 1)), sg.Text('Imagen:'), sg.InputText(key='-IMAGEN-', size=(20, 1)), sg.Button('Buscar')],
            [sg.Button('Agregar'), sg.Button('Modificar'), sg.Button('Eliminar')],
            [sg.Table(headings=['Nombre', 'Fecha', 'Cupo', 'Lugar', 'Hora', 'Imagen'], values=[], size=(80, 10), key='-TABLE-', enable_events=True)],
            [sg.Image(key='-IMAGEN-', size=(50, 50))]
        ])],
        [sg.Tab('Participantes', [
            # Campos para ingresar los datos del participante
            [sg.Text('Evento:', size=(12, 1)), sg.Combo(["Evento 1", "Evento 2", "Evento 3", "Evento 4", "Evento 5"], key='-EVENTO-', size=(20, 1)), sg.Text('Nombre:', size=(12, 1)), sg.InputText(key='-NOMBRE_PARTICIPANTE-', size=(20, 1))],
            [sg.Text('Tipo Documento:'), sg.Combo(["Tarjeta de Entidad", "Cedula de Ciudadania", "Pasaporte", "Cedula de Extranjeria", "Otro"], key='-TIPO_DOCUMENTO-', size=(20, 1)), sg.Text('Número Documento:', size=(12, 1)), sg.InputText(key='-NUMERO_DOCUMENTO-', size=(20, 1))],
            [sg.Text('Teléfono:', size=(12, 1)), sg.InputText(key='-TELEFONO-', size=(22, 1)), sg.Text('Tipo Participante:', size=(12, 1)), sg.Combo(["Estudiante", "Profesor", "Funcionario", "Turista", "Otro"], key='-TIPO_PARTICIPANTE-', size=(18, 1))],
            [sg.Text('Dirección:'), sg.InputText(key='-DIRECCION-', size=(20, 1)), sg.Text('Foto:'), sg.InputText(key='-FOTO-', size=(20, 1)), sg.Button('Buscar Foto')],
            [sg.Button('Agregar Participante'), sg.Button('Modificar Participante'), sg.Button('Eliminar Participante')],
            [sg.Table(headings=['Evento', 'Nombre', 'Tipo Documento', 'Número Documento', 'Teléfono', 'Dirección', 'Tipo Participante ', 'Foto'], values=[], size=(80, 10), key='-TABLE_PARTICIPANTES-', enable_events=True)],
            [sg.Image(key='-IMAGE_PARTICIPANTE-', size=(200, 200))]
        ])],
            [sg.Tab('Configuración', [
            [sg.Text('Validar el aforo de los participantes'), sg.Checkbox('', key='-AFORO-')],
            [sg.Text('Solicitar imágenes'), sg.Checkbox('', key='-SOLICITAR-')],
            [sg.Text('Modificar registros'), sg.Checkbox('', key='-MOD_REG-')],
            [sg.Text('Eliminar registros'), sg.Checkbox('', key='-ELIM_REG-')],
            [sg.Button('Guardar')]
            ])]
    ])]
]

# Crear la ventana
window = sg.Window('-- Pagina de registro para la COP16', layout)

# Lista para almacenar los eventos
eventos = []

# Lista para almacenar los participantes
participantes = []

# Función para actualizar la visualización de la tabla con los eventos
def actualizar_tabla():
    values = [[event[0], event[1], event[2], event[3], event[4], event[5]] for event in eventos]
    window['-TABLE-'].update(values)

# Función para actualizar la visualización de la tabla con los participantes
def actualizar_tabla_participantes():
    values = [[participante[0], participante[1], participante[2], participante[3], participante[4], participante[5], participante[6]] for participante in participantes]
    window['-TABLE_PARTICIPANTES-'].update(values)

# Bucle principal del programa
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Salir':
        break

    # Buscar imagen
    if event == 'Buscar':
        filename = sg.popup_get_file('Selecciona una imagen', file_types=(("Imagenes", "*.png;*.jpg;*.jpeg;*.gif"),))
        if filename:
            window['-IMAGEN-'].update(filename)
            window['-IMAGE-'].update(filename)

    # Buscar foto del participante
    if event == 'Buscar Foto':
        filename = sg.popup_get_file('Selecciona una imagen', file_types=(("Imagenes", "*.png;*.jpg;*.jpeg;*.gif"),))
        if filename:
            window['-FOTO-'].update(filename)
            window['-IMAGE_PARTICIPANTE-'].update(filename)

#Logica de la pestaña 1
    # Agregar nuevo evento
    if event == 'Agregar':
        nombre = values['-NOMBRE_E-']
        fecha = values['-FECHA-']
        cupo = values['-CUPO-']
        lugar = values['-LUGAR-']
        hora = values['-HORA-']
        imagen = values['-IMAGEN-']  # Obtener el nombre de la imagen
        if nombre and fecha and cupo and lugar and hora:
            eventos.append([nombre, fecha, cupo, lugar, hora, imagen])
            actualizar_tabla()

    # Modificar evento seleccionado
    if event == 'Modificar':
        selected_row = values['-TABLE-']
        if selected_row:
            index = selected_row[0]
            nombre = values['-NOMBRE-']
            fecha = values['-FECHA-']
            cupo = values['-CUPO-']
            lugar = values['-LUGAR-']
            hora = values['-HORA-']
            imagen = values['-IMAGEN-']  # Obtener el nombre de la imagen
            if nombre and fecha and cupo and lugar and hora:
                eventos[index] = [nombre, fecha, cupo, lugar, hora, imagen]
                actualizar_tabla()

    # Eliminar evento seleccionado
    if event == 'Eliminar':
        selected_row = values['-TABLE-']
        if selected_row:
            index = selected_row[0]
            eventos.pop(index)
            actualizar_tabla()

#Logica de la pestaña 2

    # Agregar nuevo participante
    if event == 'Agregar Participante':
        evento = values['EVENTO']
        nombre_participante = values['-NOMBRE_PARTICIPANTE-']
        tipo_documento = values['-TIPO_DOCUMENTO-']
        numero_documento = values['-NUMERO_DOCUMENTO-']
        telefono = values['-TELEFONO-']
        direccion = values['-DIRECCION-']
        tipo_participante = values['-TIPO_PARTICIPANTE-']
        foto = values['-FOTO-']  # Obtener el nombre de la imagen
        if evento and nombre_participante and tipo_documento and numero_documento and telefono and direccion and tipo_participante:
            participantes.append([evento, nombre_participante, tipo_documento, numero_documento, telefono, direccion, tipo_participante, foto])
            actualizar_tabla_participantes()

    # Modificar participante seleccionado
    if event == 'Modificar Participante':
        selected_row = values['-TABLE_PARTICIPANTES-']  # Asegúrate de que esta clave sea correcta
        if selected_row:
            index = selected_row[0]
            evento = values['EVENTO']
            nombre_participante = values['-NOMBRE_PARTICIPANTE-']
            tipo_documento = values['-TIPO_DOCUMENTO-']
            numero_documento = values['-NUMERO_DOCUMENTO-']
            telefono = values['-TELEFONO-']
            direccion = values['-DIRECCION-']
            tipo_participante = values['-TIPO_PARTICIPANTE-']
            foto = values['-FOTO-']  # Obtener el nombre de la imagen
            if evento and nombre_participante and tipo_documento and numero_documento and telefono and direccion and tipo_participante:
                participantes[index] = [evento, nombre_participante, tipo_documento, numero_documento, telefono, direccion, tipo_participante, foto]
                actualizar_tabla_participantes()

    # Eliminar participante seleccionado
    if event == 'Eliminar Participante':
        selected_row = values['-TABLE_PARTICIPANTES-']
        if selected_row:
            index = selected_row[0]
            participantes.pop(index )
            actualizar_tabla_participantes()

    #Logica de la pestaña 3
        if event == 'Guardar':
            aforo = values['-AFORO-']
            solicitar = values['-SOLICITAR-']
            modificar = values['-MOD_REG-']
            eliminar = values['-ELIM_REG-']
            sg.popup(f'Se guardaron los {"cambios" if aforo or solicitar or modificar or eliminar else "cambios"}')

window.close()