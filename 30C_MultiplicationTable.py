'''

Create a program that generates multiplcation tables
for the numbers 0 through 12.

___________________
Example Output
___________________
0 x 0 = 0
0 x 1 = 0
....
12 x 11 = 132
12 x 12 = 144

___________________
Constraint
___________________
Use a nested loop to complete this program

'''
def main():

    first_layer = [str(num).center(5) for num in range(0,13)]
    layers = [first_layer] + [[str(num1 * num2).center(5) for num2 in range(0,13)] for num1 in range(0,13)]
    layer_val = ''

    for layer in range(len(layers)):
        layers[layer] = [layer_val.center(5)] + layers[layer]
        layers[layer] = '|'.join(layers[layer])
        layer_val = str(layer)

    out = ('\n' + '-'*(14*6) + '\n').join(layers)
    print(out)

main()
