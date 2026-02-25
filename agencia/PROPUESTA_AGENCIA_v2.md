# PROPUESTA DE MODELADO DE AGENCIA PARA QOYLLUR RIT'I
## Versión 2.0 - Mejorada

---

## 1. INTRODUCCIÓN

### 1.1 ¿Qué es agencia?

Capacidad de los participantes de actuar movidos por motivaciones, propósitos y roles específicos. No solo describir QUÉ hacen, sino POR QUÉ lo hacen.

**Preguntas clave:**
- ¿Por qué los ukukus suben al glaciar?
- ¿Qué motiva a las naciones a peregrinar?
- ¿Qué roles desempeñan y cómo cualifican sus acciones?

### 1.2 Gap actual

**Lo que ya tenemos:**
- Quién participa: `:participaEn`
- Dónde ocurre: `:ocurreEnLugar`
- Cuándo ocurre: `:defineMarcoTemporal`

**Lo que nos falta:**
- POR QUÉ actúan: motivaciones documentadas
- PARA QUIÉN actúan: beneficiarios
- DESDE QUÉ POSICIÓN: roles especializados

---

## 2. MODELO PROPUESTO

### 2.1 Componentes (5 elementos)

| Componente | Descripción | Ejemplo |
|------------|-------------|---------|
| **Actor** | Quién actúa | `:Ukumaris_Paucartambo_2025` |
| **Rol** | Posición social/ritual | `:IntermediarioRitual` |
| **Evento** | Qué hace | `:SubidaColquePunku_2025` |
| **Propósito** | Por qué lo hace | `:AgradecimientoNacimientoAgua` |
| **Beneficiario** | Para quién | `:ComunidadesValles` |

---

## 3. NUEVAS CLASES

### 3.1 Clase base: Propósito

```turtle
:Proposito rdf:type owl:Class ;
    rdfs:comment "Motivación documentada etnográficamente que explica por qué se realiza una acción ritual. Debe tener fuente verificable."@es ;
    rdfs:label "Propósito"@es .
```

**CRÍTICO:** Cada instancia de `:Proposito` debe tener:
- Descripción clara (rdfs:comment)
- Fuente etnográfica (`:documentadoEn`)
- Al menos un evento asociado (vía `:tienePropósito`)

### 3.2 Subclases de Propósito

```turtle
# Propósitos Rituales
:PropositoRitual rdf:type owl:Class ;
    rdfs:subClassOf :Proposito ;
    rdfs:comment "Motivaciones vinculadas al mundo espiritual: reciprocidad con apus, tradición ceremonial, comunicación con deidades."@es ;
    rdfs:label "Propósito Ritual"@es .

# Propósitos Sociales
:PropositoSocial rdf:type owl:Class ;
    rdfs:subClassOf :Proposito ;
    rdfs:comment "Motivaciones que fortalecen identidad colectiva, estatus, cohesión grupal, obligaciones comunitarias."@es ;
    rdfs:label "Propósito Social"@es .

# Propósitos Personales
:PropositoPersonal rdf:type owl:Class ;
    rdfs:subClassOf :Proposito ;
    rdfs:comment "Motivaciones individuales: mandas, salud familiar, prueba de capacidad, devoción personal."@es ;
    rdfs:label "Propósito Personal"@es .

# Propósitos Prácticos
:PropositoPractico rdf:type owl:Class ;
    rdfs:subClassOf :Proposito ;
    rdfs:comment "Motivaciones con fines materiales o utilitarios que coexisten con lo ritual: recogida de agua, medicina tradicional."@es ;
    rdfs:label "Propósito Práctico"@es .
```

**NOTA:** Un propósito puede ser múltiple:
```turtle
:RecogidaHieloAgua rdf:type :PropositoRitual, :PropositoPractico .
```

### 3.3 Clase Rol (ya existe, expandir)

Agregar instancias especializadas:

