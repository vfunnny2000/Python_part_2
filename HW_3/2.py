# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.


import string

with open('sample.txt', 'r', encoding='UTF-8') as file:
    data = file.read()

for char in string.punctuation:
    data = data.lower().replace(char, ' ')

counter_dict = {}

for word in data.split():
    counter_dict[word] = counter_dict.get(word, 0) + 1

counter_dict = tuple(sorted(counter_dict.items(), key=lambda item: item[1]))
for index, word in enumerate(counter_dict[-1:-11:-1], 1):
    print(f'{index}. {word[0]:>10} {word[1]} раз')
    
    
# -------------ВАРИАНТ --------------------------------    
# import re
# from collections import Counter

# text = """Эталонной реализацией Python является интерпретатор CPython, который поддерживает большинство активно используемых платформ[38] 
# и являющийся стандартом де-факто языка[39]. Он распространяется под свободной лицензией Python Software Foundation License, 
# позволяющей использовать его без ограничений в любых приложениях, включая проприетарные[40]. CPython компилирует исходные тексты в 
# высокоуровневый байт-код, который исполняется в стековой виртуальной машине[41]. К другим трём основным реализациям языка относятся 
# Jython (для JVM), IronPython (для CLR/.NET) и PyPy[26][42]. PyPy написан на подмножестве языка Python (RPython) и разрабатывался как 
# альтернатива CPython с целью повышения скорости исполнения программ, в том числе за счёт использования JIT-компиляции[42]. 
# Поддержка версии Python 2 закончилась в 2020 году[43]. На текущий момент активно развивается версия языка Python 3[44].
# Разработка языка ведётся через предложения по расширению языка PEP (англ. Python Enhancement Proposal), в которых описываются нововведения, 
# делаются корректировки согласно обратной связи от сообщества и документируются итоговые решения[45]."""

# def top_10_words(text):
#     words = re.findall(r'\b\w+\b', text.lower())
#     return Counter(words).most_common(10)

# print(top_10_words(text))