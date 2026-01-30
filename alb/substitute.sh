#!/bin/bash



if [ ! -f "input.txt" ]; then
    echo "Error: input.txt file not found!"
    exit 1
fi

# Read each line from input.txt
while IFS='|' read -r yaml_file replacement; do
    # Skip empty lines and comments (lines starting with #)
    if [ -z "$yaml_file" ] || [[ "$yaml_file" =~ ^#.*$ ]]; then
        continue
    fi
    
    # Check if YAML file exists
    if [ ! -f "$yaml_file" ]; then
        echo "Warning: $yaml_file not found, skipping..."
        continue
    fi
    
    # Split the replacement into key and value
    IFS='=' read -r key value <<< "$replacement"
    
    # Skip if key or value is empty
    if [ -z "$key" ] || [ -z "$value" ]; then
        echo "Warning: Invalid format in line, skipping..."
        continue
    fi
    
    # Use @ as delimiter to avoid issues with URLs
    sed -i "s@$key@$value@g" "$yaml_file"
    echo "✓ Updated $yaml_file: $key -> $value"
    
done < input.txt

echo ""
echo "Configuration updated successfully!"