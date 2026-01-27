#!/bin/bash

# Read each line from values.txt
while IFS='=' read -r key value; do
    # Skip empty lines
    if [ -n "$key" ]; then
        # Use @ as delimiter instead of / to avoid issues with URLs
        sed -i "s@$key@$value@g" demo.yaml
        echo "Replaced: $key -> $value"
    fi
done < values.txt

echo ""
echo "Configuration updated successfully!"