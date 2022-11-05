import random
from util import *


def generate_kromosom(panjang_kromosom=PANJANG_KROMOSOM):

    kromosom = ""
    for _ in range(panjang_kromosom):
        kromosom += str(random.randint(0, 9))

    return kromosom


def generate_populasi(banyak_populasi=POPULATION_SIZE, panjang_kromosom=PANJANG_KROMOSOM):

    populasi = []

    for _ in range(banyak_populasi):
        populasi.append(generate_kromosom(panjang_kromosom))

    return populasi


def decode(kromosom):

    kromosom_x = int(kromosom[:(PANJANG_KROMOSOM//2)])
    kromosom_y = int(kromosom[(PANJANG_KROMOSOM//2):])
    x = -5 + ((kromosom_x-0) /
              (int("9"*len(kromosom[:(PANJANG_KROMOSOM//2)]))-0))*(5-(-5))
    y = -5 + ((kromosom_y-0) /
              (int("9"*len(kromosom[(PANJANG_KROMOSOM//2):]))-0))*(5-(-5))

    return x, y


def fitness(kromosom, a=A):
    return 1/(heuristic(decode(kromosom)[0], decode(kromosom)[1])+a)


def mutasi(kromosom, prob=PROBABILITAS_MUTASI):
    krom = kromosom
    for i in range(len(krom)):
        if random.random() < prob:
            krom = krom[:i] + str(random.randint(0, 9)) + krom[i+1:]

    return krom


def crossover(kromosom1, kromosom2, prob=PROBABILITAS_CROSSOVER):
    kromo1 = kromosom1
    kromo2 = kromosom2

    if random.random() < prob:
        tipot = random.randint(0, len(kromo1) - 1)
        kromo3 = kromo1[:tipot] + kromo2[tipot:]
        kromo4 = kromo2[:tipot] + kromo1[tipot:]
    else:
        kromo3 = kromo1
        kromo4 = kromo2

    return kromo3, kromo4


def best_kromosom(gen):
    gen.sort(key=lambda x: fitness(x), reverse=True)

    return gen[0]


def get_mating_pool(gen):
    mating_pool = []
    for i in range(len(gen)):
        # mirip dengan roulette wheel
        [terpilih] = random.choices(
            gen, weights=[fitness(kromosom) for kromosom in gen])
        mating_pool.append(terpilih)

    return mating_pool


def next_generation(gen):
    mating_pool = get_mating_pool(gen)
    next_gen = []
    for i in range(0, len(gen), 2):
        anak1, anak2 = crossover(mating_pool[i], mating_pool[i+1])
        next_gen.append(mutasi(anak1))
        next_gen.append(mutasi(anak2))
    result = []
    gen.sort(key=lambda x: fitness(x), reverse=True)
    result = gen[:2]+next_gen[2:len(gen)]

    return result


def print_generasi(generasi):
    for i in range(len(generasi)):
        print("\"{}\" ({:5f},{:5f}) : {}".format(generasi[i], decode(
            generasi[i])[0], decode(generasi[i])[1], fitness(generasi[i])))
