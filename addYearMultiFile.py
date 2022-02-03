#!/usr/bin/python3
import datetime, os, re

yearNow = datetime.date.today().year
yearPrev = yearNow - 1

lista = os.listdir()

for file in lista:
    if file.startswith("auth"):
        if str(yearPrev) in file:
            outfile = file + ".mod"
            with open(file,'r') as f:
                file = f.readlines()
                with open(outfile,'w') as o:
                    for line in file:
                        reg = re.findall("^[A-Z][a-z]{2}.*",line)
                        if reg:
                            o.write(f"{yearPrev} {reg[0]}\n")
        elif f"{yearNow}-01-" in file:
            outfile = file + ".mod"
            with open(file,'r') as f:
                file = f.readlines()
                with open(outfile,'w') as o:
                    for line in file:
                        regDec = re.findall("^Dec.*",line)
                        regJan = re.findall("^Jan.*",line)
                        if regDec:
                            o.write(f"{yearPrev} {regDec[0]}\n")
                        if regJan:
                            o.write(f"{yearNow} {regJan[0]}\n")
        else:
            outfile = file + ".mod"
            with open(file,'r') as f:
                file = f.readlines()
                with open(outfile,'w') as o:
                    for line in file:
                        reg = re.findall("^[A-Z][a-z]{2}.*",line)
                        if reg:
                            o.write(f"{yearNow} {reg[0]}\n")