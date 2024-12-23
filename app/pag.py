import streamlit as st
from . import data  #Si estás dentro de la carpeta 'app'

# Asignar valores por defecto a los parámetros si no están en session_state
def inicializar_valores():
    #Serie roja
    if 'hematies' not in st.session_state:
        st.session_state.hematies = 5.0  #Valor normal en mill/mm3
    if 'hemoglobina' not in st.session_state:
        st.session_state.hemoglobina = 15.0  #Valor normal en g/dL
    if 'hematocrito' not in st.session_state:
        st.session_state.hematocrito = 45.0  #Valor normal en %
    if 'vcm' not in st.session_state:
        st.session_state.vcm = 90.0  # Valor normal en fL
    if 'hcm' not in st.session_state:
        st.session_state.hcm = 30.0  # Valor normal en pg
    if 'ccmh' not in st.session_state:
        st.session_state.ccmh = 33.0  # Valor normal en %
    if 'rdw' not in st.session_state:
        st.session_state.rdw = 13.0  # Valor normal en %
    if 'reticulocitos' not in st.session_state:
        st.session_state.reticulocitos = 1.0  # Valor normal en %

    #Serie blanca
    if 'glob_blancos' not in st.session_state:
        st.session_state.glob_blancos = 8000.0 
    if 'neutrofilos' not in st.session_state:
        st.session_state.neutrofilos = 4000.0 
    if 'linfocitos' not in st.session_state:
        st.session_state.linfocitos = 2750.0 
    if 'monocitos' not in st.session_state:
        st.session_state.monocitos = 300.0 
    if 'eosinofilos' not in st.session_state:
        st.session_state.eosinofilos = 185.0 
    if 'basofilos' not in st.session_state:
        st.session_state.basofilos = 55.0 

    #Plaquetas
    if 'plaquetas' not in st.session_state:
        st.session_state.plaquetas=225000.0

#Función para mostrar la interfaz de ingreso de datos
def mostrar_resultados_hemograma():
    # Inicializamos los valores por defecto
    inicializar_valores()

    with st.form("formulario_examen"):
        #Parámetros de sangre
        st.subheader("Serie Roja")
        
        #Usar columnas para organizar las casillas de entrada
        col1,col2,col3=st.columns(3)

        with col1:
            hematies=st.number_input("Globulos Rojos (mill/mm³):",min_value=0.1,step=1.0,value=st.session_state.hematies,help="4,9 - 6,1 mill/mm3")
        with col2:
            hemoglobina=st.number_input("Hemoglobina (g/dL):",min_value=0.1,step=1.0,value=st.session_state.hemoglobina,help="14 - 18 g/dL")
        with col3:
            hematocrito=st.number_input("Hematocrito (%):",min_value=0.1,step=1.0,value=st.session_state.hematocrito,help="42.0 - 52.0 %")

        #Nueva fila de columnas para otros parametros
        col4, col5, col6 = st.columns(3)

        with col4:
            rdw=st.number_input("RDW (%):",min_value=1.0,step=1.0,value=st.session_state.rdw,help="11 - 15 %")
        with col5:
            reticulocitos=st.number_input("Reticulocitos (%):",min_value=0.01, step=0.1, value=st.session_state.reticulocitos,help="0.5 - 1.5 %")
        with col6:
            vcm=(hematocrito/hematies)*10

        #SERIE BLANCA
        st.subheader("Serie Blanca")

        col7,col8,col9=st.columns(3)

        with col7:
            glob_blancos=st.number_input("Globulos Blancos (uL):",min_value=0.1,step=1.0,value=st.session_state.glob_blancos,help="6000 - 10000 uL")
        with col8:
            neutrofilos=st.number_input("Neutrofilos (uL):",min_value=0.1,step=1.0,value=st.session_state.neutrofilos,help="3000 - 5000 uL")
        with col9:
            linfocitos=st.number_input("Linfocitos (uL):",min_value=0.1,step=1.0,value=st.session_state.linfocitos,help="1500 - 4000 uL")

        col10,col11,col12=st.columns(3)

        with col10:
            monocitos=st.number_input("Monocitos (uL):",min_value=0.1,step=1.0,value=st.session_state.monocitos,help="100 - 500 uL")
        with col11:
            eosinofilos=st.number_input("Eosinofilos (uL):",min_value=0.1,step=1.0,value=st.session_state.eosinofilos,help="20 - 350 uL")
        with col12:
            basofilos=st.number_input("Basofilos (uL):",min_value=0.1,step=1.0,value=st.session_state.basofilos,help="10 - 100 uL")

        st.subheader("Plaquetas")

        col13,col14,col15=st.columns(3)
        
        with col13:
            plaquetas=st.number_input("Plaquetas (uL):", min_value=0.1, step=1000.0, value=st.session_state.plaquetas, help="150000 - 300000 uL")
        with col14:
            nc=0
        with col15:
            nc=0


        #Boton para enviar el formulario
        submit_button = st.form_submit_button("EVALUAR")
        if submit_button:
            st.session_state.hematies=hematies
            st.session_state.hemoglobina=hemoglobina
            st.session_state.hematocrito=hematocrito
            st.session_state.vcm=vcm
            st.session_state.hcm=(hemoglobina/hematies)*10
            st.session_state.ccmh=(hemoglobina*100)/hematocrito
            st.session_state.rdw=rdw
            st.session_state.reticulocitos=reticulocitos

            st.session_state.glob_blancos=glob_blancos
            st.session_state.neutrofilos=neutrofilos
            st.session_state.linfocitos=linfocitos
            st.session_state.monocitos=monocitos
            st.session_state.eosinofilos=eosinofilos
            st.session_state.basofilos=basofilos
            
            st.session_state.plaquetas=plaquetas

            #Resetear data.py--------------------------------------------------------#######################
            reiniciar_data()
            evaluar_hemograma()

