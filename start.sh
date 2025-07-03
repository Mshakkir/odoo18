
echo "Starting Odoo on Render using PORT=$PORT"

# Replace http_port with Render's dynamic port
sed -i "s/^http_port *= *.*/http_port = ${PORT}/" odoo.conf

# Only initialize if database is not set up yet
python3 odoo-bin -c odoo.conf -i base --without-demo=all --stop-after-init

# Now start Odoo normally
python3 odoo-bin -c odoo.conf
