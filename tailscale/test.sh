#!/bin/bash

output=$(./helloworld.sh apple)
# echo "$output"
if [ "$output" = "Hello, World! apple" ]; then
  echo "Test Passed ✅"
else
  echo "Test Failed ❌"
  echo "Expected: Hello, World! apple"
  echo "Got: $output"
fi
