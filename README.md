# Python3-Interpreter-Research
Security research/proof of concept code for analysis of the Python3 interpreter. Prepared for the Layer 1 Security Conference in Los Angeles, California 2023.

The official slides are available [here](https://docs.google.com/presentation/d/1DFa_x44KiYaZ-tXx48TKyKrkOYL3O0W1L2LlDeC0q0E/edit?usp=sharing).<br>

## (CVSS_8.4) PyCache Poisoning
Bad bytecode validation leading to injecting the cache for code exec.

## (CVSS_4.2) Stable ABI Overflows
Stack and Heap abuse in the ABI for wrapping C code (Numpy, etc)

## (CVSS_6.5) Pip3 Typosquatting
Tests performed on Pip3 packages and the issue with limited verification.
