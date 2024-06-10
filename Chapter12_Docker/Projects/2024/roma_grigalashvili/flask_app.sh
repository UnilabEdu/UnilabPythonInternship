#!/bin/bash
echo "Create Database"
flask init_db
echo "==================================="

echo "Create Test Tavles"
flask populate_db
echo "==================================="