"""
Напишите функцию partial, которая принимает функцию (обозначим ее func),
а также произвольный набор позиционных (назовем их fixated_args) и именованных
(назовем их fixated_kwargs) аргументов и возвращет новую функцию,
которая обладает следующими свойствами:

1.При вызове без аргументов повторяет поведение функции func, вызванной
с fixated_args и fixated_kwargs.
2.При вызове с позиционными и именованными аргументами дополняет ими
fixated_args (приписывает в конец списка fixated_args), и fixated_kwargs
(приписывает новые именованные аргументы и переопределяет значения старых)
и далее повторяет поведение func с этим новым набором аргументов.
3.Имеет __name__ вида partial_<имя функции func>
4.Имеет docstring вида:

A partial implementation of <имя функции func>
with pre-applied arguements being:
<перечисление имен и значений fixated_args и fixated_kwargs>
"""


def my_sum(a, b=2):
    return a+b


def partial(func, *fixated_args, **fixated_kwargs):
    def customizer(*args, **kwargs):
        customizer.__name__ = "partial_"+func.__name__
        customizer.__doc__ = f"""
        A partial implementation of {func.__name__}
        with pre-applied arguements being:
        {fixated_args},{fixated_kwargs}
        """

        return func(*(args+fixated_args), **{**fixated_kwargs, **kwargs})

    if not fixated_kwargs and not fixated_args:
        return func
    return customizer


my = partial(my_sum, a=1)
print(my(b=4, a=4))
input()
print(round(3.333))
my = partial(round, ndigits=2)
print(my(3.33333))
print(my(3.33333))
print(my(3.33333))
print(my(3.33333))
print(my(3.33333))
print(my.__name__)
print(my.__doc__)