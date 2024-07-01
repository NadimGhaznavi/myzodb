#!/bin/bash

# A script to generate HTML documentation from Python code using the Python pdoc module.

cd /opt/prod/db4e
pdoc src/* -o docs
