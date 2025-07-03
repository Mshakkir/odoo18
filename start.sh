#!/bin/bash

echo "Starting Odoo on Render using PORT=$PORT"

# Update port
sed -i "s/^http_port *= *.*/http_port = ${PORT}/" odoo.conf

# Check if DB is empty and run base init
echo "Checking database status..."
INIT_DB_FLAG_FILE="/opt/render/project/src/.init_done"

if [ ! -f "$INIT_DB_FLAG_FILE" ]; then
  echo "First-time DB init running - installing base..."
  python3 odoo-bin -c odoo.conf -i base --without-demo=all --stop-after-init
  touch "$INIT_DB_FLAG_FILE"
else
  echo "DB already initialized, skipping -i base"
fi

# Start Odoo
exec python3 odoo-bin -c odoo.conf
