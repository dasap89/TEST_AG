#!/usr/bin/python
import os


ed = raw_input("Please, enter education to find people with it: ")
call_command = "python manage.py peoples_education " + ed
os.system(call_command)
