import os
import datetime
from twilio.rest import Client

# 1. EL MODELO DE DATOS
menu = {
    "Semana 1": {
        "Lunes": {"Desayuno": "Galletitas de banana y avena + fruta", "Merienda": "Mismas galletitas para las dos", "Tip": "Hacer doble tanda y freezar."},
        "Martes": {"Desayuno": "Pan de salvado con queso + fruta", "Merienda": "Juli: Sandwich / Ele: Yogur + fruta/granola", "Tip": "Solo agregás el yogur para Ele."},
        "Miércoles": {"Desayuno": "Panqueques de banana", "Merienda": "Juli: 2 mini panqueques / Ele: Fruta cortada", "Tip": "Hacés panqueques y listo."},
        "Jueves": {"Desayuno": "Tostadas con pasta de maní + banana", "Merienda": "Juli: Fruta / Ele: Tostaditas saladas con queso", "Tip": "Separar versiones dulce/salada."},
        "Viernes": {"Desayuno": "Yogur con avena y fruta", "Merienda": "Juli: Yogur con cereal / Ele: Mix de cereal + fruta", "Tip": "Si Juli no quiere yogur, granola seca."},
    },
    "Semana 2": {
        "Lunes": {"Desayuno": "Muffins de banana y avena", "Merienda": "Mismos muffins para las dos", "Tip": "Ideal hacerlos el domingo."},
        "Martes": {"Desayuno": "Sandwich pan integral con queso y huevo", "Merienda": "Juli: Mismo sandwich / Ele: Yogur bebible + fruta", "Tip": "Preparar el huevo revuelto a la mañana."},
        "Miércoles": {"Desayuno": "Huevo revuelto con tostada", "Merienda": "Juli: Mini omelette frío / Ele: Fruta picada + frutos secos", "Tip": "Cuidado con los frutos secos en el jardín."},
        "Jueves": {"Desayuno": "Licuado de banana + tostada con queso", "Merienda": "Juli: Fruta / Ele: Tostaditas con queso o mini sandwich", "Tip": "El licuado hacerlo en el momento."},
        "Viernes": {"Desayuno": "Granola casera + leche o yogur", "Merienda": "Juli: Yogur con granola / Ele: Granola + fruta", "Tip": "Checkear stock de granola."},
    }
}

def obtener_info_hoy():
    hoy = datetime.datetime.now()
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_nombre = dias[hoy.weekday()]
    
    # Lógica de semanas: Semana 1 en semanas impares del año, Semana 2 en pares
    semana_anio = hoy.isocalendar()[1]
    semana_nombre = "Semana 1" if semana_anio % 2 != 0 else "Semana 2"
    
    return dia_nombre, semana_nombre

def enviar_whatsapp():
    # Obtener variables de entorno (Configuradas en GitHub Secrets o Twilio)
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    from_whatsapp = os.environ.get('TWILIO_PHONE') # Ej: 'whatsapp:+14155238886'
    to_whatsapp = os.environ.get('MY_PHONE')       # Tu número con 'whatsapp:+549...'
    
    dia, semana = obtener_info_hoy()
    
    # Solo enviar de Lunes a Viernes
    if dia in ["Sábado", "Domingo"]:
        print("Es fin de semana, no se envía menú.")
        return

    data = menu[semana][dia]
    
    cuerpo_mensaje = f"""
*🗓️ {dia.upper()} ({semana})*
--------------------------
☀️ *Desayuno:* {data['Desayuno']}

🎒 *Merienda Jardín:*
{data['Merienda']}

💡 *Tip:* {data['Tip']}
--------------------------
_Enviado desde tu App de Meriendas_ 🍎
"""

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=cuerpo_mensaje,
        from_=from_whatsapp,
        to=to_whatsapp
    )
    print(f"Mensaje enviado con éxito. SID: {message.sid}")

if __name__ == "__main__":
    enviar_whatsapp()