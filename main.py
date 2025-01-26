from random import random


# скопируй сюда функции initial_data(), predict(image, weights, b), learn(weights, b, x, y) и read_image()
def initial_data():
    # скопируй свою функцию сюда
    weights = []
    for i in range(0, 784):
        weights.append(random())
    b = random()
    # print (weights)
    # print (b)

    return weights, b


def predict(image, weights, b):
    # скопируй свою функцию сюда
    count = 0
    for i in range(0, 784):
        pixel = image[i]
        wei = weights[i]
        count += pixel * wei
    otvet = count + b
    if otvet > 0:
        return 1
    else:
        return 0


def learn(weights, b, x, y):
    # пиши новый код здесь
    for i in range(30):
        for j in range(len(x)):
            predicted_res = predict(x[j], weights, b)
            d_loss = 2 * (predicted_res - y[j])
            for n in range(len(weights)):
                weights[n] = weights[n] - 0.001 * x[j][n] * d_loss
    return weights, b


def read_image():
    # пиши код здесь
    image = []
    for i in range(28):
        strochka = input()
        for j in range(len(strochka)):
            res = strochka[j]
            if res == '-':
                res = 0
            elif res == '+':
                res = 1
            image.append(res)
    return image


x, y = load_data()
# допиши программу
image_inp = read_image()
weights, b = initial_data()
weights, b = learn(weights, b, x, y)
otvet = predict(image_inp, weights, b)
print(otvet)