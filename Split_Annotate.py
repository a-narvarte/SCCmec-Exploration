from Bio import SeqIO
import os
import subprocess

#Create new folder, break up fasta file and save new fastas to folder
directory = "SCCmec_fasta_files"
os.makedirs(directory, exist_ok=True)
for seq in SeqIO.parse("SCCmec_database.fasta.txt", "fasta"):
    filename = f"SCCmec_{seq.id}.fasta"
    path = os.path.join(directory, filename)
    with open(path, "w") as filename:
        SeqIO.write(seq, filename, "fasta")

#Bakta script for annotating
script = ["bakta", "--db", ""]
for item in os.listdir(directory):
    print(f"{item}")