#Función para evaluar el hemograma y mostrar los resultados de manera más estética
def evaluar_hemograma():
    #Comprobar si los datos están disponibles en session_state
    
    #st.rerun()
    if 'hematies' not in st.session_state or 'hemoglobina' not in st.session_state or 'hematocrito' not in st.session_state:
        st.error("¡Debe ingresar los datos primero para evaluar el hemograma!")
        return  #Detener la ejecución si faltan datos

    hematies = st.session_state.hematies
    hemoglobina = st.session_state.hemoglobina
    hematocrito = st.session_state.hematocrito
    vcm = st.session_state.vcm
    hcm = st.session_state.hcm
    ccmh = st.session_state.ccmh
    rdw = st.session_state.rdw
    reticulocitos = st.session_state.reticulocitos

    glob_blancos=st.session_state.glob_blancos
    neutrofilos=st.session_state.neutrofilos
    linfocitos=st.session_state.linfocitos
    monocitos=st.session_state.monocitos 
    eosinofilos=st.session_state.eosinofilos 
    basofilos=st.session_state.basofilos 
    
    plaquetas=st.session_state.plaquetas 

    #Título para la sección de resultados
    st.subheader("Resultados del Hemograma")
    
    #------------------------------------------------------ MEJORAR la vista de esta parte \/ -------------------------------------#
    diagnostico_hematies(hematies)
    diagnostico_hemoglobina(hemoglobina)
    diagnostico_hematocrito(hematocrito)
    diagnostico_vcm(vcm)
    diagnostico_rdw(rdw)
    diagnostico_reticulocitos(reticulocitos)

    diagnostico_glob_blancos(glob_blancos)
    diagnostico_neutrofilos(neutrofilos)
    diagnostico_linfocitos(linfocitos)
    diagnostico_monocitos(monocitos)
    diagnostico_eosinofilos(eosinofilos)
    diagnostico_basofilos(basofilos)

    diagnostico_plaquetas(plaquetas)

    st.write("---------------------------------------------------------------")

    mostrar_enfermedad("Anemia",data.anemia_info,data.anemia)
    mostrar_enfermedad("Poliglobulia",data.poliglobulia_info,data.poliglobulia)
    mostrar_enfermedad("Malformacion de los globulos rojos",data.malf_info,data.malformacion)
    if data.anemia:
        mostrar_enfermedad("Anemia Regenerativa",data.a_regen_info,data.a_regen)
        mostrar_enfermedad("Anemia Arregenerativa",data.a_arregen_info,data.a_arregen)
        mostrar_enfermedad("Anemia Macrocitica",data.a_macro_info,data.a_macro)
        mostrar_enfermedad("Anemia Normocitica",data.a_normo_info,data.a_normo)
        mostrar_enfermedad("Anemia Microcitica",data.a_micro_info,data.a_micro)

    mostrar_enfermedad_v2("Infeccion",data.infeccion_info,data.infeccion)
    mostrar_enfermedad_v2("Inflamacion",data.inflamacion_info,data.inflamacion)
    mostrar_enfermedad_v2("Sepsis",data.sepsis_info,data.sepsis)
    mostrar_enfermedad_v2("Enferemedad Autoinmune",data.enf_autoinmune_info,data.enf_autoinmune)
    mostrar_enfermedad("Neutropenia",data.neutropenia_info,data.neutropenia)
    mostrar_enfermedad_v2("Hemopatias",data.hemopatias_info,data.hemopatias)
    mostrar_enfermedad_v2("Enferemedad de Cushing",data.cushing_info,data.cushing)
    mostrar_enfermedad_v2("Enferemedad de Hodgkin",data.hodgkin_info,data.hodgkin)

    if data.trombocitosis:
        mostrar_enfermedad("Trombocitosis Primaria",data.trombo_primaria_info,data.trombo_primaria)
        if plaquetas>450000:
            mostrar_enfermedad("Trombocitosis Secundaria",data.trombo_secundaria_info,data.trombo_secundaria)
    if data.trombocitopenia:
        st.write("Posible diagnostico: Trombocitopenia")
        st.write(data.trombo_central_info)
        st.write(data.trombo_periferica_info)


