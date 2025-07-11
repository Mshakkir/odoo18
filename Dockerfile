FROM python:3.10.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git build-essential wget \
    node-less libldap2-dev libsasl2-dev \
    libxml2-dev libxslt1-dev zlib1g-dev \
    libpq-dev libjpeg-dev libjpeg62-turbo-dev liblcms2-dev \
    libblas-dev libatlas-base-dev libssl-dev libffi-dev \
    libfreetype6-dev libharfbuzz-dev libfribidi-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /odoo

# Copy Odoo source code (if you cloned from GitHub)
# COPY odoo/ /odoo/

# Copy custom addons
COPY custom/ /mnt/extra-addons/

# Copy wkhtmltopdf patched
COPY wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf
RUN chmod +x /usr/local/bin/wkhtmltopdf

# Copy configuration
COPY odoo.conf /etc/odoo.conf

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV ODOO_RC /etc/odoo.conf

# Expose port
EXPOSE 8069

# Run Odoo
CMD ["odoo", "-c", "/etc/odoo.conf"]
