# crear_csv_qoylluriti.py
# Script completo para crear todos los archivos CSV necesarios

import os

def crear_csv_qoylluriti():
    """Crea todos los archivos CSV necesarios para Qoyllur Riti"""
    
    print("="*60)
    print("CREANDO ARCHIVOS CSV PARA QOYLLUR RITI")
    print("="*60)
    
    # Crear directorio
    os.makedirs('csv_qoylluriti_completo', exist_ok=True)
    
    # ==================== 1. ARCHIVO MARCOS ====================
    contenido_marcos = """ID,NOMBRE,ORDEN,FECHA
Dia1_SabadoPreparacion,Día 1: Sábado de preparación,1,2025-06-14
Dia2_DomingoPartida,Día 2: Domingo de partida y viaje,2,2025-06-15
Dia3_LunesAscenso,Día 3: Lunes de ascenso al santuario,3,2025-06-16
NocheLunesMartes_Glaciar,Noche del lunes al martes (en el glaciar),4,2025-06-16
Dia4_MartesDescensoYLomada,Día 4: Martes de descenso e inicio de la lomada,5,2025-06-17
NocheMartesMiercoles_Lomada,Noche del martes al miércoles (durante la lomada),6,2025-06-17
Dia5_MiercolesAlba,Día 5: Miércoles del alba y finalización,7,2025-06-18"""
    
    with open('csv_qoylluriti_completo/marcos.csv', 'w', encoding='utf-8') as f:
        f.write(contenido_marcos)
    print("✅ Creado: marcos.csv")
    
    # ==================== 2. ARCHIVO EVENTOS ====================
    contenido_eventos = """MARCO,ID,NOMBRE,ORDEN,HORA_APROX,DESCRIPCION_CORTA
Dia1_SabadoPreparacion,EventoPrevioPeregrinaje_Paucartambo_2025_06_14,Evento previo al peregrinaje (2025),1,14:00,Gelación y ensayo de participantes en Paucartambo
Dia2_DomingoPartida,MisaInicial_Paucartambo_2025,Misa inicial en Paucartambo (2025),1,07:00,Misa de envío en la iglesia de Paucartambo
Dia2_DomingoPartida,RomeriaPaucartambo_2025_06_15,Romería en Paucartambo (2025),2,08:30,Romería al cementerio para honrar hermanos antiguos
Dia2_DomingoPartida,RitualVestimentaDanzantes_2025,Ritual de vestimenta de danzantes (2025),3,12:00,Los danzantes se visten con trajes ceremoniales en la plaza
Dia2_DomingoPartida,ParadaHuancarani_2025,Parada en Huancarani (2025),4,14:00,Reunión y espera de todos los danzantes en cruce vial
Dia2_DomingoPartida,VisitaIglesiaCcatcca_2025,Visita a la iglesia de Ccatcca (2025),5,15:00,Visita ritual a la iglesia marcando el paso por el pueblo
Dia2_DomingoPartida,ComidaCcatcca_2025,Comida comunitaria en Ccatcca (2025),6,16:00,Descanso y comida (asado con mote) en la plaza de Ccatcca
Dia2_DomingoPartida,PasoCasaPrioste,Paso por la casa del prioste (2025),7,18:00,Visita al prioste en Ocongate, quien sirve mate caliente
Dia2_DomingoPartida,ViajeVehicular_Paucartambo_Mahuayani_2025,Viaje vehicular a Mahuayani (2025),8,19:00,Viaje ritual en camión con paradas establecidas
Dia2_DomingoPartida,Caminata_Mahuayani_Santuario_2025,Caminata Mahuayani-Santuario (2025),9,05:00,Ascenso a pie desde Mahuayani al santuario
Dia3_LunesAscenso,MisaUkukus_2025,Misa de Ukukus (2025),2,10:00,Misa especial exclusiva para los Ukukus
Dia3_LunesAscenso,Pachakunapata,P'achakunapata,3,11:00,Espera ceremonial y entrada unificada al santuario
Dia3_LunesAscenso,CeremoniaVeneracion_Templo_Qoylluriti_2025,Veneración en el templo del santuario (2025),4,12:00,Actos de veneración al Señor de Qoyllur Rit'i
Dia3_LunesAscenso,ProcesionMamachapata_2025,Procesión a Mamachapata (2025),5,14:00,Procesión con imagen del Señor de Tayankani
Dia3_LunesAscenso,DescansoCeldaUkukus_2025,Descanso en celda de Ukukus (2025),6,16:00,Descanso y preparación en la celda del bofedal
NocheLunesMartes_Glaciar,SubidaColquePunku_2025,Subida al Colque Punku (2025),1,23:00,Ascenso nocturno al glaciar para rituales
Dia4_MartesDescensoYLomada,BajadaColquePunku_2025,Bajada del Colque Punku (2025),1,09:00,Descenso desde el glaciar al santuario
Dia4_MartesDescensoYLomada,RitualMachuCruz_2025,Ritual en Machu Cruz (2025),2,10:00,Pausa ritual para comer maíz y queso en despedida
Dia4_MartesDescensoYLomada,RitualDespedida_Yanaqocha_2025,Ritual de despedida en Yanaqocha (2025),3,11:00,Rituales de despedida en la laguna Yanaqocha
Dia4_MartesDescensoYLomada,DescansoYanaqancha_2025,Descanso en Yanaqancha (2025),4,15:00,Descanso prolongado de 4 horas en Yanaqancha
Dia4_MartesDescensoYLomada,Lomada_2025,Lomada / Loman Pureq (2025),5,21:00,Caminata ritual de 24 horas con hitos específicos
NocheMartesMiercoles_Lomada,CantoQespiCruz_2025,Canto en Q'espi Cruz (2025),1,00:00,Canto de la Canción de Despedida a medianoche
NocheMartesMiercoles_Lomada,EscaleraChayoq,EscaleraChayoq,2,02:00,Bajada de piedras entre las 3 y 4 de la madrugada
Dia5_MiercolesAlba,IntiAlabado_2025,Inti Alabado (2025),1,04:00,Ritual de saludo al sol al amanecer
Dia5_MiercolesAlba,RitualGrutaTayankani_2025,Ritual en gruta de Tayankani (2025),2,07:00,Últimos rituales de Ukukus antes del ingreso procesional
Dia5_MiercolesAlba,DejaImagenEnCapillaTayancani_2025,Dejar imagen en capilla de Tayancani (2025),3,09:00,Depósito de la imagen en la capilla de Tayankani
Dia5_MiercolesAlba,TrasladoImagenSenorOcongate_Tayancani_2025,Traslado de la imagen a Ocongate (2025),4,11:00,Procesión con imagen desde Tayankani hacia Ocongate
Dia5_MiercolesAlba,ProcesionEntradaOcongate_2025,Procesión de entrada a Ocongate (2025),5,13:00,Procesión final que marca el término oficial"""
    
    with open('csv_qoylluriti_completo/eventos.csv', 'w', encoding='utf-8') as f:
        f.write(contenido_eventos)
    print("✅ Creado: eventos.csv (28 eventos)")
    
    # ==================== 3. ARCHIVO LUGARES ====================
    contenido_lugares = """ID,NOMBRE,TIPO
Paucartambo,Paucartambo,Pueblo
IglesiaPaucartambo,Iglesia de Paucartambo,Iglesia
CementerioPaucartambo,Cementerio de Paucartambo,Cementerio
PlazaPaucartambo,Plaza de Armas de Paucartambo,Plaza
SantuarioQoylluriti,Santuario del Señor de Qoyllur Rit'i,Santuario
ColquePunku,Glaciar Colque Punku,Glaciar
MachuCruz,Machu Cruz,Punto Ritual
Yanaqocha,Laguna Yanaqocha,Laguna
Yanaqancha,Yanaqancha,Lugar de Descanso
QespiCruz,Q'espi Cruz,Punto Ritual
QquchiyocWayqo,Qquchiyoc Wayq'o,Riachuelo
IntiLloksimuy,Inti Lloksimuy,Punto Solar
Tayancani,Tayancani,Pueblo
Ocongate,Ocongate,Pueblo
PlazaCcatcca,Plaza de Armas de Ccatcca,Plaza
IglesiaCcatcca,Iglesia de Ccatcca,Iglesia
Huancarani,Huancarani,Cruce Vial
Mahuayani,Mahuayani,Punto de Inicio
CeldaUkukusPaucartambo,Celda de los Ukukus de Paucartambo,Alojamiento
Mamachapata,Mamachapata,Área Ritual
CapillaTayankani,Capilla de Tayankani,Capilla
GrutaTayankani,Gruta de Tayankani,Gruta
PlazaOcongate,Plaza de Ocongate,Plaza
CasaPriosteOcongate,Casa del Prioste en Ocongate,Residencia
Caicay,Caicay,Distrito
Challabamba,Challabamba,Distrito
Colquepata,Colquepata,Distrito
Ccapi,Ccapi,Localidad
Ccarhuayo,Ccarhuayo,Localidad
Ccatcca,Ccatcca,Pueblo
Mollomarca,Mollomarca (sector alto de Paucartambo),Comunidad
GrutaYanaqancha,Gruta de Yanaqancha,Gruta
RutaPaucartamboMahuayani,Ruta Paucartambo - Mahuayani,Ruta
ViajeVehicular_Paucartambo_Mahuayani_2025,Viaje vehicular a Mahuayani (2025),Evento-Lugar
Lomada_2025,Lomada / Loman Pureq (2025),Evento-Ruta
IntiAlabado_2025,Inti Alabado (2025),Evento-Punto
Escalerachayoq,EscaleraChayoq,Evento-Tramo
Pachakunapata,P'achakunapata,Evento-Lugar"""
    
    with open('csv_qoylluriti_completo/lugares.csv', 'w', encoding='utf-8') as f:
        f.write(contenido_lugares)
    print("✅ Creado: lugares.csv (39 lugares)")
    
    # ==================== 4. ARCHIVO PARTICIPANTES ====================
    contenido_participantes = """ID,NOMBRE,TIPO
NacionPaucartambo,Nación Paucartambo,Nacion
Ukumaris_Paucartambo_2025,Ukumaris de Paucartambo (2025),Ukumari
DanzaUkumari,Danza del Ukumari,Danza
TrajeUkumari,Traje de Ukumari,Vestimenta
Sorriago,Sorriago,ObjetoRitual"""
    
    with open('csv_qoylluriti_completo/participantes.csv', 'w', encoding='utf-8') as f:
        f.write(contenido_participantes)
    print("✅ Creado: participantes.csv (5 participantes)")
    
    # ==================== 5. ARCHIVO PRACTICAS ====================
    contenido_practicas = """ID,NOMBRE
Misa,Misa católica
Procesion,Procesión
Danza,Danza ritual
Vestimenta,Vestimenta ceremonial
Comida,Comida ritual
Canto,Canto ritual
Romeria,Romería
AscensoDescenso,Ascenso/Descenso ritual
Descanso,Descanso ritual
Viaje,Viaje ritual
Gelacion,Gelación
Espera,Espera ritual
Anuncio,Anuncio público
Despedida,Despedida ritual
Alabado,Alabado al sol
Visita,Visita ritual"""
    
    with open('csv_qoylluriti_completo/practicas.csv', 'w', encoding='utf-8') as f:
        f.write(contenido_practicas)
    print("✅ Creado: practicas.csv (16 prácticas)")
    
    # ==================== 6. ARCHIVO FOTOS ====================
    contenido_fotos = """ID_FOTO,NOMBRE_ARCHIVO,FORMATO,FECHA_CAPTURA,HORA_CAPTURA,MARCO_TEMPORAL,EVENTO_ESPECIFICO,LUGAR,PARTICIPANTE,PRACTICA,DESCRIPCION,ANGULO,PERSONAS,OBJETOS,ESTADO,URL_GITHUB,NOTAS
IMG_001,ejemplo_001.jpg,image/jpeg,2025-06-15,07:30,Dia2_DomingoPartida,MisaInicial_Paucartambo_2025,IglesiaPaucartambo,NacionPaucartambo,Misa,Ukumaris arrodillados durante misa de envío,Interior,15,velas,cruces,Por subir,,Foto tomada desde el coro
IMG_002,ejemplo_002.jpg,image/jpeg,2025-06-15,08:45,Dia2_DomingoPartida,RomeriaPaucartambo_2025_06_15,CementerioPaucartambo,NacionPaucartambo,Romeria,Ukumaris rezando frente a tumbas,Exterior,8,flores,velas,Por subir,,Buen día, luz natural
IMG_003,ejemplo_003.jpg,image/jpeg,2025-06-15,12:15,Dia2_DomingoPartida,RitualVestimentaDanzantes_2025,PlazaPaucartambo,Ukumaris_Paucartambo_2025,Vestimenta,Ukumari ayudando a otro con máscara,Detalle,2,mascara,traje,Por subir,,Enfoque en las manos
IMG_004,ejemplo_004.jpg,image/jpeg,2025-06-15,14:30,Dia2_DomingoPartida,ParadaHuancarani_2025,Huancarani,NacionPaucartambo,Espera,Grupo completo esperando en cruce vial,Panorámica,25,vehículos,mochilas,Por subir,,Vista general
IMG_005,ejemplo_005.jpg,image/jpeg,2025-06-15,15:20,Dia2_DomingoPartida,VisitaIglesiaCcatcca_2025,IglesiaCcatcca,Ukumaris_Paucartambo_2025,Visita,Ukumaris entrando en procesión a iglesia,Exterior,12,sorriagos,cruces,Por subir,,Secuencia de entrada
IMG_006,ejemplo_006.jpg,image/jpeg,2025-06-15,16:45,Dia2_DomingoPartida,ComidaCcatcca_2025,PlazaCcatcca,Ukumaris_Paucartambo_2025,Comida,Grupo compartiendo asado con mote,Exterior,10,comida,platos,Por subir,,Momento de camaradería
IMG_007,ejemplo_007.jpg,image/jpeg,2025-06-15,18:30,Dia2_DomingoPartida,PasoCasaPrioste,CasaPriosteOcongate,NacionPaucartambo,Visita,Recepción por el prioste con mate caliente,Interior,5,mate,vasijas,Por subir,,Interior de casa
IMG_008,ejemplo_008.jpg,image/jpeg,2025-06-16,05:30,Dia3_LunesAscenso,Caminata_Mahuayani_Santuario_2025,Mahuayani,Ukumaris_Paucartambo_2025,Viaje,Ascenso a pie al santuario al amanecer,Exterior,8,mochilas,bastones,Por subir,,Amanecer
IMG_009,ejemplo_009.jpg,image/jpeg,2025-06-16,10:15,Dia3_LunesAscenso,MisaUkukus_2025,SantuarioQoylluriti,Ukumaris_Paucartambo_2025,Misa,Ukumaris arrodillados en misa especial,Exterior,40,,glaciar,Por subir,,Vista con glaciar al fondo
IMG_010,ejemplo_010.jpg,image/jpeg,2025-06-16,11:30,Dia3_LunesAscenso,Pachakunapata,Pachakunapata,NacionPaucartambo,Espera,Espera ceremonial antes de entrada,Exterior,30,banderas,insignias,Por subir,,Momento solemne
IMG_011,ejemplo_011.jpg,image/jpeg,2025-06-16,23:30,NocheLunesMartes_Glaciar,SubidaColquePunku_2025,ColquePunku,Ukumaris_Paucartambo_2025,AscensoDescenso,Ascenso nocturno al glaciar con antorchas,Noche,5,antorchas,crampones,Por subir,,Foto nocturna
IMG_012,ejemplo_012.jpg,image/jpeg,2025-06-17,09:15,Dia4_MartesDescensoYLomada,BajadaColquePunku_2025,ColquePunku,Ukumaris_Paucartambo_2025,AscensoDescenso,Descenso del glaciar al amanecer,Exterior,8,nieve,palas,Por subir,,Amanecer hermoso
IMG_013,ejemplo_013.jpg,image/jpeg,2025-06-17,10:30,Dia4_MartesDescensoYLomada,RitualMachuCruz_2025,MachuCruz,NacionPaucartambo,Comida,Grupo comiendo maíz y queso en despedida,Detalle,6,comida,cruz,Por subir,,Ritual simbólico
IMG_014,ejemplo_014.jpg,image/jpeg,2025-06-17,11:45,Dia4_MartesDescensoYLomada,RitualDespedida_Yanaqocha_2025,Yanaqocha,NacionPaucartambo,Despedida,Abrazos y despedidas en la laguna,Exterior,4,,laguna,Por subir,,Momento emocional
IMG_015,ejemplo_015.jpg,image/jpeg,2025-06-17,15:30,Dia4_MartesDescensoYLomada,DescansoYanaqancha_2025,Yanaqancha,NacionPaucartambo,Descanso,Grupo descansando durante 4 horas,Exterior,12,imagen_religiosa,colchonetas,Por subir,,Descanso prolongado
IMG_016,ejemplo_016.jpg,image/jpeg,2025-06-18,00:15,NocheMartesMiercoles_Lomada,CantoQespiCruz_2025,QespiCruz,NacionPaucartambo,Canto,Canto de despedida a medianoche,Noche,20,,cruz,Por subir,,Foto nocturna con linternas
IMG_017,ejemplo_017.jpg,image/jpeg,2025-06-18,02:30,NocheMartesMiercoles_Lomada,EscaleraChayoq,Escalerachayoq,NacionPaucartambo,Viaje,Bajada de piedras durante la madrugada,Noche,8,,piedras,Por subir,,Tramo difícil
IMG_018,ejemplo_018.jpg,image/jpeg,2025-06-18,04:45,Dia5_MiercolesAlba,IntiAlabado_2025,IntiLloksimuy,NacionPaucartambo,Alabado,Saludo al sol al amanecer,Amanecer,25,,,Por subir,,Momento del amanecer
IMG_019,ejemplo_019.jpg,image/jpeg,2025-06-18,07:30,Dia5_MiercolesAlba,RitualGrutaTayankani_2025,GrutaTayankani,Ukumaris_Paucartambo_2025,Ritual,Últimos rituales de ukumaris en la gruta,Interior,3,velas,incienso,Por subir,,Espacio cerrado
IMG_020,ejemplo_020.jpg,image/jpeg,2025-06-18,11:30,Dia5_MiercolesAlba,ProcesionEntradaOcongate_2025,PlazaOcongate,NacionPaucartambo,Procesion,Entrada procesional final a Ocongate,Exterior,30,banderas,estandartes,Por subir,,Fin de la peregrinación"""
    
    with open('csv_qoylluriti_completo/fotos.csv', 'w', encoding='utf-8') as f:
        f.write(contenido_fotos)
    print("✅ Creado: fotos.csv (20 ejemplos)")
    
    # ==================== 7. ARCHIVO DE CONFIGURACIÓN ====================
    contenido_config = """# CONFIGURACIÓN PARA GOOGLE SHEETS
# ============================================

# PASOS PARA CONFIGURAR MENÚS DESPLEGABLES:

1. Importa cada CSV como pestaña separada en Google Sheets

2. En la pestaña FOTOS, configura estas validaciones de datos:

   COLUMNA F (MARCO_TEMPORAL):
   - Datos → Validación de datos
   - Criterio: Lista de un rango
   - Rango: marcos!$A$2:$A$100

   COLUMNA G (EVENTO_ESPECIFICO):
   - Datos → Validación de datos  
   - Criterio: Lista de un rango
   - Rango: eventos!$B$2:$B$100

   COLUMNA H (LUGAR):
   - Datos → Validación de datos
   - Criterio: Lista de un rango
   - Rango: lugares!$A$2:$A$100

   COLUMNA I (PARTICIPANTE):
   - Datos → Validación de datos
   - Criterio: Lista de un rango
   - Rango: participantes!$A$2:$A$100

   COLUMNA J (PRACTICA):
   - Datos → Validación de datos
   - Criterio: Lista de un rango
   - Rango: practicas!$A$2:$A$100

3. Para menús dependientes (eventos por marco):
   - Crea una pestaña llamada EVENTOS_FILTRADOS
   - En A1: =FILTER(eventos!$B$2:$B$100, eventos!$A$2:$A$100=FOTOS!$F2)
   - En FOTOS columna G, usa rango: EVENTOS_FILTRADOS!$A$2:$A$100

# ============================================
# ESTRUCTURA DE CARPETAS SUGERIDA PARA FOTOS:
# qoyllur_riti_2025/
# ├── Dia1_Sabado_Preparacion/
# ├── Dia2_Domingo_Partida/
# ├── Dia3_Lunes_Ascenso/
# ├── Dia4_Martes_Descenso/
# ├── Dia5_Miercoles_Alba/
# └── general/
# ============================================"""
    
    with open('csv_qoylluriti_completo/CONFIGURACION.txt', 'w', encoding='utf-8') as f:
        f.write(contenido_config)
    print("✅ Creado: CONFIGURACION.txt")
    
    print("\n" + "="*60)
    print("🎉 ¡ARCHIVOS CSV CREADOS EXITOSAMENTE!")
    print("="*60)
    print("\n📁 Carpeta: 'csv_qoylluriti_completo/'")
    print("\n📋 Archivos creados (6):")
    print("   1. marcos.csv       - Marcos temporales (7 días)")
    print("   2. eventos.csv      - 28 eventos con horas del relato")
    print("   3. lugares.csv      - 39 lugares con tipos")
    print("   4. participantes.csv- 5 participantes y danzas")
    print("   5. practicas.csv    - 16 prácticas culturales")
    print("   6. fotos.csv        - Plantilla con 20 ejemplos")
    print("   7. CONFIGURACION.txt- Instrucciones para Google Sheets")
    
    print("\n🚀 PASOS SIGUIENTES:")
    print("   1. Ve a Google Sheets → Archivo → Importar")
    print("   2. Sube cada CSV como pestaña separada")
    print("   3. Sigue las instrucciones en CONFIGURACION.txt")
    print("   4. Comienza a agregar tus fotos reales")
    print("="*60)

if __name__ == "__main__":
    crear_csv_qoylluriti()