def mostrar_resultados_orina():
    color=st.selectbox("Color:",["Amarillo","Transparente","Amarillo Oscuro","Marron","Rojo"])
    ph=st.slider("pH:", 4.5, 8.0, 6.2, step=0.1,help="Si sus niveles de PH es mayor o menor al rango propuesto, coloque el indicador en una esquina")
    densidad=st.slider("Densidad:", 1.000, 1.035, 1.010, step=0.001,help="Si sus niveles de DENSIDAD es mayor o menor al rango propuesto, coloque el indicador en una esquina")
    proteinas=st.selectbox("Proteina:",["Negativo","Positivo"])
    glucosa=st.selectbox("Glucosa:",["Negativo","Positivo"])
    sangre=st.selectbox("Presencia de sangre:",["Negativo","Positivo"])
    
    sumbit_button_two=st.form_submit_button("EVALUAR")

    if sumbit_button_two: 
        #Funcion que regresa todos los datos almacenados en "data.py" a su estado inicial
        reiniciar_data() 

        #Diagnostica los sintomas presentados
        diagnostico_color(color)
        diagnostico_ph(ph)
        diagnostico_densidad(densidad)
        diagnostico_proteinas(proteinas)
        diagnostico_glucosa(glucosa)
        diagnostico_sangre(sangre)

        st.write("---------------------------------------------------------------")

        #Muestra el posible diagnostico
        mostrar_enfermedad_v_orina("Orina color amarillo.",data.color_amaril_info,data.color_amaril)
        mostrar_enfermedad_v_orina("Orina transparente.",data.color_transp_info,data.color_transp)
        mostrar_enfermedad_v_orina("Orina color amarillo oscuro.",data.color_a_oscu_info,data.color_a_oscu)
        mostrar_enfermedad_v_orina("Orina color marron.",data.color_marron_info,data.color_marron)
        mostrar_enfermedad_v_orina("Orina color rojo",data.color_rojo_info,data.color_rojo)

        mostrar_enfermedad_v_orina("PH ACIDO",data.ph_baj_info,data.ph_baj)
        mostrar_enfermedad_v_orina("PH ALCALINO",data.ph_alt_info,data.ph_alt)
        mostrar_enfermedad_v_orina("DENSIDAD BAJA",data.den_baj_info,data.den_baj)
        mostrar_enfermedad_v_orina("DENSIDAD ALTA",data.den_alt_info,data.den_alt)
        mostrar_enfermedad_v_orina("PROTEINAS POSITIVA",data.prot_pos,data.proteinas)
        mostrar_enfermedad_v_orina("GLUCOSA POSITIVA",data.gluc_pos,data.glucosa)
        mostrar_enfermedad_v_orina("SANGRE POSITIVA",data.sang_pos,data.sangre)
        
    



def mostrar_enfermedad(enfermedad, descripcion, estado):
    if estado==True:
        st.info(f"Posible diagnostico: {enfermedad}")
        st.write(descripcion)

def mostrar_enfermedad_v2(enfermedad, descripcion, conteo):
    if conteo>1:
        st.info(f"Posible diagnostico: {enfermedad}")
        st.write(descripcion)
