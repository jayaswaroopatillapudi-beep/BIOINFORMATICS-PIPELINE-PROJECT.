from Bio import SeqIO
record_protein=SeqIO.read("protein.fasta","fasta")
print(record_protein.id)
print(record_protein.description)
print(len(record_protein))
print(record_protein.seq)



from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
data = SeqIO.read("protein.fasta","fasta")
seq=(data.seq)
print(seq)
report=ProteinAnalysis(seq)
print(report)
count=report.count_amino_acids()
print(count)
percent=report.get_amino_acids_percent()
print(percent)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from Bio.Blast import NCBIWWW
from Bio import SeqIO
record= SeqIO.read("protein.fasta","fasta")
result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence= record.seq
)
with open ("blast_resultp.xml","w") as b:
    b.write(result_handle.read())

    
print("code is correct")    


from Bio.Blast import NCBIXML
with open ("blast_resultp.xml") as b:
    blast_report=NCBIXML.read(b)

print(len(blast_report.alignments)) 
frist_alignment= blast_report.alignments[0]
print(frist_alignment.title)
print(frist_alignment.length)
print(len(frist_alignment.hsps))
first_hsp =frist_alignment.hsps[0]
print(first_hsp.score)
print(first_hsp.expect)
print("Query sequence")
print(first_hsp.query)
print("Mached sequence")
print(first_hsp.sbjct)
print("alignmment seq")
print(first_hsp.match)
print("query range:",first_hsp.query_start,"_",first_hsp.query_end)
print("subject range:",first_hsp.query_start,"_",first_hsp.sbjct_end)

