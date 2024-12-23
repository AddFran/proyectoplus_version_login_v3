import streamlit as st
import app.pag as pag

#Página principal
def hemograma_page():
    st.title("Evaluador de Hemograma")
    #usuario = st.session_state.get("usuario", "Invitado")
    #st.write(f"Bienvenido, {usuario}!")
    st.write("""Un hemograma, también conocido como conteo sanguíneo completo (CSC), es un análisis de sangre que mide las concentraciones 
            de glóbulos rojos, glóbulos blancos y plaquetas en la sangre. También proporciona información sobre la hemoglobina y el volumen 
            promedio de los glóbulos rojos. El hemograma es una prueba que ayuda a los médicos a evaluar el estado de salud general 
            de una persona y a detectar enfermedades como anemia, infecciones o leucemia. Los resultados de un hemograma pueden ayudar 
            a confirmar un diagnóstico o detectar respuestas adversas a tratamientos.""")

    #Muestar la pagina
    pag.mostrar_resultados_hemograma()

    if st.button("Volver al menu principal"):
        st.session_state.pagina_actual="app"
        st.rerun()

#Pagina principal del examen de orina
def orina_page():
    st.title("Examen de Orina")
    st.write("""Un análisis de orina es una prueba que se le hace a la orina. Se utiliza para detectar y controlar una amplia variedad 
            de trastornos, como infecciones de las vías urinarias, enfermedad renal y diabetes.
            Un análisis de orina implica examinar el aspecto, la concentración y el contenido de la orina.""")
    with st.form("formulario_orina"):
        pag.mostrar_resultados_orina() 

    if st.button("Volver al menú principal", key="volver_menu"):
        st.session_state.pagina_actual="app" #Cambia el session_state para regresar al menu
        st.rerun() #Funcion de streamlit para no presionar el boton 2 veces