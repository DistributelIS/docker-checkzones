#!/usr/bin/env python3

import os
import sys
import subprocess

def check_zones(directory):
    goodzones = 0
    badzones = []

    for entry in os.scandir(directory):
        zonename = None

        if entry.is_dir():
            # Recursively check subdirectories
            good, bad = check_zones(entry.path)
            goodzones += good
            badzones.extend(bad)
        elif entry.is_file():
            if entry.name.endswith('.db'):
                zonename = entry.name.rstrip('.db')
            elif entry.name.endswith('.rev'):
                zonename = entry.name.lstrip('db.')
                zonename = zonename.rstrip('.rev')
                zonename = zonename.split('.')
                zonename.reverse()
                zonename.append('in-addr.arpa')
                zonename = ".".join(zonename)

            if zonename is not None:
                s = subprocess.run(['/usr/sbin/named-checkzone', zonename, entry.path], check=False)
                returncode = s.returncode

                if returncode:
                    badzones.append(zonename)
                else:
                    goodzones += 1

    return goodzones, badzones

if len(sys.argv) < 2:
    print("Usage: {} <directory>".format(sys.argv[0]))
    sys.exit(1)

directory_to_check = sys.argv[1]
goodzones, badzones = check_zones(directory_to_check)

print('\n' + str(goodzones) + ' zone files passed validation')
print('\n' + str(len(badzones)) + ' zone files failed validation')

for z in badzones:
    print('- ' + z)

sys.exit(len(badzones))
