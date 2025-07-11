

# Install Node.js and rtlcss
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt-get install -y nodejs
npm install -g rtlcss
# Step 1: Create directory for wkhtmltopdf
mkdir -p /tmp/local/bin

# Step 2: Download patched wkhtmltopdf compatible with Odoo
curl -L -o /tmp/wkhtmltox.tar.xz https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.focal-amd64.tar.xz

# Step 3: Extract binary
tar -xJf /tmp/wkhtmltox.tar.xz -C /tmp
cp /tmp/wkhtmltox/bin/wkhtmltopdf /tmp/local/bin/
chmod +x /tmp/local/bin/wkhtmltopdf

# Optional: verify version
/tmp/local/bin/wkhtmltopdf --version

apt-get update && apt-get install -y libpango1.0-0 libpangocairo-1.0-0 libcairo2 libjpeg-dev libfreetype6-dev
