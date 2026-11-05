# Atlas de Qoyllur Rit’i · v2.3 — componente conexa mayor / sobre el proyecto

Esta versión conserva la vista global oscura de la componente conexa mayor y agrega una sección «Acerca de» en español, inglés y portugués.

## Publicación en GitHub Pages

Copiar **el contenido de la carpeta `docs/` del ZIP** a la carpeta `docs/` del repositorio `javier-vz/kg-llm`, conservando nombres y rutas. URL prevista una vez completado el despliegue:

https://javier-vz.github.io/kg-llm/grafo_interactivo.html

## Cambios de esta edición

- El bloque «Alcance de la exploración» (botones 1/2/Todo) se retiró del menú lateral y las fichas de entidad. La red se abre en su conjunto; seleccionar un nodo destaca sus relaciones, con un botón de regreso a la vista global.
- Nueva pestaña **Acerca de / About / Sobre** accesible desde la barra principal y la navegación móvil.
- Presentación de Qoyllur Rit’i y del proyecto de investigación, con una fotografía de contexto de 2026 y nota sobre la ubicación de captura no verificada.
- Enlaces a la ficha de UNESCO, a dos artículos científicos publicados y al repositorio del proyecto.
- Se conservan las leyendas cromáticas, las tres lenguas, las fichas, la línea de tiempo y el archivo fotográfico.

## Datos y cautelas

- TTL original sin modificaciones: 87 individuos, 161 relaciones entre individuos y 1.060 triples RDF.
- Vista principal: 80 entidades, 161 relaciones dirigidas (componente conexa mayor calculada sin la dirección solo para conectividad).
- Siete entidades aisladas no aparecen en la vista principal, pero sí en los datos fuente.
- Las cuatro imágenes de dron de 2026 son material documental independiente y no están enlazadas sin validación al grafo de 2025.
- Las traducciones de presentación son editoriales; no modifican las etiquetas ni descripciones originales del TTL.

## Archivos

- `docs/grafo_interactivo.html`: visor publicado por GitHub Pages.
- `docs/qoyllurity.ttl`: RDF original.
- `docs/data/grafo_2025.js`: 87 entidades y 161 relaciones originales.
- `docs/data/i18n_entities.js`: traducciones del conjunto de entidades.
- `docs/data/global_layout.js`: posiciones de la vista global.
- `docs/assets/`: fotografías optimizadas para web.

Para probar sin publicarlo, abrir el HTML autónomo distribuido junto a este ZIP.