#Diagnostico de sintomas

#Serie roja
def diagnostico_hematies(hematies):
    if hematies<data.hemat_li:
        st.error("Globulos rojos por debajo del rango normal")
        data.anemia=True
    elif hematies>=data.hemat_li and hematies<=data.hemat_ls:
        st.success("Globulos rojos en el rango normal")
        
    else:
        st.error("Globulos rojos por encima del rango normal")
        data.poliglobulia=True


def diagnostico_hemoglobina(hemoglobina):
    if hemoglobina<data.hemog_li:
        st.error("Hemoglobina por debajo del rango normal")
        data.anemia=True
    elif hemoglobina>=data.hemog_li and hemoglobina<=data.hemog_ls:
        st.success("Hemoglobina en el rango normal")
        
    else:
        st.error("Hemoglobina por encima del rango normal")
        data.poliglobulia=True

def diagnostico_hematocrito(hematocrito):
    if hematocrito<data.hematoc_li:
        st.error("Hematocrito por debajo del rango normal")
        data.anemia=True
    elif hematocrito>=data.hematoc_li and hematocrito<=data.hematoc_ls:
        st.success("Hematocrito en el rango normal")

    else:
        st.error("Hematocrito por encima del rango normal")
        data.poliglobulia=True


def diagnostico_rdw(rdw):
    if rdw < data.rdw_li:
        st.error("RDW por debajo del rango normal")
        data.malformacion=True
    elif rdw>=data.rdw_li and rdw<=data.rdw_ls:
        st.success("RDW en el rango normal")
        
    else:
        st.error("RDW por encima del rango normal")
        data.malformacion=True


def diagnostico_reticulocitos(reticulocitos):
    if reticulocitos<data.ret_li:
        st.error("Reticulocitos por debajo del rango normal")
        data.a_arregen=True
    elif reticulocitos>=data.ret_li and reticulocitos<=data.ret_ls:
        st.success("Reticulocitos en el rango normal")
        
    else:
        st.error("Reticulocitos por encima del rango normal")
        data.a_regen=True


def diagnostico_vcm(vcm):
    if vcm<data.vcm_li:
        st.warning("VCM por debajo del rango normal")  
        data.a_micro=True
        data.a_normo=False
        data.a_macro=False
    elif vcm>=data.vcm_li and vcm<=data.vcm_ls:
        st.warning("VCM en el rango normal")
        
    else:
        st.warning("VCM por encima del rango normal")
        data.a_macro=True
        data.a_micro=False
        data.a_normo=False

#Serie blanca
def diagnostico_glob_blancos(glob_blancos):
    if glob_blancos<data.gb_li:
        st.error("Globulos blancos por debajo del rango normal")
        data.sepsis+=1
        data.enf_autoinmune+=1
    elif glob_blancos>=data.gb_li and glob_blancos<=data.gb_ls:
        st.success("Globulos blancos em el rango normal")
    else:
        st.error("Globulos blancos por encima del rango normal")
        data.infeccion+=2
        data.inflamacion+=1

def diagnostico_neutrofilos(neut):
    if neut<data.neut_li:
        st.error("Neutrofilos por debajo del rango normal")
        data.neutropenia=True
    elif neut>=data.neut_li and neut<=data.neut_ls:
        st.success("Nneutrofilos en el rango normal")
        #data.neutropenia=False
    else:
        st.error("Neutrofilos por encima del rango normal")
        data.infeccion+=1


def diagnostico_linfocitos(linf):
    if linf<data.linf_li:
        st.error("Linfocitos por debajo del rango normal")
        data.sepsis+=1
        data.hodgkin+=1
    elif linf>=data.linf_li and linf<=data.linf_ls:
        st.success("Linfocitos en el rango normal")
    else:
        st.error("Linfocitos por encima del rango normal")
        data.infeccion+=1
        data.inflamacion+=1

def diagnostico_monocitos(mono):
    if mono<data.mono_li:
        st.error("Monocitos por debajo del rango normal")
        data.infeccion+=1
        data.hemopatias+=1
    elif mono>=data.mono_li and mono<=data.mono_ls:
        st.success("Monocitos en el rango normal")
    else:
        st.error("Monocitos por encima del rango normal")
        data.infeccion+=1
        data.hemopatias+=1
        data.enf_autoinmune+=1

