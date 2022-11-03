from vector_functions import dot_product

#           toes/win/fins
weights = [[0.1, 0.1, -0.3],
           [0.1, 0.2, 0.0],
           [0.0, 1.3, 0.1]]

# data
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]  # Win-loss record
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]


def neural_network(input, weights):

    output = [0,0,0]

    for i in range(len(weights)):
        output[i] = dot_product(input, weights[i])

    return output

pred = neural_network(input, weights)
print(pred)
