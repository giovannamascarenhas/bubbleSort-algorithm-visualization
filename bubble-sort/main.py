import random
from matplotlib import pyplot as plt


def bubble_sorting(array: list) -> list:
    """ 
    This function implements the bubble sort 
    algorithm.
    """
    array_lenght = len(array)
    for element in range(array_lenght):
        already_sort = True
        for item in range(array_lenght - element - 1):
            if array[item] > array[item + 1]:
                array[item], array[item + 1] = array[item + 1], array[item]
                already_sort = False
        if already_sort:
            break
    return array


def visualize():
    """ 
    This functions shows the algorithm in the Matplotlib.
    """
    array_lenght = 30
    my_array = list(range(1, array_lenght + 1)) 
    random.shuffle(my_array)

    generator = bubble_sorting(my_array)

    fig, ax = plt.subplots() 
    ax.set_title("Bubble Sort O(n)") 
    bar_sub = ax.bar(range(len(my_array)), my_array, align="edge")

    ax.set_xlim(0, array_lenght) 
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes) 
    iteration = [0]

    plt.show() 
    plt.close() 
    

if __name__ == '__main__':
    visualize()
