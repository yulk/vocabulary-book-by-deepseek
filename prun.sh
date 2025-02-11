#!/bin/bash

env $(grep -v '^#' .env | xargs) python3.8 $@
