#!/bin/bash
set -e

# Clean dir with reports if it's exists
rm -rf reports/allure-results reports/report.html

# Run pytest from root dir, where tests are located
pytest tests/ui "$@"