#!/usr/bin/env python3

from pyGeno.Genome import Genome, Gene, Transcript, Exon
from pyGeno.tools.UsefulFunctions import translateDNA

genome = 'GRCh38.98'
gene_name = 'TP53'
isoform_id = 'ENST00000269305'

position = 131  # counted in amino acids; 0-based
aa = 'K'  # amino acid at position 132, Lysine (K)
kmer_size = 31  # counted in nucleotides

p = position
# kmer size rounded up to the closest multiple of 3
k = ((kmer_size // 3) + int(bool((kmer_size % 3)))) * 3

start = p * 3 - k
end = p * 3 + 3 + k

# ##########
# 1. Let's query the databse using our transcript ID
# ##########

# First, we define the reference
ref = Genome(name = genome)

transcript = ref.get(Transcript, id=isoform_id)[0]

seq = transcript.cDNA[start:end]
# query protein sequence to make we retreived the correct series of nucleotides
prot = transcript.protein.sequence[p-(k//3) : p+1+(k//3)]
print(seq)
print(prot)
print(translateDNA(seq) == prot)

# ##########
# 2. Ok, what if we don't have a transcript ID
# ##########

gene = ref.get(Gene, name=gene_name)[0]

transcripts = gene.get(Transcript)

# get transcript lengths in terms of their coding sequence (CDS)
cds_lengths = [len(t.cDNA) for t in transcripts]

# sort transcripts starting from the longest to the shortest
transcripts, cds_lengths = zip(*sorted(zip(transcripts, cds_lengths), key=lambda x: x[1], reverse=True))

# let's have a sneak peak at our top 5 candidates
for t in transcripts[:5]:
    # print transcript ID and biotype
    print(t.id, t.biotype, len(t.cDNA))

# oops, the longest transcript is not protein coding, and the next 2 are in a tie
print('Discarding the longest transcript')

# we need a way to choose between them, let's look at the length of the whole sequence
# including the 5'UTR and the 3'UTR
for t in transcripts[1:3]:
    print(t.id, t.biotype, len(t.cDNA), len(t.sequence))

# Because we have no other information, we will go with the one with the longest UTRs
# Keep in mind that this might not necesseraly be the most biologically relevant isoform
print('Best candidate: ENST00000269305')
print('We have recovered our original isoform!')

# ##########
# 3. Now, time to print our sequence in fasta format
# ##########

print('--------------------')
print('Printing fasta below')
print('--------------------')

chrom = transcript.chromosome.number
strand = transcript.gene.strand

# let's find our start and end positions on the chromosome
passed_over_pos = 0  # nucleotides we have already covered
for exon in transcript.get(Exon):
    if passed_over_pos >= end:
        break
    cur_start = max(0, start - passed_over_pos)
    cur_end = end - passed_over_pos

    if exon.hasCDS():
        # update value
        passed_over_pos += len(exon.CDS)

        if len(exon.CDS) >= cur_start:
            # nucleotides
            part_seq = ''.join(exon.CDS[cur_start:cur_end])

            # be careful when your gene is on the opposite strand
            if strand == '+':
                chrom_start = exon.start + len(exon.UTR5)
                chrom_end = chrom_start + len(part_seq)
            elif strand == '-':
                chrom_start = exon.end - len(exon.UTR5)
                chrom_end = chrom_start - len(part_seq)
                chrom_start, chrom_end = chrom_end, chrom_start

            # print fasta header
            print(
                    '>chr%s:%d-%d | name=%s | strand=%s | cds=%d-%d | len=%d | exon=%s'
                % (
                    chrom, chrom_start, chrom_end, gene_name, strand, cur_start+1,
                    cur_start+len(part_seq), len(part_seq), exon.id
                )
            )

            # print fasta sequence
            print(part_seq)
