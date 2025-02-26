from itertools import permutations

# Исходное слово
word = "абракадабра"

# Генерируем все возможные уникальные слова длиной 4

result_set = set(permutations(word, 4))

# Преобразуем кортежи в строки
unique_words = [''.join(p) for p in result_set]

# Сортируем слова для упорядоченного вывода
unique_words.sort()

# Выводим количество уникальных слов и первые 10 слов
print(f"Количество различных слов: {len(unique_words)}")
print("Первые 10 слов:")
for word in unique_words[:10]:  # Выводим только первые 10 слов
    print(word)
