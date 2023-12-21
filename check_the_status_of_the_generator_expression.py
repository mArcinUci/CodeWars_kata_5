# https://www.codewars.com/kata/585e6eb2eec14124ea000120

gen = (i for i in range(4))


import inspect
def check_generator(gen):
    if inspect.getgeneratorstate(gen) == 'GEN_CREATED':
        return 'Created'
    if inspect.getgeneratorstate(gen) == 'GEN_RUNNING':
        return 'Started'
    if inspect.getgeneratorstate(gen) == 'GEN_SUSPENDED':
        return 'Started'
    if inspect.getgeneratorstate(gen) == 'GEN_CLOSED':
        return 'Finished'
    

print(check_generator(gen))