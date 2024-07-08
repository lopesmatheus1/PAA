import random
import time
import matplotlib.pyplot as plt


def particao(arr, baixo, alto):
    pivo = arr[alto]
    i = baixo - 1

    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1


def quicksort(arr, baixo, alto):
    pilha = [(baixo, alto)]

    while pilha:
        baixo, alto = pilha.pop()
        if baixo < alto:
            pivo = particao(arr, baixo, alto)
            pilha.append((baixo, pivo - 1))
            pilha.append((pivo + 1, alto))


def insertionsort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave


tamanhos = [50, 500, 5000, 50000]
ordem_labels = ['Ordem Crescente', 'Ordem Decrescente', 'Ordem Aleatória']

for ordem_label in ordem_labels:
    fig, ax = plt.subplots(figsize=(6, 5))
    tempos_execucao_quicksort = []
    tempos_execucao_insertionsort = []

    for tamanho in tamanhos:
        if ordem_label == 'Ordem Aleatória':
            arr_quicksort = random.sample(range(tamanho), tamanho)
            arr_insertionsort = arr_quicksort[:]
        elif ordem_label == 'Ordem Crescente':
            arr_quicksort = list(range(tamanho))
            arr_insertionsort = arr_quicksort[:]
        else:
            arr_quicksort = list(range(tamanho, 0, -1))
            arr_insertionsort = arr_quicksort[:]

        inicio = time.perf_counter()
        quicksort(arr_quicksort, 0, len(arr_quicksort) - 1)
        fim = time.perf_counter()
        tempo_execucao_quicksort = fim - inicio
        tempos_execucao_quicksort.append(tempo_execucao_quicksort)
        print(f"Tempo de execução do Quick Sort para {ordem_label} e tamanho {tamanho}: {tempo_execucao_quicksort:.6f} segundos")

        inicio = time.perf_counter()
        insertionsort(arr_insertionsort)
        fim = time.perf_counter()
        tempo_execucao_insertionsort = fim - inicio
        tempos_execucao_insertionsort.append(tempo_execucao_insertionsort)
        print(f"Tempo de execução do Insertion Sort para {ordem_label} e tamanho {tamanho}: {tempo_execucao_insertionsort:.6f} segundos")

    ax.plot(tamanhos, tempos_execucao_quicksort, marker='.', label='Quick Sort')
    ax.plot(tamanhos, tempos_execucao_insertionsort, marker='.', label='Insertion Sort')
    ax.set_ylabel('Tempo de Execução')
    ax.set_xlabel('Tamanho do Vetor')
    ax.set_title(ordem_label)
    ax.legend()

    plt.tight_layout()
    plt.show()