```turtle
:IntermediarioRitual rdf:type :Rol ;
    rdfs:comment "Mediador entre mundo humano y espiritual. Ukukus son el caso paradigmático."@es ;
    rdfs:label "Intermediario Ritual"@es .

:OrganizadorPrioste rdf:type :Rol ;
    rdfs:comment "Autoridad encargada de organización material/ceremonial. Sistema de cargos."@es ;
    rdfs:label "Organizador / Prioste"@es .

:PeregrinoDevoto rdf:type :Rol ;
    rdfs:comment "Participante por fe personal o manda, sin rol ceremonial especializado."@es ;
    rdfs:label "Peregrino Devoto"@es .

:DanzanteCeremonial rdf:type :Rol ;
    rdfs:comment "Ejecuta danzas como performance ritual colectiva."@es ;
    rdfs:label "Danzante Ceremonial"@es .

:PortadorImagen rdf:type :Rol ;
    rdfs:comment "Responsable de portar imágenes sagradas en procesiones."@es ;
    rdfs:label "Portador de Imagen"@es .
```

---

## 4. NUEVAS PROPIEDADES

### 4.1 Propiedades principales

```turtle
# Vincula evento con su(s) motivación(es)
:tienePropósito rdf:type owl:ObjectProperty ;
    rdfs:domain :EventoRitual ;
    rdfs:range :Proposito ;
    rdfs:comment "Relaciona evento con motivación documentada. Un evento puede tener múltiples propósitos simultáneos."@es ;
    rdfs:label "tiene propósito"@es .

# Propiedad inversa (navegación bidireccional)
:esPropositoDe rdf:type owl:ObjectProperty ;
    owl:inverseOf :tienePropósito ;
    rdfs:domain :Proposito ;
    rdfs:range :EventoRitual ;
    rdfs:label "es propósito de"@es .

# Identifica beneficiario del propósito
:tieneBeneficiario rdf:type owl:ObjectProperty ;
    rdfs:domain :Proposito ;
    rdfs:range [ owl:unionOf (:Nacion :Colectivo :Lugar :Participante) ] ;
    rdfs:comment "Indica quién se beneficia: comunidades, lugares sagrados, individuos."@es ;
    rdfs:label "tiene beneficiario"@es .

# Fuente etnográfica del propósito
:documentadoEn rdf:type owl:ObjectProperty ;
    rdfs:domain :Proposito ;
    rdfs:range :FuenteEtnografica ;
    rdfs:comment "Vincula propósito con entrevista, observación o fuente bibliográfica que lo documenta."@es ;
    rdfs:label "documentado en"@es .
```

**IMPORTANTE:** Usar `:desempeniaRol` (ya existe) en lugar de crear nueva propiedad.

### 4.2 Propiedades de datatype

```turtle
:intensidadPropósito rdf:type owl:DatatypeProperty ;
    rdfs:domain :Proposito ;
    rdfs:range xsd:string ;
    rdfs:comment "Clasificador: 'primario', 'secundario', 'emergente'. Indica importancia relativa."@es ;
    rdfs:label "intensidad del propósito"@es .
```

---

## 5. EJEMPLOS DE INSTANCIAS

### 5.1 Propósito con múltiples beneficiarios

```turtle
:AgradecimientoNacimientoAgua rdf:type :PropositoRitual ;
    rdfs:label "Agradecimiento por el nacimiento del agua"@es ;
    rdfs:comment "Ukukus suben al glaciar para agradecer al Apu Ausangate por el agua de deshielo que alimenta valles y comunidades."@es ;
    :tieneBeneficiario :ComunidadesValles ;
    :tieneBeneficiario :Ausangate ;  # El apu también recibe reciprocidad
    :documentadoEn :Entrevista_Ukuku_2025_001 ;
    :intensidadPropósito "primario" .
```

### 5.2 Propósito múltiple (ritual + social)

```turtle
:DemostracionResistencia rdf:type :PropositoSocial, :PropositoPersonal ;
    rdfs:label "Demostración de resistencia y valentía"@es ;
    rdfs:comment "Para jóvenes ukukus, completar subida al glaciar demuestra fortaleza física/espiritual, ganando prestigio comunitario."@es ;
    :tieneBeneficiario :Ukumaris_Paucartambo_2025 ;  # Beneficio propio
    :documentadoEn :Observacion_Campo_2025_06_15 ;
    :intensidadPropósito "secundario" .
```

