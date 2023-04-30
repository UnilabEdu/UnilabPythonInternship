# yield from

def expensive_process(var):
    return var


def generator_till_2010():
    for i in range(10):
        yield i


def generator_for_2010_2020():
    for j in range(10, 21):
        yield j


def with_generator():
    yield from generator_till_2010()

    yield from generator_for_2010_2020()

    print("reached the end")


sum_number = 0
for elem in with_generator():
    sum_number += elem

print(sum_number)
