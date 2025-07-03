
echo "Starting Odoo on Render using PORT=$PORT"


sed -i "s/^http_port *= *.*/http_port = ${PORT}/" odoo.conf


#python3 odoo-bin -c odoo.conf -i base --without-demo=all --stop-after-init


python3 odoo-bin -c odoo.conf
