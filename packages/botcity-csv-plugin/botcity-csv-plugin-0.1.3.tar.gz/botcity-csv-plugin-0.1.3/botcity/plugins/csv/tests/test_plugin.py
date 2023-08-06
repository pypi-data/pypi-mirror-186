import os

from botcity.plugins.csv import BotCSVPlugin

cur_dir = os.path.abspath(os.path.dirname(__file__))

# TODO Numbers should be int sometimes, not always double. In other words, 'sample' shouldn't exist.
reference = [
    ['Name', 'Mana', 'Price', 'Mana/Price', 'Where to Buy'],
    ['Small Mana Potion', 150.0, 4.0, 37.5, 'Ginkgo'],
    ['Strong Mana Potion', 300.0, 12.0, 25.0, 'Bicheon'],
    ['Great Mana Potion', 600.0, 36.0, 16.66666667, 'Snake Pit']
]

reference_dict = [
    {
        'Name': row[0],
        'Mana': row[1],
        'Price': row[2],
        'Mana/Price': row[3],
        'Where to Buy': row[4]
    }
    for row in reference[1:]
]

sample = [
    ['Name', 'Mana', 'Price', 'Mana/Price', 'Where to Buy'],
    ['Small Mana Potion', 150, 4, 37.5, 'Ginkgo'],
    ['Strong Mana Potion', 300, 12, 25, 'Bicheon'],
    ['Great Mana Potion', 600, 36, 16.66666667, 'Snake Pit']
]

sorted1 = [
    ['Great Mana Potion', 300, 36, 16.66666667, 'Snake Pit'],
    ['Strong Mana Potion', 300, 12, 25, 'Bicheon'],
    ['Small Mana Potion', 150, 4, 37.5, 'Ginkgo'],
]

sorted2 = [
    ['Small Mana Potion', 150, 4, 37.5, 'Ginkgo'],
    ['Strong Mana Potion', 300, 12, 25, 'Bicheon'],
    ['Great Mana Potion', 300, 36, 16.66666667, 'Snake Pit'],
]


def test_read():
    """
    Read tests.

    Performs:
        get_entry(),
        get_row(),
        get_column(),
        as_list(),
        as_dict()
    """
    bot = BotCSVPlugin().read(os.path.join(cur_dir, 'Test Read.csv'))
    assert bot.header == reference[0]
    assert bot.get_entry('Mana/Price', 1) == reference[2][3]
    assert bot.get_entry(3, 1) == reference[2][3]
    assert bot.get_row(1) == reference[2]
    assert bot.get_column('Price') == [row[2] for row in reference[1:]]
    assert bot.get_column(2) == [row[2] for row in reference[1:]]
    assert bot.as_list() == reference[1:]
    assert bot.as_dict() == reference_dict


def test_write():
    """
    Write tests.

    Performs:
        set_header(),
        get_header(),
        add_row(),
        add_rows(),
        as_list()
        write()
        read(),
        clear(),
    """
    bot = BotCSVPlugin().set_header(sample[0])
    assert bot.header == reference[0]
    assert bot.add_row(sample[1][:2]).as_list() == [reference[1][:2] + ['', '', '']]
    assert bot.add_rows([row[:2] for row in sample[2:4]]).as_list() == [
        row[:2] + ['', '', ''] for row in reference[1:]]
    assert bot.add_column(sample[0][2], [row[2] for row in sample[1:]]).as_list() \
        == [row[:3] + ['', ''] for row in reference[1:]]
    assert bot.add_columns({sample[0][col]: [row[col] for row in sample[1:]] for col in [3, 4]}).as_list() \
        == reference[1:]
    assert bot.write('Test Write.csv').read('Test Write.csv').as_list() == reference[1:]
    assert bot.clear().write('Test Write.csv').read('Test Write.csv').as_list() == []
    assert bot.header == reference[0]


def test_modify():
    """
    Modify tests.

    Performs:
        add_rows(),
        set_row(),  # TODO
        get_row(),
        set_column(),  # TODO
        get_column
        sort(),
        sort(multiple columns),
        as_list()
    """
    bot = BotCSVPlugin().set_header(sample[0])
    assert bot.set_row(0, {'Name': sample[1][0], 'Mana': sample[1][1]}).as_list() \
        == [reference[1][:2] + ['', '', '']]
    assert bot.set_row(1, sample[2][:2]).as_list() == [row[:2] + ['', '', ''] for row in reference[1:3]]
    assert bot.set_row(2, sample[3]).as_list() == [row[:2] + ['', '', '']
                                                   for row in reference[1:3]] + [reference[3]]
    assert bot.set_column('Price', [row[2] for row in sample[1:]]).as_list() \
        == [row[:3] + ['', ''] for row in reference[1:3]] + [reference[3]]
    assert bot.set_column(3, [row[3] for row in sample[1:]]).as_list() \
        == [row[:4] + [''] for row in reference[1:3]] + [reference[3]]
    assert bot.set_column(4, [row[4] for row in sample[1:]]).as_list() == reference[1:]
    assert bot.set_entry(1, 2, 999).get_entry(1, 2) == 999
    assert bot.set_entry('Mana', 2, 300).get_entry('Mana', 2) == 300
    assert bot.sort('Price', False).as_list() == sorted1
    assert bot.sort(['Mana', 'Price'], True).as_list() == sorted2


def test_destroy():
    """
    Clear and remove tests.

    Performs:
        set_range(),
        clear_range(),
        remove_row(),
        remove_rows(),
        remove_column(),
        remove_columns(),
        as_list(),
    """
    bot = BotCSVPlugin().set_header(sample[0])
    assert bot.add_rows(sample[1:]).as_list() == reference[1:]
    assert bot.remove_row(0).as_list() == reference[2:]
    assert bot.remove_rows([0, 1]).as_list() == []
    assert bot.add_rows(sample[1:]).as_list() == reference[1:]
    assert bot.remove_column('Name').as_list() == [row[1:] for row in reference[1:]]
    assert bot.remove_columns(['Mana/Price', 'Where to Buy']).as_list() == [row[1:3] for row in reference[1:]]
    assert bot.clear().as_list() == []
    assert bot.set_header(sample[0]).add_rows(sample[1:]).as_list() == reference[1:]
    assert bot.remove_column(0).as_list() == [row[1:] for row in reference[1:]]
    assert bot.remove_columns([0, 1]).as_list() == [row[3:] for row in reference[1:]]
