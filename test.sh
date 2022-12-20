#!/bin/bash
# Test your code before pushing it into the repository by launching this script!
clear

# Exit immediately if a command exits with a non-zero status.
set -e

# Set the color variable.
green="\033[0;32m"

# Clear the color after that.
clear="\033[0m"

# pytest unit tests check.
printf "pytest:\n"

# NB: add -s to pytest calls to print the stdout of the called tests.
pytest --cov src tests --cov-report=html --cov-fail-under=75 -s

# pylint sintax check.
printf "\npylint:"
pylint src

# Success message.
printf "${green}Success${clear}, you can go ahead and push your code!\n"
