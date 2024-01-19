# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not hashable(key):
            key = str(key)
        result[value] = key
    return result


def hashable(key):
    try:
        hash(key)
        return True
    except TypeError:
        return False


params = create_dict(a=1, b='text', c=(1, 2, 3))
print(params)
