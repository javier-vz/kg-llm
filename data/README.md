# Flujo completo: Protégé Desktop (PC) → GitHub → Raspberry Pi (kg-llm)

El principio es simple:

- La **Raspberry nunca edita** el grafo, solo recibe cambios.
- El **PC con Protégé Desktop** es tu “editor oficial” de la ontología.

---

## 🔵 1. Instalar y usar Protégé Desktop en tu PC

1. Descarga Protégé Desktop desde:  
   https://protege.stanford.edu/software.php

2. Abre tu ontología en Protégé:

    File → Open  
    Selecciona el archivo: `kg-llm/data/grafo.ttl`

3. Edita lo que necesites:

   - Clases  
   - Propiedades  
   - Individuos  
   - Axiomas y restricciones  
   - Jerarquías

4. Guarda los cambios:

    File → Save

Ese `grafo.ttl` actualizado será el que sincronices con GitHub.

---

## 🟣 2. Subir el TTL editado a GitHub (desde tu PC)

En tu PC donde editaste con Protégé:

    cd kg-llm
    git add data/grafo.ttl
    git commit -m "Ontología actualizada desde Protégé Desktop"
    git push

Con esto, el repositorio remoto ya tiene la nueva versión de la ontología.

---

## 🟢 3. Actualizar la Raspberry Pi (donde vive kg-llm)

La Raspberry **no edita** el grafo, solo baja la última versión.

En la Raspberry Pi:

    cd kg-llm
    git pull

Ahora `data/grafo.ttl` está actualizado también en la Raspberry.

---

## 🟡 4. Regenerar los índices en la Raspberry

Cada vez que cambias la ontología, debes regenerar:

- `data/index_entities.json`
- `index/entity_vectors.npz`

En la Raspberry:

    python scripts/extract_entities.py
    python scripts/build_index.py

Después de esto, puedes hacer consultas con el grafo actualizado, por ejemplo:

    python scripts/answer.py "¿Quiénes son los personajes de Qoyllur Rit'i?"

---

## 🟤 5. (Opcional) Script para automatizar la actualización en Raspberry

Puedes crear un script llamado `update_kg.sh` que haga todo junto.

Contenido sugerido:

    #!/bin/bash
    cd /home/pi/kg-llm
    git pull
    source llm-env/bin/activate
    python scripts/extract_entities.py
    python scripts/build_index.py
    echo "✓ KG actualizado"

Luego le das permisos de ejecución:

    chmod +x update_kg.sh

Y cuando quieras actualizar todo:

    ./update_kg.sh

---

## 🔥 Resumen ultra claro

- **En tu PC con Protégé Desktop:**  
  Editas la ontología → Guardas (`File → Save`) → `git add` → `git commit` → `git push`

- **En la Raspberry Pi:**  
  `git pull` → regeneras índices (`extract_entities.py` y `build_index.py`) → usas `kg-llm` normalmente.