### 5.3 Evento con múltiples propósitos

```turtle
:SubidaColquePunku_2025 
    :tienePropósito :AgradecimientoNacimientoAgua ;
    :tienePropósito :RenovacionAlianzaConApu ;
    :tienePropósito :ComunicacionEspiritual ;
    :tienePropósito :DemostracionResistencia ;
    :realizadoPor :Ukumaris_Paucartambo_2025 .
```

### 5.4 Participante con roles

```turtle
:Ukumaris_Paucartambo_2025 
    :desempeniaRol :IntermediarioRitual ;  # Rol principal
    :desempeniaRol :DanzanteCeremonial ;   # Rol secundario
    :perteneceA :NacionPaucartambo ;
    :participaEn :SubidaColquePunku_2025 .
```

---

## 6. PROPÓSITOS DOCUMENTADOS (10 instancias iniciales)

### 6.1 Rituales

```turtle
:RenovacionAlianzaConApu rdf:type :PropositoRitual ;
    rdfs:label "Renovación de alianza con el Apu"@es ;
    rdfs:comment "Peregrinación renueva pacto de reciprocidad (ayni) con Ausangate, asegurando protección y fertilidad."@es ;
    :tieneBeneficiario :NacionPaucartambo .

:ComunicacionEspiritual rdf:type :PropositoRitual ;
    rdfs:label "Comunicación con mundo espiritual"@es ;
    rdfs:comment "Ascenso permite a ukukus recibir mensajes/orientación de deidades para la comunidad."@es ;
    :tieneBeneficiario :ComunidadesValles .
```

### 6.2 Sociales

```turtle
:FortalecimientoIdentidad rdf:type :PropositoSocial ;
    rdfs:label "Fortalecimiento de identidad colectiva"@es ;
    rdfs:comment "Participación colectiva refuerza identidad de nación y vínculo con territorio sagrado."@es ;
    :tieneBeneficiario :NacionPaucartambo .

:CumplimientoCargo rdf:type :PropositoSocial ;
    rdfs:label "Cumplimiento de cargo comunal"@es ;
    rdfs:comment "Para priostes, organizar festividad es parte del sistema de cargos que otorga prestigio."@es ;
    :intensidadPropósito "primario" .
```

### 6.3 Personales

```turtle
:CumplimientoDeManda rdf:type :PropositoPersonal ;
    rdfs:label "Cumplimiento de manda"@es ;
    rdfs:comment "Cumplir promesa hecha al Señor de Qoyllur Rit'i en agradecimiento por favor recibido (salud, trabajo)."@es .

:PeticionSaludFertilidad rdf:type :PropositoPersonal, :PropositoRitual ;
    rdfs:label "Petición de salud y fertilidad"@es ;
    rdfs:comment "Pedir al Apu por salud de familiares, fertilidad de campos y ganado."@es .
```

### 6.4 Prácticos

```turtle
:RecogidaHieloAgua rdf:type :PropositoRitual, :PropositoPractico ;
    rdfs:label "Recogida ritual de hielo/agua"@es ;
    rdfs:comment "Tradicionalmente, ukukus recogían hielo del glaciar con propiedades rituales y medicinales. Hoy persiste el simbolismo."@es ;
    :documentadoEn :Sallnow1987 .  # Fuente bibliográfica
```

---

## 7. CONSULTAS SPARQL HABILITADAS

### 7.1 Propósitos de un evento

```sparql
SELECT ?propósito ?tipo ?descripcion
WHERE {
    :SubidaColquePunku_2025 :tienePropósito ?propósito .
    ?propósito rdf:type ?tipo .
    ?propósito rdfs:comment ?descripcion .
    FILTER(?tipo != owl:NamedIndividual)
}
```

### 7.2 Beneficiarios de propósitos rituales

```sparql
SELECT ?propósito ?beneficiario
WHERE {
    ?propósito rdf:type :PropositoRitual .
    ?propósito :tieneBeneficiario ?beneficiario .
    ?beneficiario rdfs:label ?nombre .
}
```

