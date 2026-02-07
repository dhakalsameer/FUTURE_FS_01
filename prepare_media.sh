#!/bin/bash

# Script to prepare media files for deployment
echo "Preparing media files for deployment..."

# Create media directory if it doesn't exist
mkdir -p media

# Copy all media files
if [ -d "media" ]; then
    echo "Media files already exist in media/ directory"
else
    echo "Warning: No media directory found"
fi

# List what will be deployed
echo "Files to be deployed:"
find media -type f 2>/dev/null | head -10

echo "Media preparation complete!"