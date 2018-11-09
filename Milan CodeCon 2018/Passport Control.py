#Problem        : Passport Control
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

"""
WARNING: this code has been written AFTER the contest has ended. It means the solution
has not been submitted and there is no guarantee it is the actual working solution.
"""

class Booth:
    def __init__(self):
        # indica i minuti mancanti prima che il booth sia disponibile ESCLUDENDO LA PAUSA
        # percio' 0 = disponibile
        # ad ogni ciclo va decrementato di 1
        self.available = 0
        
        # contiene il numero di gruppi fatti, ovvero la risposta dell'esercizio
        # quando assegni un gruppo questo va incrementato di 1
        self.gruppi_fatti = 0
        
        # quando sale a 10 il booth va in pausa (e si resetta questo valore a 0)
        self.gruppi_fatti_mod_10 = 0
        
        # indica quanti minuti di pausa mancano al booth prima di tornare disponibile
        # percio' 0 = disponibile
        # ogni 10 gruppi va settato a 5 e si decrementa di 1 ad ogni ciclo
        self.pausa = 0
        
        # un booth e' libero se available <= 0 and pausa <= 0
        
def schedule(N, M, booths, groups, i):    
    for n in range(N):
        if i >= M: return i
        booth = booths[n]
        if booth.available <= 0 and booth.pausa <= 0:
            booth.available = groups[i]
            booth.gruppi_fatti += 1
            booth.gruppi_fatti_mod_10 += 1;
            i += 1
    return i
        
N = int(input())
M = int(input())

booths = []
for n in range(N):
    booths.append(Booth())
groups = []
for m in range(M):
    groups.append(int(input()))

i = 0
while i < M:
    i = schedule(N, M, booths, groups, i)
    for n in range(N):
        booth = booths[n]
        booth.available -= 1
        booth.pausa -= 1
        if booth.gruppi_fatti_mod_10 == 10:
            booth.pausa = 5
            booth.gruppi_fatti_mod_10 = 0

ans = []
for booth in booths:
    ans.append(str(booth.gruppi_fatti))

print(' '.join(ans))