def diagnostico_eosinofilos(eosi):
    if eosi<data.eosi_li:
        st.error("Eosinofilos por debajo del rango normal")
        data.infeccion+=1
        data.cushing+=1
    elif eosi>=data.eosi_li and eosi<=data.eosi_ls:
        st.success("Eosinofilos en el rango normal")
    else:
        st.error("Eosinofilos por encima del rango normal")
        data.infeccion+=1
        data.hodgkin+=1
        data.hemopatias+=1

def diagnostico_basofilos(baso):
    if baso<data.baso_li:
        st.error("Basofilos por debajo del rango normal")
    elif baso>=data.baso_li and baso<=data.baso_ls:
        st.success("Basofilos en el rango normal")
    else:
        st.error("Basofilos por encima del rango normal")
        data.cushing+=1

#Plaquetas
def diagnostico_plaquetas(plaq):
    if plaq<data.plaq_li:
        st.error("Plaquetas por debajo del rango normal")
        data.trombocitopenia=True
    elif plaq>=data.plaq_li and plaq<=data.plaq_ls:
        st.success("Plaquetas en el rango normal")
    else:
        st.error("Plaquetas por encima del rango normal")
        data.trombocitosis=True


#---------- Diagnostico Orina------------------------------#
def diagnostico_color(col):
    if col=="Amarillo":
        st.success(f"Orina color {col}")
        data.color_amaril=True
    if col=="Transparente":
        st.warning(f"Orina color {col}")
        data.color_transp=True
    if col=="Amarillo Oscuro":
        st.warning(f"Orina color {col}")
        data.color_a_oscu=True
    if col=="Marron":
        st.warning(f"Orina color {col}")
        data.color_marron=True
    if col=="Rojo":
        st.error(f"Orina color {col}")
        data.color_rojo=True

def diagnostico_ph(ph):
    if ph<=data.ph_li:
        st.warning("PH acido")
        data.ph_baj=True
        data.ph_alt=False
    elif ph>=data.ph_ls:
        st.warning("PH alcalino")
        data.ph_alt=True
        data.ph_baj=False
    else:
        data.ph_baj=False
        data.ph_alt=False
        st.success("PH normal")

def diagnostico_densidad(den):
    if den<=data.den_li:
        st.warning("DENSIDAD baja")
        data.den_baj=True
        data.den_alt=False
    elif den>=data.den_ls:
        st.warning("DENSIDAD alta")
        data.den_baj=False
        data.den_alt=True
    else:
        st.success("DENSIDAD normal")

def diagnostico_proteinas(pt):
    if pt=="Negativo":
        st.success(f"Sin presencia de PROTEINAS")
        data.proteinas=False
    elif pt=="Positivo":
        st.warning(f"Presencia de PROTEINAS")
        data.proteinas=True

def diagnostico_glucosa(pt):
    if pt=="Negativo":
        st.success(f"Sin presencia de GLUCOSA")
        data.glucosa=False
    elif pt=="Positivo":
        st.warning(f"Presencia de GLUCOSA")
        data.glucosa=True

def diagnostico_sangre(pt):
    if pt=="Negativo":
        st.success(f"Sin presencia de SANGRE")
        data.sangre=False
    elif pt=="Positivo":
        st.error(f"Presencia de SANGRE")
        data.sangre=True

def mostrar_enfermedad_v_orina(nombre, informacion, estado):
    if estado==True:
        st.info(f"{nombre}.")
        st.write(informacion)

def reiniciar_data():
    data.anemia=False
    data.poliglobulia=False
    data.malformacion=False
    data.a_regen=False   
    data.a_arregen=False
    data.a_macro=False
    data.a_normo=False
    data.a_micro=False
    data.a_def_hierro=False
    data.beta_talasemia=False
    data.infeccion=0
    data.inflamacion=0
    data.sepsis=0
    data.enf_autoinmune=0
    data.neutropenia=False
    data.hemopatias=0
    data.cushing=0
    data.hodgkin=0
    data.trombocitosis=False
    data.trombo_primaria=False
    data.trombo_secundaria=False #(>450000)
    data.trombocitopenia=False
    data.trombo_central=False
    data.trombo_periferica=False

    data.color_amaril=False
    data.color_transp=False
    data.color_a_oscu=False
    data.color_marron=False
    data.color_rojo=False
    data.ph_alt=False
    data.ph_baj=False
    data.den_alt=False
    data.den_baj=False
    data.proteinas=False
    data.glucosa=False
    data.sangre=False