#!/bin/bash
# Test your code before pushing it into the repository by launching this script!
clear

# Exit immediately if a command exits with a non-zero status.
set -e

# Set the color variable.
green="\033[0;32m"

# Clear the color after that.
clear="\033[0m"

# pylint sintax check.
pylint src

# pytest unit tests check.
pytest --cov src tests/ --cov-report=html --cov-fail-under=75

# Success message.
printf "${green}\nSuccess${clear}, you can go ahead and push your code!\n"
