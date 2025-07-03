#!/bin/bash

echo "Starting Odoo on Render using PORT=$PORT"

# Update port
sed -i "s/^http_port *= *.*/http_port = ${PORT}/" odoo.conf

# Check if DB is empty and run base init
echo "Checking database status..."
INIT_DB_FLAG_FILE="/opt/render/project/src/.init_done"

python3 odoo-bin -c odoo.conf -d database18 -u all --stop-after-init

exec python3 odoo-bin -c odoo.conf
