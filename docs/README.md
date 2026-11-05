# Atlas Qoyllur Rit’i 2.0 — vista global (ES/EN/PT)

Esta revisión **restaura la vista completa del grafo** como pantalla inicial, usando una estética oscura de alto contraste inspirada en el visor original. Conserva la interfaz multilingüe, las fichas de entidades, la secuencia de 2025 y el pequeño archivo aéreo separado de 2026.

## Abrir en GitHub Pages

Copiar el contenido de `docs/` a la carpeta `docs/` de `javier-vz/kg-llm`. Se mantiene la ruta `grafo_interactivo.html`. No sustituir ni modificar los datos de campo originales sin auditoría.

## Cambios importantes

- La página abre con **todos los individuos y todas las relaciones individuales** del archivo de 2025. Incluye los nodos aislados.
- Un clic destaca relaciones inmediatas sin abandonar la vista global. Los botones 1 y 2 aíslan entornos; **Vista global** los restaura.
- Colores oscuros y contrastes altos recuperan la estética general del HTML original. Colores por grupo de entidades, no por valoración cultural.
- Posiciones calculadas de manera reproducible desde las relaciones del grafo (semilla fija), sin modificar el TTL. La distancia entre nodos en pantalla no expresa distancia geográfica.
- Las relaciones son dirigidas: 161 aserciones del archivo del proyecto. Las etiquetas RDF originales se conservan en los datos y se traducen solo en la vista.
- Las fichas traducidas son resúmenes editoriales, no nuevas fuentes.
- Cuatro fotografías de dron 2026 permanecen como archivo separado; su ubicación y fecha exacta no han sido verificadas.

## Estructura

- `grafo_interactivo.html`: interfaz
- `data/grafo_2025.js`: proyección para el visor, derivada del TTL de 2025
- `data/i18n_entities.js`: traducciones de presentación
- `data/global_layout.js`: coordenadas de la distribución *visual* precalculada
- `qoyllurity.ttl`: archivo fuente RDF original, no editado
- `assets/`: cuatro miniaturas del archivo aéreo de 2026

No se ha hecho ningún cambio automático en GitHub.
