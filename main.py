from algoritmagenetika import generate_populasi, decode, best_kromosom, next_generation, print_generasi


def main():

    generasi = []
    generasi = generate_populasi()
    print("Generasi 1")
    print_generasi(generasi)
    best = best_kromosom(generasi)

    termination = 500
    i = 2
    while termination > 0:
        generasi = next_generation(generasi)
        print("Generasi {}".format(i))
        print_generasi(generasi)

        if best == best_kromosom(generasi):
            termination -= 1
        else:
            best = best_kromosom(generasi)
            termination = 500

        i += 1

    print("=============================================================")
    print("hasil akhir")
    print("berhenti di generasi ke {}".format(i-1))
    print("kromosom terbaik : {}".format(best))
    print("nilai x : {}".format(decode(best)[0]))
    print("nilai y : {}".format(decode(best)[1]))


if __name__ == "__main__":
    main()
