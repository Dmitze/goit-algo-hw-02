# Домашнє завдання: Основні структури даних

## Опис проекту
1. Черга (Queue) - система обробки заявок
2. Двостороння черга (deque) - перевірка паліндромів
3. Стек (Stack) - перевірка симетрії дужок

## Структура файлів
- `task1_queue.py` - система обробки заявок у сервісному центрі
- `task2_palindrome.py` - перевірка, чи є рядок паліндромом
- `task3_brackets.py` - перевірка симетрії дужок у виразах

## Приклади виконання програми

```console
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-02> python task1_queue.py
Додано заявку: Request_470
Обробляється заявка: Request_470
Черга порожня
Розмір черги: 0
Додано заявку: Request_948
Додано заявку: Request_325
Обробляється заявка: Request_948
Обробляється заявка: Request_325
Розмір черги: 0
Додано заявку: Request_653
Обробляється заявка: Request_653
Черга порожня
Розмір черги: 0
...
Traceback (most recent call last):
  File "C:\Users\dmitz\Documents\GitHub\goit-algo-hw-02\task1_queue.py", line 28, in <module>
    time.sleep(2)
KeyboardInterrupt
```

```console
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-02> python task2_palindrome.py
'А роза упала на лапу...' -> паліндром
'мадам...' -> паліндром
'hello...' -> не паліндром
'12321...' -> паліндром
```

```console
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-02> python task3_brackets.py  
'( ){[ 1 ]( 1 + 3 )( ...' -> Симетрично
'( 23 ( 2 - 3);...' -> Несиметрично
'( 11 }...' -> Несиметрично
'{[()]}...' -> Симетрично
```
