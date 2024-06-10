#!/bin/bash
echo "Create Database"
flask init_db
echo "==================================="

echo "Create Initialization"
flask populate_db
echo "==================================="