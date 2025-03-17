""" I define a function, prodotto_cartesiano, because permutations, combinations, and arrangements, both simple and non-simple,
 are subsets of the Cartesian product of a set with itself"""

def prodotto_cartesiano(insieme, k):             
    risultato = [[]] 
    for i in range(k):
        risultato = [x + [y] for x in risultato for y in insieme]
    return risultato

insieme = ('a', 'b', 'c')
n = len(insieme)
k = 2
print("Cartesian product: \n", prodotto_cartesiano(insieme, k))





"""Permutations with repetition are subsets of the Cartesian product where we choose sequences
of length k from the set, allowing repetitions."""

permutazioni_con_ripetizione = prodotto_cartesiano(insieme, k)
print("Permutations with repetition: \n", permutazioni_con_ripetizione)




"""Permutations without repetition are subsets of the Cartesian product where we take all
sequences of length n and require that all elements appear only once."""

permutazioni_senza_ripetizione = [elemento for elemento in prodotto_cartesiano(insieme, n) if len(elemento) == len(set(elemento))]
print("Permutations without repetition: \n", permutazioni_senza_ripetizione)





"""Arrangements with repetition are subsets of all possible sequences of length k,
including all ordered combinations with repetition."""

disposizioni_con_ripetizione = prodotto_cartesiano(insieme, k)
print("Arrangements with repetition: \n", disposizioni_con_ripetizione)




"""Arrangements without repetition are subsets of all possible sequences of length k,
considering only sequences in which each element appears at most once."""
disposizioni_senza_ripetizione = [elemento for elemento in prodotto_cartesiano(insieme, k) if len(elemento) == len(set(elemento))]
print("Arrangements without repetition: \n", disposizioni_senza_ripetizione)




"""Combinations with repetition are subsets of all possible sequences of length k,
where different orders of the same sequence are counted as a single combination."""
combinazioni_con_ripetizione = []
for elemento in prodotto_cartesiano(insieme, k):
    elemento.sort()
    if elemento not in combinazioni_con_ripetizione:
        combinazioni_con_ripetizione.append(elemento)
print("Combinations with repetition: \n", combinazioni_con_ripetizione)




"""Simple combinations without repetition are subsets of all possible sequences of length k where each element
can appear only once, and the order does not matter."""
combinazioni_semplici = [elemento for elemento in combinazioni_con_ripetizione if len(elemento) == len(set(elemento))]
print("Combinations without repetition: \n", combinazioni_semplici)
