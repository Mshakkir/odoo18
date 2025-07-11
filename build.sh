

# Install Node.js and rtlcss
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt-get install -y nodejs
npm install -g rtlcss

# Install required dependencies for wkhtmltopdf
apt-get update && apt-get install -y \
  xfonts-75dpi xfonts-base fontconfig libxrender1 libxext6 libjpeg62-turbo wget gnupg

# Download and install Odoo-compatible wkhtmltopdf (patched Qt)
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
dpkg -i wkhtmltox_0.12.6-1.focal_amd64.deb || apt-get install -f -y

# Cleanup
rm wkhtmltox_0.12.6-1.focal_amd64.deb

apt-get update && apt-get install -y libpango1.0-0 libpangocairo-1.0-0 libcairo2 libjpeg-dev libfreetype6-dev
