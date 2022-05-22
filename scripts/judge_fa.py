from Bio import SeqIO

my_file = "../inputfiles/26cefcb8-d023-11ec-97fa-0242ac110002"  # Obviously not FASTA


def is_fasta(filename):
    with open(filename, "r") as handle:
        fasta = SeqIO.parse(handle, "fasta")
        return any(fasta)


print(is_fasta(my_file))
