#!/bin/bash

# activate virtual environment
source "C:\Users\Kunmi\OneDrive\Desktop\quantium-starter-repo\venv\Scripts\activate"

# Run test_data.py,
# if all tests passed return exit code 0,
# if tests failed return exit code 1,

if pytest test_data.py -q; then
	echo "All test passed"
	exit_code=0
else
	echo "Tests failed"
	exit_code=1
fi

echo "Exit code: $exit_code"
exit $exit_code
