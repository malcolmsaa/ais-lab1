#!/bin/bash

echo "Simulerar brute force attack..."

for i in {1..10}
do
    ssh invaliduser@localhost
done

echo "Attack simulering klar"
