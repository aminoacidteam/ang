def translate():#각 코돈에 대응하는 아미노산의 종류를 지정한다.
    table = { 
        'ATA':'ILEU-', 'ATC':'ILEU-', 'ATT':'ILEU-', 'ATG':'MET-', 
        'ACA':'THR-', 'ACC':'THR-', 'ACG':'THR-', 'ACT':'THR-', 
        'AAC':'ASN-', 'AAT':'ASN-', 'AAA':'LYS-', 'AAG':'LYS-', 
        'AGC':'SER-', 'AGT':'SER-', 'AGA':'ARG-', 'AGG':'ARG-',                  
        'CTA':'LEU-', 'CTC':'LEU-', 'CTG':'LEU-', 'CTT':'LEU-', 
        'CCA':'PRO-', 'CCC':'PRO-', 'CCG':'PRO-', 'CCT':'PRO-', 
        'CAC':'HIS-', 'CAT':'HIS-', 'CAA':'GLN-', 'CAG':'GLN-', 
        'CGA':'ARG-', 'CGC':'ARG-', 'CGG':'ARG-', 'CGT':'ARG-', 
        'GTA':'VAL-', 'GTC':'VAL-', 'GTG':'VAL-', 'GTT':'VAL-', 
        'GCA':'ALA-', 'GCC':'ALA-', 'GCG':'ALA-', 'GCT':'ALA-', 
        'GAC':'ASP-', 'GAT':'ASP-', 'GAA':'GLU-', 'GAG':'GLU-', 
        'GGA':'GLY-', 'GGC':'GLY-', 'GGG':'GLY-', 'GGT':'GLY-', 
        'TCA':'SER-', 'TCC':'SER-', 'TCG':'SER-', 'TCT':'SER-', 
        'TTC':'PHE-', 'TTT':'PHE-', 'TTA':'LEU-', 'TTG':'LEU-', 
        'TAC':'TYR-', 'TAT':'TYR-', 'TAA':'_', 'TAG':'_', 
        'TGC':'CYS-', 'TGT':'CYS-', 'TGA':'_', 'TGG':'TRY-', 

    } 
    protein ="" 
    sm = False
    if len(rslt)%3 == 0: 
        for i in range(0, len(rslt), 3):#염기서열을 3개씩 쪼개어 지정한다.

            codon = rslt[i:i + 3]#코돈을 지정한다.

            if codon == 'ATG':
                sm = True#개시코돈을 읽으면 번역을 시작한다.

            if sm == True:
                if codon == ('TAA' or 'TAG' or 'TGA'):
                    return protein#종결코돈을 읽으면 번역을 중단하고 단백질을 리턴한다.
                else: 
                    protein+= table[codon]#신장을 계속한다. 
                 
    return False
             

print(translate())
