#!/bin/bash

stdbuf -oL ./manage.py get_all_objects_info > "$(date +'%d%m%Y')".dat
printf "Was created %s\n" "$(date +'%d%m%Y')".dat