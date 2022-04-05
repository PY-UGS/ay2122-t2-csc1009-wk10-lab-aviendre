user = str.upper(input('Course Code: '))
match user:
    case 'CSC1010':
        print('Computer Networking')
    case 'CSC1009':
        print('Object Oriented Programming')
    case 'CSC1008':
        print('Data Structure and Algorithms')
    case 'CSC1007':
        print('Operating Systems')
    case 'CSC1006':
        print('Mathematics 2')
    case _:
        print('Invalid Module')