### 7.3 Roles desempeñados en eventos con propósito social

```sparql
SELECT DISTINCT ?participante ?rol ?evento
WHERE {
    ?participante :desempeniaRol ?rol .
    ?participante :participaEn ?evento .
    ?evento :tienePropósito ?propósito .
    ?propósito rdf:type :PropositoSocial .
}
```

### 7.4 Fuentes etnográficas de propósitos

```sparql
SELECT ?propósito ?fuente
WHERE {
    ?propósito :documentadoEn ?fuente .
    ?fuente rdfs:label ?nombreFuente .
}
```

---

## 8. METODOLOGÍA DE IMPLEMENTACIÓN

### 8.1 Fase 1: Definiciones (1 semana)

1. Agregar 4 clases de propósito al TTL
2. Agregar 5 roles especializados
3. Definir 4 propiedades nuevas
4. Validar sintaxis

### 8.2 Fase 2: Instancias iniciales (2 semanas)

1. Documentar 10 propósitos (2 por cada tipo)
2. Vincular 5 eventos principales con propósitos
3. Asignar roles a 3 grupos de participantes
4. Crear 5 entidades de beneficiarios

### 8.3 Fase 3: Validación (1 semana)

1. Ejecutar queries SPARQL de prueba
2. Verificar que GraphRAG recupera propósitos
3. Evaluar respuestas a preguntas sobre motivaciones
4. Ajustar según resultados

---

## 9. INTEGRACIÓN CON GRAPHRAG

### 9.1 Actualizar config_graphrag.py

Agregar mapeos:

```python
MAPEOS_RELACIONES = {
    # ... existentes ...
    
    # Agencia
    'tienePropósito': 'Propósito',
    'tieneBeneficiario': 'Beneficia a',
    'desempeniaRol': 'Rol',
    'documentadoEn': 'Documentado en',
}
```

### 9.2 Queries de ejemplo

**Input:** "¿Por qué los ukukus suben al glaciar?"

**Contexto esperado:**
```
• Subida al Colque Punku
  Ascenso nocturno al glaciar...
  Propósito: Agradecimiento por el nacimiento del agua
  Propósito: Renovación de alianza con el Apu
  Propósito: Comunicación con mundo espiritual
```

**Respuesta esperada:**
```
Los ukukus suben al glaciar para agradecer al Apu Ausangate 
por el agua de deshielo, renovar la alianza con el apu, y 
comunicarse con el mundo espiritual.
```

---

## 10. GLOSARIO

| Término | Definición |
|---------|------------|
| **Agencia** | Capacidad de actuar movido por motivaciones y roles específicos |
| **Propósito** | Motivación documentada que explica una acción |
| **Rol** | Función o posición social/ritual desde la que se actúa |
| **Beneficiario** | Quien recibe el beneficio de una acción motivada |
| **Manda** | Promesa hecha a deidad a cambio de favor |
| **Ayni** | Reciprocidad andina, intercambio equilibrado |
| **Intermediario** | Mediador entre humanos y deidades |

---

## 11. DIFERENCIAS CON VERSIÓN 1.0

| Aspecto | V1.0 | V2.0 (Mejorada) |
|---------|------|-----------------|
| Nombre propiedad | `:tieneMotivo` | `:tienePropósito` (más claro) |
| Propiedad rol | `:actuaDesdeRol` | `:desempeniaRol` (reusar existente) |
| Subclases | Solo 3 tipos | 4 tipos (+ PropositoPractico) |
| Inversas | No | Sí (`:esPropositoDe`) |
| Fuentes | No | Sí (`:documentadoEn`) |
| Intensidad | No | Sí (primario/secundario) |
| Ejemplos | 8 | 10 (más variedad) |
| Queries | 3 | 4 (+ fuentes) |
| Integración GraphRAG | No | Sí (mapeos específicos) |

---

**Versión:** 2.0  
**Fecha:** Febrero 2025  
**Próximo paso:** Implementar Fase 1 en qoyllurity.ttl
