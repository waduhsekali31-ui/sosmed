#!/bin/bash

echo "Setting Netlify environment variables..."
echo ""

# Generate SECRET_KEY
SECRET_KEY=$(openssl rand -hex 32)
echo "Generated SECRET_KEY: $SECRET_KEY"
netlify env:set SECRET_KEY "$SECRET_KEY"
echo "✅ SECRET_KEY set"
echo ""

# Set FLASK_ENV
netlify env:set FLASK_ENV "production"
echo "✅ FLASK_ENV set to production"
echo ""

# Optional: DATABASE_URL
read -p "Enter DATABASE_URL (or press Enter to skip): " DATABASE_URL
if [ ! -z "$DATABASE_URL" ]; then
    netlify env:set DATABASE_URL "$DATABASE_URL"
    echo "✅ DATABASE_URL set"
else
    echo "⚠️  DATABASE_URL not set. You can set it later."
fi
echo ""

echo "Current environment variables:"
netlify env:list
