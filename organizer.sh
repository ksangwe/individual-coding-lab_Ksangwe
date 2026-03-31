#!/bin/bash

# Create archive folder if it doesn't exist
mkdir -p archive

# Timestamp for unique file naming
timestamp=$(date +"%Y%m%d-%H%M%S")

# Move and rename grades.csv into archive
mv grades.csv "archive/grades_$timestamp.csv"

# Create a fresh empty grades.csv file
touch grades.csv

# Log the action
echo "$timestamp - grades.csv archived as grades_$timestamp.csv" >> organizer.log

echo "Archive completed successfully."
