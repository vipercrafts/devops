#!/bin/bash

output=$(./helloworld.sh)
# echo "$output"
if [ "$output" = "Hello, World!" ]; then
  echo "Test Passed ✅"
else
  echo "Test Failed ❌"
  echo "Expected: Hello, World!"
  echo "Got: $output"
fi
