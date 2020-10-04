#!/usr/bin/env python3

import glob, sys, os, shutil
import fitz

documents = [doc for doc in glob.glob('*.pdf')]

documents_wpw = []

if len(sys.argv) != 2:
    sys.exit("Usage: ./pdfdecrypt.py 'password'")
    
for doc in documents:
    if fitz.Document(doc).needsPass:
        documents_wpw.append(doc)

if len(documents_wpw) + len(documents) == 0:
    sys.exit("Can't find any encrypted pdf")

if not os.path.exists('backup'):
    os.makedirs('backup')

for name in documents_wpw: 
    doc = fitz.Document(name)   
    if doc.authenticate(sys.argv[1]):
        doc.save(name+"temp")
        shutil.move(name, 'backup')
        os.rename(name+"temp",name)
    else:
        print(f'Wrong pw for {name}')
