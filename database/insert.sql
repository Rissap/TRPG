INSERT INTO `race` VALUES
(1, 'Аласи'),
(2, 'Элементали'),
(3, 'Артифексы'),
(4, 'Перевёртыши'),
(5, 'Хвостатые');

INSERT INTO `keyboard` VALUES
(0, '{"one_time":false, "buttons":[]}');

INSERT INTO `script` VALUES
(0, 'Не понял тебя. Скажи иначе.'),
(1, 'Свежая кровь желает стать частью чего-то большего? Похвально. \nПриветствую тебя в мире Раумор!'),
(2, "Мир Раумор - огромный континент среди множества островов. Тут ни дня не проходит без битв, приключений и мирных соглашений. Ремесло и торговля буйно процветают в городах, а пустые чащи лесов ожидают заблудших путников для обеда."),
(3, "На твой выбор предоставляются четыре разумные расы:\nАласи, Артифексы, Перевёртыши, Элементали\n"),
(4, "Я - Лис. Хвостатый демон, что владеет всей информацией. Обожаю приключения, квесты, и маленьких милых лисят."),
(5, "Мы, создатели мира Раумор, желаем вам приятно провести время в текстовой ролевой игре. Делайте то, что пожелаете - никаких рамок или ограничений!"),

(10, "Приветствую в Рауморе - мире, полном беззакония и возможностей! Назови своё имя:"),
(11, "Ты свирепый воин, или железная воительница?"),
(12, "Из какой ты расы?"),
(13, "Сколько тебе лет (10~90)?"),
(14, "Расскажи мне о себе. Или отправь точку, если желаешь скрыть своё прошлое:"),
(15, "Итак, вот что ты создал:\n"),
(16, "Желаешь быть идеальным существом? Имеешь право. А теперь, вновь назови мне имя:"),
(17, "Отлично! Добро пожаловать в мир Хаоса. "),

(90, "И вот ты вновь у самого начала."),
(99, "Назад так назад"),

(300, "Вперёд, на поиски приключений!"),
(301, "Вот список твоих текущих квестов:"),
(302, "Подбираем список всех доступных заданий... Оно тебе надо?"),
(303, "Ученье - свет, а неученье - чуть свет и на работу."),
(304, "Работай на галере, или в универе!");

/* id key keyboard script action */
INSERT INTO `keyword` VALUES
(0, "False", 0, 0, 0),
(1, "True", 0, 0, 100000),

(2, "Начать!", 0, 1, 1),
(3, "Что это за место?", 0, 2, 1),
(4, "Кем я могу стать?", 0, 3, 1),
(5, "Кто ты?", 0, 4, 1),
(6, "О ролевой", 0, 5, 1),

(7, "Начать приключение!", 0, 10, 10),
(8, "gender", 0, 11, 11),
(9, "race", 0, 12, 12),
(10, "age", 0, 13, 13),
(11, "bio", 0, 14, 14),
(12, "confirm", 0, 15, 15),
(13, "Нет, пересоздать персонажа!", 0, 16, 10),
(14, "Да, всё верно!", 0, 17, 90000),

(15, "menu", 0, 90, 90000),
(16, "Назад", 0, 99, 90000),



(300, "Задания", 0, 300, 300000),
	(301, "Текущие задания", 0, 301, 30000),
	(302, "Ежедневные задания", 0, 302, 300000),
	(303, "Особые задания", 0, 303, 300000),
	(304, "Учёба", 0, 304, 300000);

/*
delete from keyboard;
delete from script;
delete from keyword;
*/

