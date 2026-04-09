#!/bin/sh
set -e

if [ -n "$BASE_PATH" ]; then
    sed -i "s|<base href=\"/\" >|<base href=\"${BASE_PATH}\">|g" /app/dist/index.html
    sed -i "s|BASE_PATH: '[^']*'|BASE_PATH: '${BASE_PATH}'|g" /app/dist/config.js
fi

exec /app/hatchet-staticfileserver -static-asset-dir /app/dist