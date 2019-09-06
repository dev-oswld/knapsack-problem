import numpy as np
import random
import os


def main_menu():
    print(
        "\n  ~~~ MENU ~~~\n1.Lowest to Highest\n2.Highest to Lowest\n3.The Knapsack problem with RI\n4.Exit"
    )
    goto = int(input("Go to: "))

    if goto == 1:
        print("\nThe Knapsack problem with Lowest to Highest")
        lower_heuristic(weightNEWKS, itemsKS)
    elif goto == 2:
        print("\nThe Knapsack problem with Highest to Lowest")
        highest_heuristic(weightNEWKS, itemsKS)
    elif goto == 3:
        print("\nThe Knapsack problem with RI")
        ri_heuristic(weightNEWKS, itemsKS)
    else:
        print("\nBye, try again :)")


def lower_heuristic(weightNEWKS, itemsKS):
    DataFile = input("Give me the file name: ")
    file_aux = np.genfromtxt(DataFile, dtype="int", skip_header=1, usecols=(1, 2))
    print("File name -> results_LOW.txt")  # print (file_aux)

    column_value = file_aux[:, [0]]
    column_weight = file_aux[:, [1]]
    column_id = []
    column_valueN = []  # Array news in 1D
    column_weightN = []
    KS_final = []
    Feasible_value = 0
    weight_aux = weightNEWKS
    w_aux = 0

    for i in range(itemsKS):
        if column_weight[i] <= weight_aux:
            column_id.append(i + 1)
            Feasible_value += column_value[i]
            column_valueN.append(column_value[i])
            w_aux += column_weight[i]
            column_weightN.append(column_weight[i])
            weight_aux -= column_weight[i]

    KS_final.append(column_id)
    KS_final.append(column_valueN)
    KS_final.append(column_weightN)
    KS_NewFinal = np.transpose(KS_final)
    np.savetxt(
        "results_LOW.txt", KS_NewFinal, delimiter=" ", header="vi wi", fmt="%i"
    )  # Writing in the file with the new data
    File = open("results_LOW.txt", "a")  # Writing in the file with the new data
    File.writelines("\nInstance: " + str(itemsKS))
    File.writelines("\nNumber of items: " + str(len(column_id)))
    File.writelines("\nWeight to be used: " + str(weightNEWKS))
    File.writelines("\nFinal weight: " + str(w_aux))
    File.writelines("\nFinal output [X]: " + str(Feasible_value))
    File.close()
    main_menu()


def highest_heuristic(weightNEWKS, itemsKS):
    DataFile = input("Give me the file name: ")
    file_aux = np.genfromtxt(DataFile, dtype="int", skip_header=1, usecols=(1, 2))
    print("File name -> results_HIGH.txt")  # print (file_aux)

    c_valueSort = file_aux[(-file_aux[:, 1]).argsort()]
    column_value = c_valueSort[:, [0]]
    column_weight = c_valueSort[:, [1]]
    column_id = []
    column_valueN = []  # Array news in 1D
    column_weightN = []
    KS_final = []
    Feasible_value = 0
    weight_aux = weightNEWKS
    w_aux = 0

    for i in range(itemsKS):
        if column_weight[i] <= weight_aux:
            column_id.append(i + 1)
            Feasible_value += column_value[i]
            column_valueN.append(column_value[i])
            w_aux += column_weight[i]
            column_weightN.append(column_weight[i])
            weight_aux -= column_weight[i]

    KS_final.append(column_id)
    KS_final.append(column_valueN)
    KS_final.append(column_weightN)
    KS_NewFinal = np.transpose(KS_final)
    np.savetxt(
        "results_HIGH.txt", KS_NewFinal, delimiter=" ", header="vi wi", fmt="%i"
    )  # Writing in the file with the new data
    File = open("results_HIGH.txt", "a")  # Writing in the file with the new data
    File.writelines("\nInstance: " + str(itemsKS))
    File.writelines("\nNumber of items: " + str(len(column_id)))
    File.writelines("\nWeight to be used: " + str(weightNEWKS))
    File.writelines("\nFinal weight: " + str(w_aux))
    File.writelines("\nFinal output [X]: " + str(Feasible_value))
    File.close()
    main_menu()


def ri_heuristic(weightNEWKS, itemsKS):
    DataFile = input("Give me the file name: ")
    file_aux = np.genfromtxt(DataFile, dtype="int", skip_header=1, usecols=(1, 2))
    print("File name -> results_RI.txt")  # print (file_aux)

    column_value = file_aux[:, [0]]
    column_weight = file_aux[:, [1]]
    column_WN = []
    column_WN = column_weight
    column_ri = np.divide(column_value, column_weight)

    column_id = []
    column_valueN = []  # Array news in 1D
    column_weightN = []
    KS_final = []
    Feasible_value = 0
    weight_aux = weightNEWKS
    w_aux = 0

    for i in range(itemsKS):
        if column_ri[i] <= weight_aux:
            column_id.append(i + 1)
            Feasible_value += column_value[i]
            column_valueN.append(column_value[i])
            w_aux += column_WN[i]
            column_weightN.append(column_WN[i])
            weight_aux -= column_WN[i]
        else:
            break

    KS_final.append(column_id)
    KS_final.append(column_valueN)
    KS_final.append(column_weightN)
    KS_NewFinal = np.transpose(KS_final)
    np.savetxt(
        "results_RI.txt", KS_NewFinal, delimiter=" ", header="vi wi", fmt="%i"
    )  # Writing in the file with the new data
    File = open("results_RI.txt", "a")  # Writing in the file with the new data
    File.writelines("\nInstance: " + str(itemsKS))
    File.writelines("\nNumber of items: " + str(len(column_id)))
    File.writelines("\nWeight to be used: " + str(weightNEWKS))
    File.writelines("\nFinal weight: " + str(w_aux))
    File.writelines("\nFinal output [X]: " + str(Feasible_value))
    File.close()
    main_menu()


print("The Knapsack problem with integer generator\n")
itemsKS = int(input("Give me the number of items: "))
valueMIN = int(input("Value[min] of items: "))
valueMAX = int(input("Value[max] of items: "))
weightMINKS = int(input("Give me the Weight[min] of knapsack: "))
weightMAXKS = int(input("Give me the Weight[max] of knapsack: "))
aux = ((weightMINKS + weightMAXKS) / 2) * itemsKS * 0.3
weightNEWKS = int(aux)  # Double cast, float to int to string
print("Weight to be used: " + str(weightNEWKS))
if weightNEWKS > 1:
    pass
else:
    print("No negative numbers!")

id = []
values = []  # For each column
weights = []
knapsack = []

for i in range(itemsKS):
    id.append(i + 1)
    valuesRandom = random.randint(valueMIN, valueMAX)  # Generate the random numbers
    values.append(valuesRandom)
    weightRandom = random.randint(weightMINKS, weightMAXKS)
    weights.append(weightRandom)

knapsack.append(id)
knapsack.append(values)
knapsack.append(weights)
knapsack_final = np.transpose(knapsack)
np.savetxt(
    "instance.txt", knapsack_final, delimiter=" ", header="vi wi", fmt="%i"
)  # Writing in the file with the new data
# New lines for file name
new_name = "{}_{}.txt".format("instance", itemsKS)
os.rename("instance.txt", new_name)

main_menu()