/*
INSERT INTO `race` VALUES
(1, 'Аласи'),
(2, 'Элементали'),
(3, 'Артифексы'),
(4, 'Перевёртыши'),
(5, 'Хвостатые');

INSERT INTO `script` VALUES
(0, 'А, это ты. Ну что ж, садись, раз пришѐл... Хорошо, что ты нашѐл меня, а не моего старого знакомого, Фринса. Он вообще мог отправить твою душеньку в тело какого-то Трумбо. И бродил бы ты по острову в гордом животном одиночестве.Ладно, не суть. Попытаюсь тебе объяснить ситуацию. Твоя душа сейчас находится в состоянии суперпозиции. И пока что только я могу еѐ видеть, вот так! Но я предлагаю тебе сделку. Стать частью интересного мира в образе разумного существа, которое имеет возможность стать героем, великим волшебником, политиком, а может быть даже самим полубогом. Всѐ зависит от удачи этого существа. Ну и от силы твоей души, конечно же. Я могу это сделать, но в обмен ты соглашаешься, что я буду владеть всей информацией о твоих передвижениях по Раумору, твоѐм прогрессе и умениях. Конечно, я буду помогать тебе с этой информацией, выдавая еѐ тебе при первой твоѐм желании, с помощью моей телепатии. Ты можешь меня спросить то, что тебе интересно, а можешь сразу ринуться подыскивать себе тело!'),
(1, 'Ты, юная душа, в мире Создателя Хаоса, Рауморе. Его населяет 4 основных разумных расы – порождений своих Богов и Богинь, детей Хаоса.  После многих событий, о которых тебе удастся узнать в своѐм приключении, ситуация в мире сложилась таким образом:\n\nСуществуют четыре основных материка рас, их «Родина». С их законами, культурой и верованием. Ты, вселившись в одного из этих разумных существ, начнѐшь свой путь именно с одного из этих материков. Так же, при поддержке Богини Виты, создательницы расы Аласи, был создан один общий континент, в самом центре Планеты. Именно там находятся нейтральные законы для всех рас, мировое правительство, храм Хаоса, а также вершина мирового прогресса, бриллиант новейшего времени, Институт Хаоса, в простонародье имеющий название «Пансионат».'),
(2, 'Я - Лис. Одинокий странник, желающий найти себе красивого лисёнка для совместных скитаний.'),
(3, 'На твой выбор, юная душа, представляется 4 разумных расы: Аласи, Артифексы, Перевѐртыши и Элементали. Ты можешь стать представителем одной из этих рас, юным (или не очень) существом, которое начнѐт свой путь к славе в опасном мире Раумор. Выбрав одну из рас, ты сам начинаешь писать своѐ приключение. Хочешь быть мореплавателем? Пожалуйста! Или же заняться добычей полезных руд в шахте возле вулкана? Без проблем! Выбор лишь за тобой. Я тебе немного расскажу о доступных расах, прежде чем ты сделаешь свой выбор: \n\nЭлементали – cкрытые, тѐмные, высокие и худощавые. Истинные тѐмные маги, которым доступна самая неизведанная – магия сна. Их продолжительность жизни до сих пор не определена, но, поговаривают, они могут жить и до тысячи лет. Их самый главный недостаток – они не могут находиться в этом мире больше восьми часов. Им необходимо, хотя бы раз в 8 часов, спускаться в своѐ измерение. Такое проклятие им выдал Создатель Хаос, за совершенное преступление их Бога – старшего сына Хаоса, Гипа.  Они физически слабы, мало защищены от ближнего боя, но с их умением магической атаки не сравнится никто. \n\nАласи – Порождения самой старшей дочери Хаоса, Богини Виты. В какой-то степени, священные существа с хрупким телом и крыльями. Обладают способностью летать, отчего развивают самую большую скорость из всех рас, что и является их главным преимуществом. Так же, как и Элементали, слабы физически, но хорошие маги, в чѐм могут сравниться по силе с Элементалями. Их Магия жизни является больше оборонительной магией,  чем атакующей. Зачастую Аласи –превосходные политические деятели, врачи, профессора, священнослужители.  По благословению Виты Хаосом стали обладать фактическим бессмертием. Они не стареют, но случайный зачарованный кинжал вполне может их убить. Именно из-за этого Аласи зачастую ведутоседлый образ жизни, занимая государственные должности, и редко являются искателями приключений. \n\nАртифекcы - Остроухие, высокие, мускулистые полу-машины с бледной кожей, похожие на обитателей подземных миров. Эта раса, созданная младшей дочерью Хаоса, Богиней Алимерой, является самой технологически развитой на Планете. Они слабее всех подвержены магии, они медлительны, но при этом могут поднимать большие грузы, и их главный козырь, помимо интеллекта – физическая сила и выносливость. Их магия Машин служит, скорее, для разработки, модернизации и зачарования их всевозможных аппаратов и орудий, нежели для магических дуэлей. Прекрасные существа для любителей кузнечного дела, большой грузоподъѐмности, а так же решения дел физической силой.\n\nПеревёртыши – Звероподобные существа, обладающие разумом, даннымим средним сыном Хаоса – Ханделем. Разные виды этих существ, будь то ящеры, волки, имеют свой вид морды/лица, схожий с животными. Рост в больших случаях варьируется от 1.4 до 1.8 метра.Перевѐртыши тесно связаны с животным миром, и связь эта проявляется во внешнем виде, их поведении, религии и магии. Им лучше всего подходит магия элементов, так как они максимально гармоничны с собой и окружающим миром. Из-за их приближѐнности к природе, являются самой сбалансированной расой, от чего берутся почти любую работу в мире Раумор.\n\nТак же, я не мог не упомянуть свою расу, Хвостатых! О ней ты сможешь узнать поподробнее только тогда, когда их встретишь. Мы, лисы, скрытая раса, но кое-что о нас всем известно. При определѐнных обстоятельствах, которые ты сможешь узнать из древних легенд, мы отошли от основной расы Перевѐртышей, основав свою маленькую «колонию» где-то на Планете. Тебе я не расскажу наше месторасположение, а то сможешь нас выдать, хе-хе. Мы быстры, а о нашем навыке владения мечом слагают истории. Из нас получились бы прекрасные наѐмники! Но, у нас есть недостаток. Из-за потери связи со своим Божеством напрямую, мы не имеем никакой магии, кроме нашей собственной. Пожалуй, это всѐ, что тебе надо знать о разумных существах мира Раумор.'),
(4, 'Мы, создатели ролевого мира Раумор, надеемся, что Вы получите удовольствие от игрового процесса, общения в приятной компании, а так же массы познавательных вещей! В нашей ролевой Вы вольны делать то, что угодно. Наша главная цель – создание максимально открытых для действий условий, в рамках ВКонтакте. Ролевая совмещает в себе аспекты ММОРПГ, стратегии, а так же настольно-ролевой и ролевой игры. В ней Вы действительно можете развивать политику, торговлю, науку. Создавать новые рабочие заклинания, или же открыть свою кузницу и ковать мечи. А может, Вы хотите отправиться на исследование опасных участков мира, одолев мощных монстров? Всѐ это Вы сможете сделать в нашей ролевой! Контакты для связи:\nОснователь: https://vk.com/id92926273\nТехнический директор: https://vk.com/rinsap\nТворческий центр: https://vk.com/id484822996 '),
(5, 'Душа, в материальном мире у каждого существа есть своѐ название, своѐ слово, на которое он отзывается. Как ты хочешь, чтоб тебя называли? Укажи своё полное имя-фамилию:'),
(6, 'Отлично, приятно познакомиться! Ты всѐ ближе на пути к материализации. Из какой расы твоѐ существо? Ты можешь выбрать между:\n1. Аласи\n2. Элементали\n 3. Артифексы\n4. Перевѐртыши'),
(7, 'Ты уже определился с именем и расой собственного материального я. Похвально. Теперь скажи, сколько тебе планетарных лет? (От 10 до 90)'),
(8, 'Материальность всѐ ближе. Мир уже готов принять тебя, но для его обитателей нужна твоя история. Придумай, кем ты был до настоящего времени. Это запишется в скрижали, как твоя биография. Ты можешь сделать это потом, просто отправив мне точку (лимит в 4000 знаков).'),
(9, 'А сейчас ты можешь рассказать о своих планах на будущее. Кем ты хочешь стать в Рауморе? Искателем приключений, или же торговцем вольных городов? Расскажи это тут, и я буду помогать тебе осуществлять твои цели! Ты можешь сделать это потом, просто отправив мне точку (лимит в 4000 знаков).'),
(10, 'Поздравляю! Ты обрѐл материальность, (*@*). И в данный момент начинается твой путь героя. Помни, что я лишь обычный лис, и рассказывать обо мне всем вокруг не стоит.Ты всегда сможешь со мной связаться, просто подумав обо мне. Вся информация о тебе будет храниться на моих записях. \nКраткое руководство по ролевой, боту, да и просто полезная информация:\n \nЕсли что-то осталось непонятно, напиши создателю: \nhttps://vk.com/id92926273\n или техподдержке: \nhttps://vk.com/rinsap\nОни обязательно помогут.'),

(12, 'Приветствую тебя, мой юный друг.'),
(13, 'Исследуй то, что может убить тебя.'),
(14, 'Вперёд, навстречу приключениям!'),
(15, 'Изволите запечатлить вашу летопись в истории на века? Извольте отправить ей сюда.'),
(16, 'Информация о ролевой, нашем общении и прочие типичные вопросы:\nhttps://vk.com/topic-177941291_39342203'),
(17, 'Ошибки, нетипичное поведение или я жалобы:\nhttps://vk.com/topic-177941291_39342561'),

(18, 'Ну что же ты, душа, всѐ определиться не можешь. Так уж и быть, выбери себе новое существо.'),
(19, ''),
(20, 'Назад так назад'),
(50000, 'Заглушка'),
(21, 'Все твои звеняшки, блестяшки, дорогушки - что душу греют в зимний день.');

INSERT INTO `keyboard` VALUES
(0, '{"one_time":false, "buttons":[]}'),
(1, '{"one_time":false, "buttons":[]}'),
(2, '{"one_time":false, "buttons":[]}'),
(3, '{"one_time":false, "buttons":[]}'),
(4, '{"one_time":false, "buttons":[]}'),
(5, '{"one_time":false, "buttons":[]}'),
(6, '{"one_time":false, "buttons":[]}'),
(7, '{"one_time":false, "buttons":[]}'),
(8, '{"one_time":false, "buttons":[]}'),
(9, '{"one_time":false, "buttons":[]}'),
(10, '{"one_time":false, "buttons":[]}'),
(11, '{"one_time":false, "buttons":[]}'),
(12, '{"one_time":false, "buttons":[]}'),
(13, '{"one_time":false, "buttons":[]}'),
(14, '{"one_time":false, "buttons":[]}'),
(15, '{"one_time":false, "buttons":[]}');

(1, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Где я?"
				},
				"color":"positive"
			},
			{
			"action":{
				"type":"text",
				"label":"Кем я могу стать?"
				},
				"color":"positive"
			}
			],
			[
				{
			"action": {
				"type":"text",
				"label":"Начать приключение!"
				},
				"color":"positive"
				}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Кто ты?"
				},
				"color":"positive"
			},
			{
			"action":{
				"type":"text",
				"label":"О Ролевой"
				},
				"color":"positive"
			}
			]
		]
	}'),
(2, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Аласи"
				},
				"color":"default"
			},
			{
			"action":{
				"type":"text",
				"label":"Артифексы"
				},
				"color":"default"
			}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Перевёртыши"
				},
				"color":"default"
			},
			{
			"action":{
				"type":"text",
				"label":"Элементали"
				},
				"color":"default"
			}
			]
		]
	}'),
(3, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Персонаж"
				},
				"color":"positive"
			}],
			[
				{
			"action": {
				"type":"text",
				"label":"Мир"
				},
				"color":"default"
				}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Задания"
				},
				"color":"positive"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Тексты"
				},
				"color":"default"
			}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Инфо"
				},
				"color":"default"
			},
			{
			"action":{
				"type":"text",
				"label":"Ошибки"
				},
				"color":"negative"
			}
			]
		]
	}'),
(4, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Да, всё верно!"
				},
				"color":"positive"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Нет, давайте заново!"
				},
				"color":"negative"
			}]]}'),
(5, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Характеристики"
				},
				"color":"positive"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Статистика"
				},
				"color":"positive"
				}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Инвентарь"
				},
				"color":"positive"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Возможности"
				},
				"color":"default"
			}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Назад"
				},
				"color":"default"
			},
			{
			"action":{
				"type":"text",
				"label":"-/-"
				},
				"color":"default"
			}
			]
		]
	}'),
(6, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Учёба"
				},
				"color":"positive"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Доступные задания"
				},
				"color":"positive"
				}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Ежедневные задания"
				},
				"color":"default"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Особые задания
				},
				"color":"default"
			}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Назад"
				},
				"color":"default"
			}]
		]
	}'),
(7, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Полный инвентарь"
				},
				"color":"positive"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Активные предметы"
				},
				"color":"default"
				}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Экипировка"
				},
				"color":"default"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Обмен/продажа предметов"
				},
				"color":"default"
			}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Назад"
				},
				"color":"default"
			},
			{
			"action":{
				"type":"text",
				"label":"-/-"
				},
				"color":"default"
			}
			]
		]
	}'),
(8, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Описание местности"
				},
				"color":"default"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Карта"
				},
				"color":"default"
				}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Населённый пункт"
				},
				"color":"default"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Добыча"
				},
				"color":"positive"
			}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Назад"
				},
				"color":"default"
			},
			{
			"action":{
				"type":"text",
				"label":"-/-"
				},
				"color":"default"
			}
			]
		]
	}'),
(9, '{
		"one_time": false,
		"buttons":[
			[
			{
			"action": {
				"type":"text",
				"label":"Оружие"
				},
				"color":"default"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Кирка"
				},
				"color":"default"
				}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Топор"
				},
				"color":"default"
			}],
			[
			{
			"action": {
				"type":"text",
				"label":"Ножницы"
				},
				"color":"default"
			}
			],
			[
			{
			"action": {
				"type":"text",
				"label":"Назад"
				},
				"color":"default"
			},
			{
			"action":{
				"type":"text",
				"label":"-/-"
				},
				"color":"default"
			}
			]
		]
	}');


INSERT INTO `keyword` VALUES
(0, 'Начать!', 1, 0, 0),
(1, 'Где я?', 1, 1, 0),
(2, 'Кто ты?', 1, 2, 0),
(3, 'Кем я могу стать?', 1, 3, 0),
(4, 'О Ролевой', 1, 4, 0),
(5, 'Начать приключение!', 0, 5, 1),
(6, 'race', 2, 6, 2),
(7, 'age', 0, 7, 3),
(8, 'biography', 0, 8, 4),
(9, 'additional', 0, 9, 5),
(10, 'prove', 4, 19, 6),
(11, 'registered', 3, 10, 1000000),

(12, 'Персонаж', 5, 12, 2000000),

(13, 'Мир', 8, 13, 3000000),

(14, 'Задания', 6, 14, 4000000),

(24, 'Учёба', 6, 50000, 4100000),
(25, 'Доступные задания', 6, 50000, 4200000),
(26, 'Ежедневные задания', 6, 50000, 4300000),
(27, 'Особые задания', 6, 50000, 4400000),

(40, 'Сдать предмет', 1, 19, 4110000),
(41, 'Отработка', 1, 19, 4120000),
(42, 'Учебные заведения', 1, 19, 4130000),
(43, 'Успеваемость', 1, 19, 4140000),
(44, 'Связь с преподавателем', 1, 19, 4150000),




(15, 'Тексты', 3, 15, 5000000),
(16, 'Инфо', 3, 16, 6000000),
(17, 'Ошибки', 3, 17, 7000000),
(18, 're-register', 0, 18, 1),

(19, 'Назад', 3, 20, 9999),

(20, 'Характеристики', 5, 19, 11001),
(21, 'Статистика', 5, 50000, 11002),
(22, 'Инвентарь', 7, 21, 11003),
(23, 'Возможности', 5, 50000, 11004),

(28, 'Полный инвентарь', 7, 50000, 11101),
(29, 'Активные предметы', 7, 50000, 11102),
(30, 'Экипировка', 7, 50000, 11103),
(31, 'Обмен/продажа', 7, 50000, 11104),

(32, 'Описание местности', 8, 50000, 12001),
(33, 'Карта', 8, 50000, 12002),
(34, 'Населённый пункт', 8, 50000, 12003),
(35, 'Добыча', 9, 50000, 12004),

(36, 'Оружие', 9, 50000, 12401),
(37, 'Кирка', 9, 50000, 12401),
(38, 'Топор', 9, 50000, 12401),
(39, 'Ножницы', 9, 50000, 12401);


INSERT INTO stats VALUES
(1, 'health', 'Здоровье'),
(2, 'mana', 'Мана'),
(3, 'damage', 'Физический урон'),
(4, 'protect', 'Защита'),
(5, 'weight', 'Переносимый вес'),
(6, 'm_attack', 'Магическая атака (%)'),
(7, 'm_resist', 'Магическая защита (%)'),
(8, 'speed', 'Скорость'),
(9, 'gold', 'Золото'),
(10, 'glory', 'Слава'),
(11, 'quests', 'Выполнено квестов'),
(12, 'x', 'Координата горизонтали'),
(13, 'y', 'Координата вертикали');

INSERT INTO raceStats VALUES
(1, 1, 50),
(1, 2, 150),
(1, 3, 1),
(1, 4, 1),
(1, 5, 30),
(1, 6, 30),
(1, 7, 40),
(1, 8, 3),
(1, 9, 100),
(1, 10, 0),
(1, 11, 0),
(1, 12, 1200),
(1, 13, 1200),

(2, 1, 50),
(2, 2, 150),
(2, 3, 1),
(2, 4, 1),
(2, 5, 30),
(2, 6, 40),
(2, 7, 40),
(2, 8, 5),
(2, 9, 100),
(2, 10, 0),
(2, 11, 0),
(2, 12, 1200),
(2, 13, 1200),

(3, 1, 150),
(3, 2, 50),
(3, 3, 5),
(3, 4, 5),
(3, 5, 60),
(3, 6, 40),
(3, 7, 40),
(3, 8, 5),
(3, 9, 100),
(3, 10, 0),
(3, 11, 0),
(3, 12, 1200),
(3, 13, 1200),

(4, 1, 100),
(4, 2, 100),
(4, 3, 3),
(4, 4, 3),
(4, 5, 40),
(4, 6, 20),
(4, 7, 20),
(4, 8, 6),
(4, 9, 100),
(4, 10, 0),
(4, 11, 0),
(4, 12, 1200),
(4, 13, 1200),

(5, 1, 200),
(5, 2, 20),
(5, 3, 10),
(5, 4, 5),
(5, 5, 50),
(5, 6, 5),
(5, 7, 5),
(5, 8, 2),
(5, 9, 100),
(5, 10, 0),
(5, 11, 0),
(5, 12, 1200),
(5, 13, 1200);

INSERT INTO playerQuest VALUES
(219124437, 1, 1, 0);

INSERT INTO item VALUES
(1, 'Рисунок отпечатка лапы', 'quest', 1),
(2, 'Рисунок отпечатка сапога', 'quest', 1),
(3, 'Клочок рыжей шерсти', 'quest', 1);

INSERT INTO enchant VALUES
(0, "", '', 1);

INSERT INTO playerItem VALUES
(219124437, 1, 0, 1),
(219124437, 2, 0, 1),
(219124437, 3, 0, 1);

INSERT INTO quest VALUES (1, 'Неведомый зверь', 'Эта история случилась очень давно. Молодой воин, охраняющий деревню, был жестоко разорван неизвестным зверем. Деревня нуждается в помощи сильных мира сего. Вам предстоит узнать, что за существо послужило причиной сметри и не притаилось ли оно поблизости.', '');

 
delete from player;
delete from allowPlayer;
delete from playerStats;
delete from playerQuest;
delete from playerItem;

*/