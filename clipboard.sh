#!/bin/bash

while true; do
  # Obtener el contenido del portapapeles
  clipboard_content=$(xclip -o -selection clipboard)

  # Obtener la primera línea del contenido del portapapeles
  first_line=$(echo "$clipboard_content" | head -n 1)

  # Mostrar solo los primeros 30 caracteres de la primera línea
  trimmed_content=$(echo "$first_line" | cut -c 1-30)

  # Verificar si el contenido del portapapeles está vacío o es una sola línea
  if [ -z "$clipboard_content" ]; then
    trimmed_content="....."
  elif [ $(echo "$clipboard_content" | wc -l) -gt 1 ]; then
    trimmed_content+="..."
  fi

  # Imprimir el contenido ajustado
  echo $trimmed_content >~/.config/qtile/Complementos/clipboard.txt
  # echo "$trimmed_content"
  sleep 5
done
