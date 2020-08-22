
INSERT INTO keyboard VALUES
  (0, ""),
  (1, ""),

  (2, "Аласи|Элементали||Перевёртыши|Артифексы"),
  (3, "Господин|Госпожа"),
  (4, "Да, всё верно!|Нет, давай заново!"),

  (5, ),

  (6, "Карта||Перемещение||Местность||Назад|/Ошибки/"),

  (7, "Глобальная||Местности||Назад"),
  (8, "2196|2191|2197||2190|Координаты|2192||2199|2193|2198||Назад"),
  (9, "Исследовать||Взять задание||Добыча/сбор ресурсов||Особые действия||Назад|."),

  (10, "Характеристика||Статистика||Биография||Записная книжка||Назад|."),
  (11, "Назад|."),
  (12, "Изменить био|Назад"),
  (13, "Отмена|Назад"),
  (14, "Добавить запись||Удалить запись||Назад"),
  (15, "Начать задание||Отказаться от задания||Статистика заданий||Ежедневки||Назад|,");

INSERT INTO message VALUES
  (-1, ""),
  (0, ),
  (1, ),
  (2, ),
  (3, ),

  (4, ),
  (5, "Красивое имя. Теперь укажи свой возраст (от 16 до 90):"),
  (6, "Выбери себе расу. Хорошенько подумай, ты не сможешь изменить её. У каждой из рас есть преимущества и недостатки."),
  (7, "Ты господин или госпожа?"),
  (8, "Опиши себя - амбиции, желания, стремления. Желаешь остаться неизвестным? Отправь точку."),
  (9, "Подтверди, что всё верно. Или создай себя заново!"),
  (10, "Раумор открыт для тебя! Добро пожаловать."),

  (11, "Назад так назад"),

  (12, "Вперёд, на встречу приключениям!"),
  (13, "Мир у твоих ног – разноцветной картинкой."),
  (14, "Стрелочки для перемещения по соседним клеткам, координаты – для дальних расстояний."),
  (15, "Где ты сейчас? Вот тут:"),
  (16, "Вот твоя карта:"),
  (17, "Введи два числа от 0 до 3041 через пробел:"),

  (18, "Все записи о тебе хранятся тут – летопись Раумора."),
  (19, "Вот твои физические данные:"),
  (20, "Вот твои статистические данные:"),
  (21, "Посмотри, что запомнит о тебе весь Раумор:"),
  (22, "Запиши сюда всё мало-мальски важное."),
  (23, "Опиши себя заново:"),
  
  (24, "Пиши:"),
  (25, "Введи номер заметки для удаления:"),
  (26, "Вот взятые тобой задания: "),
  (27, "Выбери номер задания: "),
  (28, "Проверь готовность ежедневных заданий и получи награду!");

INSERT INTO scripts VALUES
  (0, "Что это за место?", 1, 0, 1),
  (1, "Кто ты?", 1, 1, 1),
  (2, "Краткое инфо", 1, 2, 1),
  (3, "О ролевой", 1, 3, 1),

  (4, "Начать приключение!", 1, 4, 0),

  (5, "age", 2, 5, 0),
  (6, "race", 2, 6, 2),
  (7, "gender", 2, 7, 3),
  (8, "bio", 2, 8, 0),
  (9, "confirm", 2, 9, 4),

  (10, "registered", 2, 10, 5),

  (11, "Назад", 1000, 11, 5),
  (12, "Назад", 2000, 11, 5),
  (13, "Назад", 3000, 11, 5),
  (14, "Назад", 4000, 11, 5),

  (16, "Мир", 1000, 12, 6),
  (17, "Карта", 1000, 13, 7),
  (18, "Перемещение", 1000, 14, 8),
  (19, "Местность", 1000, 15, 9),

  (20, "Глобальная", 1000, 16, 7),
  (21, "Местности", 1000, 16, 7),
  (22, "Координаты", 1000, 17, 0),

  (23, "Персонаж", 3000, 18, 10),
  (24, "Характеристика", 3000, 19, 11),
  (25, "Статистика", 3000, 20, 11),
  (26, "Биография", 3000, 21, 12),
  (27, "Записная книжка", 3000, 22, 14),
  (28, "Изменить био", 3000, 23, 13),
  
  (29, "Добавить запись", 3000, 24, 13),
  (30, "Удалить запись", 3000, 25, 13),
  (31, "Взять задание", 1000, -1, 13),

  (32, "Задания", 2000, 26, 15),
  (33, "Начать задание", 2000, 27, 13),
  (34, "Отказаться от задания", 2000, 27, 13),
  (35, "Статистика заданий", 2000, -1, 0),
  (36, "Ежедневки", 2000, 28, 0);