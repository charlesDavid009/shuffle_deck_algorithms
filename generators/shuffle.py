from time import time
import randoms
import xorshift

seedlcg = randoms.seedLCG
lcg = randoms.lcg
xor = xorshift.XORShift(1)

def start():
    print("Welcome To Random Generator\n\n")
    rounds = int(input("Please enter the amount of time you would wish run the generator: \n"))
    if rounds < 1:
        print("number can't be less than 1")
    elif rounds > 10000:
        print("number can't be gerater than 10,000")

    print("Enter the type of generator you wish to run\n")
    print("Enter 1 for Js random generator\n")
    print("Enter 2 for XorShift generator\n")
    print("Enter 3 for SH501a.c generator\n")
    choice = int(input("Please enter your choice here: "))
    print("\n-----starting generator-----\n")

    if choice == 1:
        seedlcg(1)
        start_time = time()
        for i in range(rounds):
            print("js random generated {}".format(lcg()))
        end_time = time()
        total = (start_time + end_time)
        performance_interval = (end_time - start_time)

        print("\nstart time {} microseconds".format(start_time))
        print("Code ended time is {} microseconds".format(end_time))
        print("total time code ran for {} microseconds".format(total))
        print("performance_interval time code ran for {} microseconds".format(
            performance_interval))

    elif choice == 2:
        start_time = time()
        for i in range(rounds):
            print("Xor shift random generated: {}".format(xor.random()))
        end_time = time()
        total = (start_time + end_time)
        performance_interval = (end_time - start_time)
        print("\nstart time {} microseconds".format(start_time))
        print("Code ended time is {} microseconds".format(end_time))
        print("total time code ran for {} microseconds".format(total))
        print("performance_interval time code ran for {} microseconds".format(
            performance_interval))

    elif choice == 3:
        pass
    else:
        pass


start()

