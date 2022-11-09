locomotives_data = [
    'ТЭМ2', 'ТЭМ18', 'ТЭМ7', 'ТЭМ18м', 'ТЭМ14'
]
parts_data = [
    "Колодка тормозная гребневая",
    "Кожух редуктора",
    "Упор осевой",
    "Колесо зубчатое",
    "Колёсная пара в сборе",
    "Цилиндр в сборе",
    "Подвеска маятниковая",
    "Секция радиаторная водяная",
    "Башмак  тормозной горочный",
    "Автосцепка СА-3",
    "Воздухоочиститель",
    "Топливоподкачивающая помпа",
]
places_work_data = [
    'Ремонтная позиция 1',
    'Ремонтная позиция 2',
    'Ремонтная позиция 3',
    'Ремонтная позиция 4',
    'Ремонтная позиция 5',
    'Ремонтная позиция 6',
]
types_repair_data = [
    {
        'name': 'ТО2', 'hour': 1,
        'work': [
            "Замена тормозных колодок",
            "Осмотр трубопроводы и секции холодильников",
            "Проверка давление в масляной и топливной система",
            "Проверка сопротивление изоляции силовых и вспомогательных цепей",
            "Замена поврежденных пластин или фильтрующих элементов",
        ]
    },
    {
        'name': 'ТО3', 'hour': 12,
        'work': [
            "Проверка на стенде форсунки",
            "Проверка величины напряжения.",
            "Очистка всей аппараты от пыли и копоти",
            "Проверка состояния колесных пар",
        ]
    },
    {
        'name': 'ТР1', 'hour': 24,
        'work': [
            "Осмотр и ремонт тормозной рычажной передачи",
            "Осмотр и ремонт опор и рамы кузова",
            "Осмотр тяговых двигателей",
            "Осмотр токоприемников и электрической аппаратуры",
        ]
    },
    {
        'name': 'ТР2', 'hour': 96,
        'work': [
            "Ремонт цилиндровых крышек",
            "Ремонт шатунно-поршневой группы с разборкой",
            "Осмотр и ремонт водяного и масляного насосов",
            "Осмотр и ремонт топливной аппаратуры",
        ]
    },
    {
        'name': 'ТР3', 'hour': 114,
        'work': [
            "Восстановление",
            "Осмотр",
            "Освидетельствование и регулировку узлов и агрегатов",
        ]
    }
]
users_data = [
    (
        'Имя клиента 1', 'Фамилия клиента 1', 'customer1',
        'customer1@ru.ru', 'CUSTOMER', '11111'
    ),
    (
        'Имя клиента 2', 'Фамилия клиента 1', 'customer2',
        'customer2@ru.ru', 'CUSTOMER', '11111'
    ),
    (
        'Имя Техник', 'Фамилия Техник', 'technician',
        'technician@ru.ru', 'TECHNICIAN', '11111'
    ),
    (
        'Имя Мастер', 'Фамилия Мастер', 'master',
        'master@ru.ru', 'MASTER', '11111'
    ),
    (
        'Имя Слесарь 1', 'Фамилия Слесарь 1', 'worker1',
        'worker1@ru.ru', 'WORKER', '11111'
    ),
    (
        'Имя Слесарь 2', 'Фамилия Слесарь 2', 'worker2',
        'worker2@ru.ru', 'WORKER', '11111'
    ),
    (
        'Имя Слесарь 3', 'Фамилия Слесарь 3', 'worker3',
        'worker3@ru.ru', 'WORKER', '11111'
    ),
]