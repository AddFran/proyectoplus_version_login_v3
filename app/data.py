import streamlit as st

#------------------------------- VALORES ------------------------------------------------------------------------------------------#

#SERIE ROJA
hemat_li=4.9  
hemat_ls=6.1  
hemog_li=14.0  
hemog_ls=18.0  
hematoc_li=42.0 
hematoc_ls=52.0 
vcm_li=80.0 
vcm_ls=100.0 
hcm_li=27.0
hcm_ls=33.0
ccmh_li=32.0
ccmh_ls=36.0
rdw_li=11.0
rdw_ls=15.0
ret_li=0.5
ret_ls=1.5

#SERIE BLANCA
#Numeros
gb_ls=10000.0
gb_li=6000.0
neut_ls=5000.0
neut_li=3000.0
linf_ls=4000.0
linf_li=1500.0
mono_ls=500.0
mono_li=100.0
eosi_ls=350.0
eosi_li=20.0
baso_ls=100.0
baso_li=10.0
#Porcentaje %
gbp=100.0
neutp_ls=65.0
neutp_li=55.0
linfp_ls=35.0
linfp_li=25.0
monop_ls=8.0
monop_li=4.0
eosip_ls=4.0
eosip_li=0.5
basop_ls=1.0
basop_li=0.5


#PLAQUETAS
plaq_li=150000.0
plaq_ls=300000.0

#-------- SINTOMAS -------------------------------------------------#

#Serie roja
hemat_alt=False
hemat_baj=False

hemog_alt=False
hemog_baj=False

hematoc_alt=False
hematoc_baj=False

vcm_alt=False
vcm_reg=False
vcm_baj=False

hcm_alt=False
hcm_reg=False
hcm_baj=False

rdw_alt=False
rdw_reg=False
rdw_baj=False

ret_alt=False
ret_baj=False



#Serie blanca
glob_blancos_alt=False
glob_blancos_baj=False

neut_alt=False
neut_baj=False

linf_alt=False
linf_baj=False

mono_alt=False
mono_baj=False

eosi_alt=False
eosi_baj=False

baso_alt=False
baso_baj=False


#Plaquetas
plaq_alt=False
plaq_baj=False


#------------- OTROS VALORES ---------------------------------#

indice_mentzer=0.0


#------------- SINTOMAS ------------------------------------#
#Version xd

#Hematies, hemoglobina y hematocrito
anemia=False
anemia_info="""Afección que se desarrolla cuando la sangre produce una cantidad inferior a la normal 
            de glóbulos rojos sanos. Si tiene anemia, su cuerpo no obtiene suficiente cantidad de 
            sangre rica en oxígeno. La falta de oxígeno puede hacer que se sienta cansado o débil."""

poliglobulia=False
poliglobulia_info="""Indica un exceso de producción de hematíes o glóbulos rojos. De hecho, la denominación 
            correcta para definir esta situación es eritrocitosis. Coloquialmente también se le llama 
            sangre espesa. Es el principal sintoma de POLICITEMIA VERA. Si experimentas síntomas como DOLOR 
            DE CABEZA, MAREOS, FATIGA, ENROJECIMIENTO FACIAL o DIFICULTADES PARA RESPIRAR, se recomienda buscar
            ayuda medica inmediata."""

#RDW
malformacion=False
malf_info="""La prueba de amplitud de distribución eritrocitaria (RDW, por sus siglas en inglés) 
            es un análisis que mide cuanto varía el volumen y el tamaño de sus glóbulos rojos (eritrocitos). 
            Las diferencias en el tamaño de los glóbulos rojos pueden afectar la capacidad de estos para 
            transportar oxígeno a través del cuerpo."""

#Reticulocitos
a_regen=False   
a_regen_info="""es una condición en la que la médula ósea responde a la disminución de glóbulos rojos 
            aumentando la producción de nuevas células sanguíneas. Esto se produce cuando hay una pérdida 
            o destrucción de globulos rojos, lo que puede ser causado por hemorragia o hemólisis."""   

a_arregen=False
a_arregen_info="""Es un tipo de anemia caracterizada por una disminución o ausencia de producción de glóbulos 
            rojos en la medula osea, es decir, la médula ósea no responde adecuadamente a la falta de 
            glóbulos rojos y no produce nuevos eritrocitos, lo que agrava la anemia."""   

#VCM
a_macro=False
a_macro_info="""Afección en la que los glóbulos rojos son más grandes de lo normal, lo que se conoce tambien como 
            macrocitosis o megalocitosis."""

a_normo=False
a_normo_info="""Afección en la que los glóbulos rojos tienen un tamaño normal, pero no hay la cantidad 
            suficiente. Se asocia con una gran variedad de trastornos, generalmente de curso crónico,"""

a_micro=False
a_micro_info="""afección que se caracteriza por la presencia de glóbulos rojos más pequeños de lo normal. 
            Esto puede afectar la capacidad de la sangre para transportar oxígeno."""

a_def_hierro=False
a_def_hierro_info="""La anemia por deficiencia de hierro es un tipo frecuente de anemia, trastorno en el cual 
            la sangre no tiene la cantidad suficiente de glóbulos rojos sanos. Sin el hierro necesario, el organismo 
            no puede producir una cantidad suficiente de hemoglobina, sustancia presente en los glóbulos rojos que 
            les permite transportar oxígeno. Como consecuencia, la anemia por deficiencia de hierro puede hacerte 
            sentir cansado y con dificultad para respirar."""

beta_talasemia=False
beta_talasemia_info="""La talasemia es un grupo de trastornos hereditarios de la sangre que afectan la producción 
            de hemoglobina, la proteína de los glóbulos rojos encargada de transportar oxígeno en el cuerpo.
            Se caracteriza por la producción inadecuada de cadenas de globina (alfa o beta), lo que provoca glóbulos 
            rojos pequeños (microcíticos) y una anemia crónica de distinta gravedad, dependiendo del tipo de talasemia."""




