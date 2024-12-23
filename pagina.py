#"pagina.py": pagina del inicio de la app, controla las paginas de hemograma y orina

import streamlit as st

def main_page():
    st.title("Evaluador Médico")
    usuario=st.session_state.get("usuario", "Invitado")
    st.write(f"Bienvenido, {usuario}!") #Mostrar el nombre del usuario que ingreso

    #Para el cambio de paginas 
    if st.button("Examen de Hemograma",key="hemograma"):
        st.session_state.pagina_actual="hemograma" #Cambia el estado de "pagina_actual" a hemograma
        st.rerun()
    if st.button("Examen de Orina",key="orina"):
        st.session_state.pagina_actual="orina" #Cambia el estado de "pagina_actual" a orina
        st.rerun()
    if st.button("Cerrar sesión",key="logout"):
        st.session_state.pagina_actual="login" #Cambia el estado de "pagina_actual" a login
        st.rerun()