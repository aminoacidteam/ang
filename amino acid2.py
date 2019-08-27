def translate(): 
    table = { 
        'AUA':'ILEU-', 'AUC':'ILEU-', 'AUU':'ILEU-', 'AUG':'MET-', 
        'ACA':'THR-', 'ACC':'THR-', 'ACG':'THR-', 'ACU':'THR-', 
        'AAC':'ASN-', 'AAU':'ASN-', 'AAA':'LYS-', 'AAG':'LYS-', 
        'AGC':'SER-', 'AGU':'SER-', 'AGA':'ARG-', 'AGG':'ARG-',                  
        'CUA':'LEU-', 'CTC':'LEU-', 'CUG':'LEU-', 'CUU':'LEU-', 
        'CCA':'PRO-', 'CCC':'PRO-', 'CCG':'PRO-', 'CCU':'PRO-', 
        'CAC':'HIS-', 'CAU':'HIS-', 'CAA':'GLN-', 'CAG':'GLN-', 
        'CGA':'ARG-', 'CGC':'ARG-', 'CGG':'ARG-', 'CGU':'ARG-', 
        'GUA':'VAL-', 'GUC':'VAL-', 'GUG':'VAL-', 'GUU':'VAL-', 
        'GCA':'ALA-', 'GCC':'ALA-', 'GCG':'ALA-', 'GCU':'ALA-', 
        'GAC':'ASP-', 'GAU':'ASP-', 'GAA':'GLU-', 'GAG':'GLU-', 
        'GGA':'GLY-', 'GGC':'GLY-', 'GGG':'GLY-', 'GGU':'GLY-', 
        'UCA':'SER-', 'UCC':'SER-', 'UCG':'SER-', 'UCU':'SER-', 
        'UUC':'PHE-', 'UUU':'PHE-', 'UUA':'LEU-', 'UUG':'LEU-', 
        'UAC':'TYR-', 'UAU':'TYR-', 'UAA':'_', 'UAG':'_', 
        'UGC':'CYS-', 'UGU':'CYS-', 'UGA':'_', 'UGG':'TRY-', 

    } 
    protein ="" 
    sm = False
    if len(rslt)%3 == 0: 
        for i in range(0, len(rslt), 3):

            codon = rslt[i:i + 3]

            if codon == 'ATG':
                sm = True

            if sm == True:
                if codon == ('TAA' or 'TAG' or 'TGA'):
                    return protein
                else: 
                    protein+= table[codon] 
                 
    return False
             

print(translate())
