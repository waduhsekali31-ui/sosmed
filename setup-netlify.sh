#!/bin/bash

# Script untuk setup dan deploy aplikasi ke Netlify

echo "=========================================="
echo "Netlify Deployment Setup Script"
echo "=========================================="
echo ""

# Check if netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo "📦 Installing Netlify CLI..."
    npm install -g netlify-cli
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install Netlify CLI"
        exit 1
    fi
    echo "✅ Netlify CLI installed"
else
    echo "✅ Netlify CLI already installed"
fi
echo ""

# Check if user is logged in
echo "Checking Netlify login status..."
netlify status > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "👤 Not logged in to Netlify. Starting login..."
    netlify login
    if [ $? -ne 0 ]; then
        echo "❌ Login failed"
        exit 1
    fi
fi
echo "✅ Logged in to Netlify"
echo ""

# Link site
echo "Linking site to Netlify..."
netlify link
if [ $? -ne 0 ]; then
    echo "❌ Failed to link site"
    exit 1
fi
echo "✅ Site linked"
echo ""

# Set environment variables
echo "Setting environment variables..."
echo ""

read -p "Enter DATABASE_URL: " DATABASE_URL
if [ ! -z "$DATABASE_URL" ]; then
    netlify env:set DATABASE_URL "$DATABASE_URL"
    echo "✅ DATABASE_URL set"
fi

read -p "Enter SECRET_KEY (press Enter to generate): " SECRET_KEY
if [ -z "$SECRET_KEY" ]; then
    SECRET_KEY=$(openssl rand -hex 32)
    echo "Generated SECRET_KEY: $SECRET_KEY"
fi
netlify env:set SECRET_KEY "$SECRET_KEY"
echo "✅ SECRET_KEY set"

netlify env:set FLASK_ENV "production"
echo "✅ FLASK_ENV set to production"

echo ""
echo "Current environment variables:"
netlify env:list

echo ""
echo "=========================================="
echo "Setup Complete! Next steps:"
echo "=========================================="
echo ""
echo "1. Push to GitHub (if not already):"
echo "   git push origin main"
echo ""
echo "2. Deploy to Netlify:"
echo "   netlify deploy --prod"
echo ""
echo "3. View logs:"
echo "   netlify logs:tail"
echo ""
echo "4. Or use Netlify UI:"
echo "   https://app.netlify.com"
echo ""
echo "Useful commands:"
echo "  - netlify deploy          # Deploy preview"
echo "  - netlify deploy --prod   # Deploy production"
echo "  - netlify env:list        # View environment variables"
echo "  - netlify status          # View site status"
echo "  - netlify logs:tail       # View live logs"
echo ""