infeccion=0
infeccion_info="""Invasión y multiplicación de microorganismos, como bacterias, virus, hongos o parásitos, en el cuerpo humano. 
            Las infecciones pueden comenzar en cualquier parte del cuerpo y propagarse por todo el organismo. Pueden causar fiebre, 
            malestar, daño a órganos y tejidos, o enfermedad."""

inflamacion=0
inflamacion_info="""Respuesta natural del cuerpo a una lesión, infección u otra afección médica. Se produce cuando el cuerpo produce sustancias 
            químicas que desencadenan una respuesta inmunitaria para combatir la infección o reparar el tejido dañado."""

sepsis=0
sepsis_info="""Es la respuesta abrumadora y extrema de su cuerpo a una infección. La sepsis es una emergencia médica que puede ser 
            mortal. Sin un tratamiento rápido, puede provocar daños en los tejidos, falla orgánica e incluso la muerte. Se recomienda
            asistir al centro de salud mas cercano."""

enf_autoinmune=0
enf_autoinmune_info="""Conjunto de afeccines en las que el sistema inmunologico ataca por error a las celulas sanas del organismo."""

neutropenia=False
neutropenia_info="""Presencia de un número anormalmente bajo de neutrófilos (un tipo de glóbulos blancos) en la sangre. Si es grave, aumenta de 
            manera importante el riesgo de padecer una infección potencialmente mortal. A menudo es un efecto adverso del tratamiento 
            del cáncer con quimioterapia o radioterapia."""

hemopatias=0
hemopatias_info="""Conjunto de enfermedades de la sangre que se caracterizan por trastornos en la multiplicación y diferenciación de 
            las células hematopoyéticas."""

cushing=0
cushing_info="""Trastorno hormonal que se produce cuando el cuerpo tiene niveles elevados de cortisol, una hormona producida por las 
            glándulas suprarrenales."""

hodgkin=0
hodgkin_info="""Tipo de cáncer que se desarrolla en el sistema linfático. Su sistema linfático es parte de su sistema inmunitario. 
            Ayuda a proteger su cuerpo de infecciones y enfermedades."""



trombocitosis=False

trombo_primaria=False
trombo_primaria_info="""Es una enfermedad de la sangre y la médula ósea que se caracteriza por un aumento en el número de plaquetas. 
            """

trombo_secundaria=False #(>450000)
trombo_secundaria_info="""La trombocitemia secundaria es una cantidad excesiva de plaquetas en el torrente sanguíneo que aparece como consecuencia 
            de otro trastorno y que con muy poca frecuencia conduce a una coagulación sanguínea o una hemorragia excesivas."""

trombocitopenia=False

trombo_central=False
trombo_central_info="""En este tipo de trombocitopenia, el número de plaquetas disminuye y se asocia con alteraciones en otras células sanguíneas."""

trombo_periferica=False
trombo_periferica_info="""En este caso, el examen del frotis periférico es importante para descartar seudotrombocitopenia, que puede ser causada por la 
            aglomeración de plaquetas por el reactivo EDTA presente en los tubos de recolección de sangre. """



#Examen de orina 

ph_li=4.5
ph_ls=8.0

den_li=1.00
den_ls=1.03


color_amaril=False
color_transp=False
color_a_oscu=False
color_marron=False
color_rojo=False

ph_alt=False
ph_baj=False
den_alt=False
den_baj=False
proteinas=False
glucosa=False
sangre=False

#Mensajes 
#Color
color_amaril_info="Color normal, significativo de nada grave, al menos a simple vista."
color_transp_info="Orina muy diluida, exceso de líquidos, se recomienda consumir menos agua."
color_a_oscu_info="Deshidratación, orina concentrada"
color_marron_info="Presencia de bilirrubina, problemas hepáticos"
color_rojo_info="""Presencia de sangre, hematuria. La hematuria es la presencia de sangre en la 
            orina. Puede ser visible a simple vista o solo ser detectable con un microscopio o en un 
            análisis de orina."""

#info
ph_baj_info="""El pH mide la acidez o alcalinidad de la orina. El PH acido o bajo puede ser indicios 
            de una dieta alta en proteínas, acidosis metabólica o diabetes no controlada."""

ph_alt_info="""El pH mide la acidez o alcalinidad de la orina. El PH alcalino o alto puede ser indicio
            de infecciones del tracto urinario (bacterias que descomponen la urea), dieta vegetariana
            o alcalosis metabólica """

den_baj_info="""La densidad refleja la concentración de partículas en la orina. La baja densidad es indicio
            de orina diluida (exceso de líquidos) o diabetes insípida Daño renal (incapacidad para concentrar orina)."""

den_alt_info="""La densidad refleja la concentración de partículas en la orina. La alta densidad es indicio
            de orina concentrada (deshidratación), diabetes mellitus (glucosa en orina) o exceso de proteínas."""

prot_pos="""La presencia de proteínas en la orina puede indicar daño renal (glomerulonefritis, síndrome nefrótico),
            hipertensión, diabetes mellitus o infecciones urinarias."""

gluc_pos="""La glucosa en orina es signo de hiperglucemia, ademas, es indicio de diabetes mellitus no controlada,
            Síndrome de Cushing, hipertiroidismo, estrés o embarazo (glucosuria fisiológica)."""

sang_pos="""La sangre en orina (hematuria) puede ser microscópica o visible. Es indicativo de o	Infecciones urinarias, 
            cálculos renales, traumatismos, glomerulonefritis, cáncer de vejiga o riñón o ejercicio extremo 
            (hematuria de esfuerzo)."""