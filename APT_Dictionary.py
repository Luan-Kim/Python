import pickle

print('아파트 브랜드 이름 열람 프로그램입니다.')


def menu():
    print('1. 정보 입력')
    print('2. 정보 삭제')
    print('3. 정보 열람')
    print('4. 프로그램 종료')
    print('메뉴를 선택해주세요')


Dict = dict()

while True:
    menu()
    sel = int(input())

    if sel == 1:
        while True:
            constructor = input('건설사 이름을 입력해주세요 : ')
            brand = input('건설사 브랜드 이름을 입력해주세요 : ')
            Dict[constructor] = brand

            with open('Dict.pkl', 'wb') as fout:
                pickle.dump(Dict, fout)

            res = input('입력을 종료하시겠습니까? (Y/N) : ')

            if res == 'Y' or res == 'y':
                break

    elif sel == 2:
        while True:
            with open('Dict.pkl', 'wb') as fout:
                pickle.dump(Dict, fout)

            del_brand = input('삭제할 건설사 이름을 입력해주세요 : ')

            if del_brand in Dict:
                del Dict[del_brand]
                print('정상적으로 삭제되었습니다.')

                res = input('계속 하시겠습니까? (Y/N) : ')

                if res == 'N' or res == 'n':
                    break

            else:
                print('등록되지 않은 건설사입니다.')
                break

    elif sel == 3:
        while True:
            with open('Dict.pkl', 'rb') as fin:
                Apt_dic = pickle.load(fin)

            find_brand = input('아파트 건설사 이름을 입력해주세요 : ')
            if find_brand in Apt_dic:
                print(f'해당 건설사의 브랜드 이름은 {Apt_dic[find_brand]}입니다.')

                res = input('조회를 종료하시겠습니까? (Y/N) : ')

                if res == 'Y' or res == 'y':
                    break

            else:
                print('등록 되어있지 않은 건설사입니다.')

                res = input('조회를 종료하시겠습니까? (Y/N) : ')

                if res == 'Y' or res == 'y':
                    break
    else:
        print('프로그램을 종료합니다.')
        break

    print('\n')
