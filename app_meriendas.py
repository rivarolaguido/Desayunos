import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Meriendas Juli & Ele", page_icon="🍎")

# El modelo de tus 2 semanas
menu = {
    "Semana 1": {
        "Lunes": {"Desayuno": "Galletitas caseras de banana y avena + fruta", "Merienda": "Mismas galletitas para las dos", "Tip": "Hacer doble tanda y freezar."},
        "Martes": {"Desayuno": "Pan de salvado con queso untable + fruta", "Merienda": "Juli: Sandwich / Ele: Yogur + fruta/granola", "Tip": "Solo agregás el yogur para Ele."},
        "Miércoles": {"Desayuno": "Panqueques de banana", "Merienda": "Juli: 2 mini panqueques / Ele: Fruta cortada", "Tip": "Hacés panqueques y listo."},
        "Jueves": {"Desayuno": "Tostadas con pasta de maní + banana", "Merienda": "Juli: Fruta / Ele: Tostaditas saladas con queso", "Tip": "Separar versiones dulce/salada."},
        "Viernes": {"Desayuno": "Yogur con avena y fruta", "Merienda": "Juli: Yogur con cereal / Ele: Mix de cereal + fruta", "Tip": "Si Juli no quiere yogur, granola seca."},
    },
    "Semana 2": {
        "Lunes": {"Desayuno": "Muffins caseros de banana y avena", "Merienda": "Mismos muffins para las dos", "Tip": "Ideal hacerlos el domingo."},
        "Martes": {"Desayuno": "Sandwich pan integral con queso y huevo", "Merienda": "Juli: Mismo sandwich / Ele: Yogur bebible + fruta", "Tip": "Preparar el huevo revuelto a la mañana."},
        "Miércoles": {"Desayuno": "Huevo revuelto con tostada", "Merienda": "Juli: Mini omelette frío / Ele: Fruta picada + frutos secos", "Tip": "Cuidado con los frutos secos en el jardín."},
        "Jueves": {"Desayuno": "Licuado de banana + tostada con queso", "Merienda": "Juli: Fruta / Ele: Tostaditas con queso o mini sandwich", "Tip": "El licuado hacerlo en el momento."},
        "Viernes": {"Desayuno": "Granola casera + leche o yogur", "Merienda": "Juli: Yogur con granola / Ele: Granola + fruta", "Tip": "Checkear stock de granola."},
    }
}

st.title("🍎 Planificador de Meriendas")
st.write(f"Hoy es: **{datetime.now().strftime('%A %d/%m')}**")

# Selectores
semana_sel = st.selectbox("Seleccioná la semana:", ["Semana 1", "Semana 2"])
dia_sel = st.pills("Día:", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])

if dia_sel:
    data = menu[semana_sel][dia_sel]
    
    st.divider()
    
    st.subheader(f"☀️ Desayuno - {dia_sel}")
    st.info(data["Desayuno"])
    
    st.subheader(f"🎒 Merienda Jardín")
    st.success(data["Merienda"])
    
    st.warning(f"💡 **Tip:** {data['Tip']}")
else:
    st.write("Seleccioná un día para ver el detalle.")

# Botón para el Calendar (Simulado o link)
st.sidebar.button("Sincronizar Google Calendar")
st.sidebar.write("---")
st.sidebar.caption("App personalizada para Juli y Ele")