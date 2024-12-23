#"app.py": Controla el flujo entre las pagiinas de la aplicacion web

import streamlit as st

#Importamos los otros archivos necesarios para el programa (solo control de flujo)
from login import login_page
from login import crear_usuario_page
from analisis import orina_page, hemograma_page
from pagina import main_page

#Navegación entre páginas
#Dependiendo del valor del session_state nos moveremos por la diferentes paginas
#Cada pagina esta guardada dentro de una funcion en otro archivo .py


#"session_state", es como una variable global que guardara datos durante la ejecucion del programa
#lo usamos para manejar en que paagina estaremos
if "pagina_actual" not in st.session_state:
    st.session_state.pagina_actual="login"

if st.session_state.pagina_actual=="login":
    login_page()
elif st.session_state.pagina_actual=="crear_usuario":
    crear_usuario_page()
elif st.session_state.pagina_actual=="app":
    main_page()
elif st.session_state.pagina_actual=="orina":
    orina_page()
elif st.session_state.pagina_actual=="hemograma":  # Nueva condición
    hemograma_page()