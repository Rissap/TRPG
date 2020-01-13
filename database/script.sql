CREATE TABLE scripts (
  id                    INTEGER NOT NULL,
  keyword               TEXT,
  point                 INTEGER,
  MESSAGE               INTEGER,
  keyboard              INTEGER,
CONSTRAINT PK_scripts PRIMARY KEY (id),
CONSTRAINT FK_REFERENCE_2 FOREIGN KEY (keyboard)  REFERENCES keyboard (ID),
CONSTRAINT FK_r FOREIGN KEY (MESSAGE)  REFERENCES message (id)
) 
;

CREATE TABLE keyboard ( 
  ID             INTEGER NOT NULL,
  data           INTEGER,
CONSTRAINT PK_keyboard PRIMARY KEY (ID)
) 
;

CREATE TABLE message ( 
  id             INTEGER NOT NULL,
  data           TEXT,
CONSTRAINT PK_message PRIMARY KEY (id)
) 
;

CREATE TABLE players ( 
  id             INTEGER NOT NULL,
  player_race    INTEGER,
  action         TEXT,
  name           TEXT,
  age            INTEGER,
  gender         TEXT,
  bio            TEXT,
  born           TEXT,
  position       TEXT,
CONSTRAINT PK_players PRIMARY KEY (id),
CONSTRAINT FK_REFERENCE_5 FOREIGN KEY (player_race)  REFERENCES player_race (id)
) 
;

CREATE TABLE quest ( 
  id             INTEGER NOT NULL,
  name           TEXT,
  description    TEXT,
  data           TEXT,
CONSTRAINT PK_quest PRIMARY KEY (id)
) 
;

CREATE TABLE player_quest ( 
  id             INTEGER NOT NULL,
  players        INTEGER,
  quest          INTEGER,
  status         TEXT,
CONSTRAINT PK_player_quest PRIMARY KEY (id),
CONSTRAINT FK_REFERENCE_4 FOREIGN KEY (players)  REFERENCES players (id),
CONSTRAINT FK_REFERENCE_3 FOREIGN KEY (quest)  REFERENCES quest (id)
) 
;

CREATE TABLE player_race ( 
  id             INTEGER NOT NULL,
  name           TEXT,
  health         INTEGER,
  mana           INTEGER,
  attack         INTEGER,
  defence        INTEGER,
  magic_attack   REAL,
  magic_defence  REAL,
  weight         INTEGER,
CONSTRAINT PK_player_race PRIMARY KEY (id)
) 
;

CREATE TABLE own ( 
  id             INTEGER NOT NULL,
  player         INTEGER,
  type           TEXT,
  name           TEXT,
  data           TEXT,
  position       TEXT,
CONSTRAINT PK_own PRIMARY KEY (id),
CONSTRAINT FK_REFERENCE_6 FOREIGN KEY (player)  REFERENCES players (id)
) 
;

CREATE TABLE dignity ( 
  id             INTEGER NOT NULL,
  player         INTEGER,
  name           TEXT,
  data           TEXT,
CONSTRAINT PK_dignity PRIMARY KEY (id),
CONSTRAINT FK_REFERENCE_7 FOREIGN KEY (player)  REFERENCES players (id)
) 
;

CREATE TABLE notes ( 
  id             INTEGER NOT NULL,
  player         INTEGER,
  data           TEXT,F
CONSTRAINT PK_notes PRIMARY KEY (id),
CONSTRAINT FK_REFERENCE_8 FOREIGN KEY (player)  REFERENCES players (id)
) 
;



delete from players;
delete from player_race;
delete from own;
delete from dignity;
delete from notes;
 
delete from keyboard;
delete from message;
delete from scripts;

INSERT INTO keyboard VALUES
  (0, ""),
  (1, "Что это за место?|Кто ты?||Начать приключение!||Краткое инфо|О ролевой"),

  (2, "Аласи|Элементали||Перевёртыши|Артифексы"),
  (3, "Господин|Госпожа"),
  (4, "Да, всё верно!|Нет, давай заново!"),

  (5, "Персонаж||Мир||Задания||Блокнот||Помощь|Ошибки"),

  (6, "Карта||Перемещение||Местность||Назад|/Ошибки/"),

  (7, "Глобальная||Местности||Назад"),
  (8, "2196|2191|2197||2190|Координаты|2192||2199|2193|2198||Назад"),
  (9, "Исследовать||Поискать задания||Добыча/сбор ресурсов||Особые действия||Назад|."),

  (10, "Характеристика||Статистика||Биография||Записная книжка||Назад|."),
  (11, "Назад|."),
  (12, "Изменить био|Назад"),
  (13, "Отмена|Назад"),
  (14, "Добавить запись||Удалить запись||Назад");

INSERT INTO message VALUES
  (0, "Мир Раумор - огромный континент среди множества островов. Тут ни дня не проходит без битв, приключений и мирных соглашений. Ремесло и торговля буйно процветают в городах, а пустые чащи лесов ожидают заблудших путников для обеда."),
  (1, "Я - Лис. Хвостатый демон, что владеет всей информацией. Обожаю приключения, квесты, и маленьких милых лисят."),
  (2, "На твой выбор предоставляются четыре разумные расы:\nАласи, Артифексы, Перевёртыши, Элементали\n"),
  (3, "Мы, создатели мира Раумор, желаем вам приятно провести время в текстовой ролевой игре. Делайте то, что пожелаете - никаких рамок или ограничений!"),

  (4, "Приветствую в Рауморе - мире, полном беззакония и возможностей! Назови своё имя:"),
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
  (25, "Введи номер заметки для удаления:");

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
  (30, "Удалить запись", 3000, 25, 13);