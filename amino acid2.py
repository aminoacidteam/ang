
def translate(rslt): 
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

    for i in range(0, len(rslt)):

        codon = rslt[i:i + 3]


            if sm == True:
                if codon == ('TAA' or 'TAG' or 'TGA'):
                    return protein
                else: 
                    protein+= table[codon] 
            if codon ==('TTT' or 'TTC'):
                print('if you have 페닐케톤뇨증, 삼가 고인의 명복을 빔.')
    return False
             


print(translate())

            if protain"" in ('GLY', 'ALA', 'VAL', 'LEU', 'ILE', 'MET', 'PHE', 'TRP', 'PRO'):
                 print('해당 폴리펩타이드가 아미노산 분자 내로 숨겨지는 구조입니다.')
            if protain"" in ('SER', 'THR', 'CYS', 'TYR', 'ASN', 'GLN', 'ASP', 'GLU', 'LYS','ARG','HIS'):
                 print('해당 폴리펩타이드가 아미노산 분자 표면으로 배치됩니다.)
   # 사슬모양, 고리형, 방향족 등의 특성도 넣기#         

