import os
from random import randrange

path = os.path.dirname(__file__)


def firstname_en(sex='r'):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    files = ['male_en.txt', 'female_en.txt']
    f = open(path + '/data/' + files[sex], 'r', encoding='utf8')
    names = f.read().split('\n')
    firstName = names[randrange(len(names))]
    return firstName


def lastname_en():
    sfx1 = [
        '', '', '', '', '', '', '', '', '', '', '',
        'pour',
        'zadeh',
        'far',
        'fard',
        'an',
        'kia',
        'rad',
        'zand',
        'khah',
        'nia',
        'mehr'
    ]
    sfx2 = [
        'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i',
        'pour',
        'zadeh',
        'far',
        'fard',
        'khani',
        'vand',
        'lou',
        'nia'
    ]

    f = open(path + '/data/male_en.txt', 'r', encoding='utf8')
    names = f.read().split('\n')
    lastName = names[randrange(len(names))]
    if lastName[1:] == 'ostafa' or lastName[1:] == 'ousa' or lastName[1:] == 'ahya':
        lastName += 'vi'
    elif lastName[1:] == 'orteza':
        lastName = lastName.replace('ez', 'az') + 'vi'
    elif lastName[1:] == 'hosro':
        lastName = lastName.replace('ro', 'ravi')
    elif lastName[-1] == 'a' or lastName[-1] == 'o' or lastName[-1] == 'u':
        lastName += 'ei'
    elif lastName[-1] == 'i':
        pass
    else:
        lastName += ['i', ''][randrange(2)]
    if len(lastName) > 10 and lastName[-1] == 'i':
        lastName += ''
    elif len(lastName) > 10 and lastName[-1] != 'i':
        lastName += 'i'
    elif lastName[-1] == 'i':
        lastName += sfx1[randrange(len(sfx1))]
    else:
        lastName += sfx2[randrange(len(sfx2))]
    return lastName


def fullname_en(sex='r'):
    return firstname_en(sex) + ' ' + lastname_en()


def firstname_fa(sex='r'):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    files = ['male_fa.txt', 'female_fa.txt']
    f = open(path + '/data/' + files[sex], 'r', encoding='utf8')
    names = f.read().split('\n')
    firstName = names[randrange(len(names))]
    return firstName


def lastname_fa():
    sfx1 = [
        '', '', '', '', '', '', '', '', '', '', '',
        ' پور',
        ' زاده',
        ' فر',
        ' فرد',
        'ان',
        ' کیا',
        ' راد',
        ' زند',
        ' خواه',
        ' نیا',
        ' مهر'
    ]
    sfx2 = [
        'ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی',
        ' پور',
        ' زاده',
        ' فر',
        ' فرد',
        ' خانی',
        ' وند',
        ' لو',
        ' نیا'
    ]

    f = open(path + '/data/male_fa.txt', 'r', encoding='utf8')
    namesArray = f.read().split('\n')
    lastName = namesArray[randrange(len(namesArray))]
    if lastName == 'مرتضی' or lastName == 'مصطفی' or lastName == 'موسی':
        lastName = lastName.replace('ی', 'وی')
    elif lastName == 'یحیی':
        lastName = lastName.replace('یی', 'یوی')
    elif lastName == 'خسرو':
        pass
    elif lastName[-1] == 'ا' or lastName[-1] == 'و':
        lastName += 'ئی'
    elif lastName[-1] == 'ی':
        pass
    else:
        lastName += ['ی', ''][randrange(2)]
    if lastName[-1] == 'ی':
        lastName += sfx1[randrange(len(sfx1))]
    else:
        lastName += sfx2[randrange(len(sfx2))]
    return lastName


def fullname_fa(sex='r'):
    return firstname_fa(sex) + ' ' + lastname_fa()

print(fullname_fa('r'))
print(firstname_fa('r'))
print(lastname_fa())

