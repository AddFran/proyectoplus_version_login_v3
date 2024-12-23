import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import re
import requests

# Leer credenciales desde Streamlit secrets
firebase_credentials = st.secrets["firebase_credentials"]
api_key = firebase_credentials["api_key"]

firebase_credentials_dict = dict(firebase_credentials)

# Inicializar Firebase Admin usando las credenciales desde secrets
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials_dict)
    firebase_admin.initialize_app(cred)

def es_correo_valido(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

def verificar_usuario(usuario, password):
    if not es_correo_valido(usuario):
        return False, "El formato del correo es invalido. Por favor, ingrese un correo válido."

    try:
        user = auth.get_user_by_email(usuario)

        # Autenticación con la API de Firebase usando API Key
        url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        payload = {
            "email": usuario,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(f"{url}?key={api_key}", json=payload)

        if response.status_code == 200:
            return True, "Inicio de sesión exitoso"
        else:
            error_message = response.json().get("error", {}).get("message", "Error desconocido")
            return False, f"Error de autenticación: {error_message}"

    except auth.UserNotFoundError:
        return False, "El usuario no existe."
    except ValueError:
        return False, "El formato del correo es inválido. Por favor, ingrese un correo válido."
    except Exception as e:
        return False, f"Error al comunicarse con Firebase: {str(e)}"

# Página de inicio de sesión
def login_page():
    if "pagina_actual" not in st.session_state:
        st.session_state.pagina_actual = "login"

    st.title("Inicio de Sesión")

    usuario = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        autenticado, mensaje = verificar_usuario(usuario, password)
        if autenticado:
            st.success(mensaje)
            st.session_state.pagina_actual = "app"  # Cambiar a la página principal
            st.session_state.usuario = usuario      # Guardar el usuario en la sesión
            st.rerun()
        else:
            st.error(mensaje)

    if st.button("¿Eres nuevo? Crea una cuenta"):
        st.session_state.pagina_actual = "crear_usuario"  # Ir a la página de registro
        st.rerun()


def crear_usuario_page():
    st.title("Crear cuenta")
    nombre = st.text_input("Nombre completo")
    usuario = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    if st.button("Registrarse"):
        try:
            # Crear usuario en Firebase con correo y contraseña
            user = auth.create_user(
                email=usuario,
                password=password,
                display_name=nombre
            )
            st.success("Usuario registrado exitosamente")
            st.session_state.pagina_actual = "login"  # Redirigir al login
            st.rerun()
        except Exception as e:
            st.error(f"Error al crear usuario: {e}")

    if st.button("Volver"):
        st.session_state.pagina_actual = "login"
        st.rerun()
