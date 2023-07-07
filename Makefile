ifeq ($(OS),Windows_NT)
	RM := del /Q /F 2>nul
	RD := rmdir /Q /S
	MKDIR := mkdir
	PY := python
	SEP = \\
else
	RM := rm -rf
	RD := rmdir --ignore-fail-on-non-empty
	MKDIR := mkdir -p
	PY := python3
	SEP = /
endif

PACKAGE_NAME := qvsed
DIST_DIR := dist
BUILD_DIR := build

target:
	@$(PY) setup.py sdist

wheel:
	@$(PY) setup.py bdist_wheel

clean:
	@if exist $(PACKAGE_NAME).egg-info $(RD) $(PACKAGE_NAME).egg-info
	@if exist $(DIST_DIR) $(RD) $(DIST_DIR)
	@if exist $(BUILD_DIR) $(RD) $(BUILD_DIR)	
	@if exist $(PACKAGE_NAME).spec $(RM) $(PACKAGE_NAME).spec
	@if exist $(PACKAGE_NAME)$(SEP)__pycache__ $(RD) $(PACKAGE_NAME)$(SEP)__pycache__