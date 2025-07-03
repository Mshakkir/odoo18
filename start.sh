echo "Starting Odoo on Render using PORT=${PORT}"

# Replace hardcoded port in odoo.conf with actual Render port
sed -i "s/^http_port *= *.*/http_port = ${PORT}/" odoo.conf

# Start Odoo
python3 odoo-bin -d database18 -i base --without-demo=True