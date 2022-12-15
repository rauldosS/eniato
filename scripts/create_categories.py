expenses = [
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Casa',
        'icon': 'house',
        'color': 'blue',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Educação'
        'icon': 'book',,
        'color': 'purple',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Eletrônic
        'icon': 'display',os',
        'color': 'yellow',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Lazer',
        'icon': 'controller',
        'color': 'orange',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Outros'
        'icon': 'three-dots',,
        'color': 'grey',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Restaurante',
        'icon': 'shop',
        'color': 'light-green',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Saúde'
        'icon': 'heart-pulse',,
        'color': 'red',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Serviços
        'icon': 'file-text',',
        'color': 'green',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Superm
        'icon': 'cart2',ercado',
        'color': 'red',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Transpo
        'icon': 'truck-front',rte',
        'color': 'blue',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Vestuár
        'icon': 'person',io',
        'color': 'pink',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'expense',
        'name': 'Viagem',
        'icon': 'airplane',
        'color': 'light-blue',
        'default': True
    },
]

incomes = [
    {
        'user_id': 1,
        'category_type': 'income',
        'name': 'Investimentos',
        'icon': 'graph-up-arrow',
        'color': 'blue',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'income',
        'name': 'Outros',
        'icon': 'three-dots',
        'color': 'red',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'income',
        'name': 'Prêmios',
        'icon': 'star',
        'color': 'yellow',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'income',
        'name': 'Presente',
        'icon': 'gift',
        'color': 'purple',
        'default': True
    },
    {
        'user_id': 1,
        'category_type': 'income',
        'name': 'Salário',
        'icon': 'wallet2',
        'color': 'green',
        'default': True
    },
]

[Category.stored.create(**expense) for expense in expenses]
[Category.stored.create(**income) for income in incomes]

