import numpy as np
import random
import os


def main_menu():
    print(
        "\n  ~~~ MENU ~~~\n1.Lowest to Highest\n2.Highest to Lowest\n3.The Knapsack problem with RI\n4.Exit")
    action = int(input("Go to: "))

    if action == 1:
        print("\nThe Knapsack problem with Lowest to Highest")
        lower_heuristic(weight_final, items_ks)
    elif action == 2:
        print("\nThe Knapsack problem with Highest to Lowest")
        highest_heuristic(weight_final, items_ks)
    elif action == 3:
        print("\nThe Knapsack problem with RI")
        ri_heuristic(weight_final, items_ks)
    else:
        print("\nBye, try again :)")


def lower_heuristic(weight_final, items_ks):
    file_name = input("Give me the file name: ")
    file_aux = np.genfromtxt(file_name, dtype="int", skip_header=1, usecols=(1, 2))
    print("File name -> results_LOW.txt")

    column_value = file_aux[:, [0]]
    column_weight = file_aux[:, [1]]
    column_id = []
    c_value_new = []
    c_weight_new = []
    ks_final = []
    feasible_value = 0
    weight_aux = weight_final
    w_aux = 0

    for i in range(items_ks):
        if column_weight[i] <= weight_aux:
            column_id.append(i + 1)
            feasible_value += column_value[i]
            c_value_new.append(column_value[i])
            w_aux += column_weight[i]
            c_weight_new.append(column_weight[i])
            weight_aux -= column_weight[i]

    ks_final.append(column_id)
    ks_final.append(c_value_new)
    ks_final.append(c_weight_new)
    ks_aux = np.transpose(ks_final)
    np.savetxt("results_LOW.txt", ks_aux, delimiter=" ", header="vi wi", fmt="%i")  
    file = open("results_LOW.txt", "a")
    file.writelines("\nInstance: " + str(items_ks))
    file.writelines("\nNumber of items: " + str(len(column_id)))
    file.writelines("\nWeight to be used: " + str(weight_final))
    file.writelines("\nFinal weight: " + str(w_aux))
    file.writelines("\nFinal output [X]: " + str(feasible_value))
    file.close()
    main_menu()


def highest_heuristic(weight_final, items_ks):
    file_name = input("Give me the file name: ")
    file_aux = np.genfromtxt(file_name, dtype="int", skip_header=1, usecols=(1, 2))
    print("File name -> results_HIGH.txt")

    c_value_sort = file_aux[(-file_aux[:, 1]).argsort()]
    column_value = c_value_sort[:, [0]]
    column_weight = c_value_sort[:, [1]]
    column_id = []
    c_value_new = []
    c_weight_new = []
    ks_final = []
    feasible_value = 0
    weight_aux = weight_final
    w_aux = 0

    for i in range(items_ks):
        if column_weight[i] <= weight_aux:
            column_id.append(i + 1)
            feasible_value += column_value[i]
            c_value_new.append(column_value[i])
            w_aux += column_weight[i]
            c_weight_new.append(column_weight[i])
            weight_aux -= column_weight[i]

    ks_final.append(column_id)
    ks_final.append(c_value_new)
    ks_final.append(c_weight_new)
    ks_aux = np.transpose(ks_final)
    np.savetxt(
        "results_HIGH.txt", ks_aux, delimiter=" ", header="vi wi", fmt="%i"
    ) 
    file = open("results_HIGH.txt", "a")
    file.writelines("\nInstance: " + str(items_ks))
    file.writelines("\nNumber of items: " + str(len(column_id)))
    file.writelines("\nWeight to be used: " + str(weight_final))
    file.writelines("\nFinal weight: " + str(w_aux))
    file.writelines("\nFinal output [X]: " + str(feasible_value))
    file.close()
    main_menu()


def ri_heuristic(weight_final, items_ks):
    file_name = input("Give me the file name: ")
    file_aux = np.genfromtxt(file_name, dtype="int", skip_header=1, usecols=(1, 2))
    print("File name -> results_RI.txt")

    column_value = file_aux[:, [0]]
    column_weight = file_aux[:, [1]]
    column_WN = []
    column_WN = column_weight
    column_ri = np.divide(column_value, column_weight)

    column_id = []
    c_value_new = []
    c_weight_new = []
    ks_final = []
    feasible_value = 0
    weight_aux = weight_final
    w_aux = 0

    for i in range(items_ks):
        if column_ri[i] <= weight_aux:
            column_id.append(i + 1)
            feasible_value += column_value[i]
            c_value_new.append(column_value[i])
            w_aux += column_WN[i]
            c_weight_new.append(column_WN[i])
            weight_aux -= column_WN[i]
        else:
            break

    ks_final.append(column_id)
    ks_final.append(c_value_new)
    ks_final.append(c_weight_new)
    ks_aux = np.transpose(ks_final)
    np.savetxt(
        "results_RI.txt", ks_aux, delimiter=" ", header="vi wi", fmt="%i"
    )
    file = open("results_RI.txt", "a")
    file.writelines("\nInstance: " + str(items_ks))
    file.writelines("\nNumber of items: " + str(len(column_id)))
    file.writelines("\nWeight to be used: " + str(weight_final))
    file.writelines("\nFinal weight: " + str(w_aux))
    file.writelines("\nFinal output [X]: " + str(feasible_value))
    file.close()
    main_menu()


print("The Knapsack problem with integer generator\n")
items_ks = int(input("Give me the number of items: "))
value_min = int(input("Value[min] of items: "))
value_max = int(input("Value[max] of items: "))
weight_min = int(input("Give me the Weight[min] of knapsack: "))
weight_max = int(input("Give me the Weight[max] of knapsack: "))
weight_average = ((weight_min + weight_max) / 2) * items_ks * 0.3
weight_final = int(weight_average)
print("Weight to be used: " + str(weight_final))
if weight_final > 1:
    pass
else:
    print("No negative numbers!")

id = []
values = []
weights = []
knapsack = []

for i in range(items_ks):
    id.append(i + 1)
    values_random = random.randint(value_min, value_max)
    values.append(values_random)
    weight_random = random.randint(weight_min, weight_max)
    weights.append(weight_random)

knapsack.append(id)
knapsack.append(values)
knapsack.append(weights)
knapsack_final = np.transpose(knapsack)
np.savetxt(
    "instance.txt", knapsack_final, delimiter=" ", header="vi wi", fmt="%i"
) 
new_name = "{}_{}.txt".format("instance", items_ks)
os.rename("instance.txt", new_name)

main_menu()
