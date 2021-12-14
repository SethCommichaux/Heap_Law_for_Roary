# Heap_Law_for_Roary
This python3 program calculates the Heap Law from the gene_presence_absence.Rtab Roary output file.

Here we estimate the parameters k and γ for the Heap Law equation:
n = κN<sup>γ</sup>

If γ < 0, the pangenome is closed. If γ > 0, the pangenome is open.

See this paper for an explanation of the Heap Law: Large-Scale Genomics Reveals the Genetic Characteristics of Seven Species and Importance of Phylogenetic Distance for Estimating Pan-Genome Size

Basic usage:
```
python Roary_Heaps_Law.py gene_presence_absence.Rtab <number of permutations>
```

Example command that performs 100 permutations
```
python Roary_Heaps_Law.py gene_presence_absence.Rtab 100
```

