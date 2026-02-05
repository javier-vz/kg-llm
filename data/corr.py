# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 12:03:10 2026

@author: jvera
"""

# Limpieza total de inicio y caracteres ilegales en TTL
import re

infile = "grafo.ttl"
outfile = "grafo_clean.ttl"

with open(infile, "rb") as f:
    raw = f.read()

# Elimina BOM si existe
raw = raw.lstrip(b'\xef\xbb\xbf')

text = raw.decode("utf-8", errors="replace")

# Quita caracteres de control (excepto \n y \t)
text = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", text)

# Elimina líneas vacías iniciales
text = text.lstrip()

with open(outfile, "w", encoding="utf-8", newline="\n") as f:
    f.write(text)

print("Archivo limpio:", outfile)
