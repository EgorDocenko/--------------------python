from datetime import datetime
from math import log2
from random import randint
from attesation_func import (
    authorization,
    infa,
    meny,
    additional_printing
)


'''Инициализация.'''
CLASSIC_MODE: int = 1
CREATIVE_MODE: int = 2
MULTIPLAYER_MODE: int = 3
EXIT_MODE: int = 4
ODIN: int = 1
DWA: int = 2
TRI: int = 3
THITERI = 4
PETI = 5
EMPTY: int = 0
SIX: int = 6
STO: int = 100
THE_BEGINNING_OF_THE_EVENING: int = 18
THE_BEGINNING_OF_THE_DAY: int = 12
EARLY_MORNING: int = 6
THE_END_OF_THE_NIGHT: int = 24
FIRST_SELECTION_CONDITION: int = 1
SECOND_SELECTION_CONDITION: int = 2
THIRD_SELECT_CONDITION: int = 3
FOURTH_SELECT_CONDITION: int = 4
FIFTH_THE_SELECTION_CONDITION: int = 5
SHESDISET: int = 60
EMPTY_STR: str = ''

time_start: datetime = datetime.now()


request: str = EMPTY_STR
extra_request: str = EMPTY_STR
request: str = EMPTY_STR
game_mode_request: str = EMPTY_STR

number_computer_min: int = 1
number_computer_max: int = 40
attempts_max: int = 80
how_much_less: int = EMPTY
how_much_less_min: int = 20
how_much_less_max: int = 40
game_mode: int = EMPTY
v: int = EMPTY
lvl_now: int = EMPTY
lvl_max: int = 4

user_name_eneme: str = "Компьютер"


'''Блок приветсвия.'''

print(
    f'{time_start.day}.{time_start.month}.{time_start.year} '
    'Программа запущена успешно.'
    '\n\n'
)

START_NIGNT: int = EMPTY
if START_NIGNT <= time_start.hour <= EARLY_MORNING:
    print('Добрый ночи,дорогой пользователь!')
elif EARLY_MORNING <= time_start.hour <= EARLY_MORNING:
    print('Добрый утро,дорогой пользователь!')
elif EARLY_MORNING <= time_start.hour <= THE_BEGINNING_OF_THE_EVENING:
    print('Добрый день,дорогой пользователь!')
elif THE_BEGINNING_OF_THE_EVENING <= time_start.hour <= THE_END_OF_THE_NIGHT:
    print('Добрый вечер,дорогой пользователь!')

print()
user_name: str = authorization()
print(f'{user_name}, рады приветствовать вас в игре "Угадайка"!')
meny()

while (
      not game_mode_request.isdigit() or not
      EMPTY < int(game_mode_request) < PETI
):
    game_mode_request = input(
        "Введи номер режима (числа от "
        f"{CLASSIC_MODE} до {EXIT_MODE}):\n"
    )
game_mode = int(game_mode_request)
if game_mode == CLASSIC_MODE:
    print(
        f"Вам предстоит пройти {lvl_max} уровет,"
        "каждый новый - сложнее предыдущего"
    )
elif game_mode == CREATIVE_MODE:
    settings_request = ''
    process_menu_settings = True
    while process_menu_settings:

        print('Вы выбрали режим криотив, в нем можите создать свои правила')
        print()
        print("Выберите, что вы хотите изменить в игре:")
        print(
            f"\t{FIRST_SELECTION_CONDITION}) "
            "Максимальное количество уровней"
        )
        print(f"\t{SECOND_SELECTION_CONDITION}) Начальное каличество попыток")
        print(
            f"\t{THIRD_SELECT_CONDITION}) Уменьшить кольчество попыток"
            " при переходе на новый уровень"
        )
        print(
           f"\t{FOURTH_SELECT_CONDITION}) Увеличение"
           "загадаваемой области чисел при перезоде на новый уровень"
        )
        print(
            f"\t{FIFTH_THE_SELECTION_CONDITION}) "
            "Сохранить ищменения и продолжить"
            )
        print()

        while (
            not settings_request.isdigit()
            or not EMPTY < int(settings_request) < SIX
        ):

            settings_request = input(
                                    "Выбирете пункт меню (цифор "
                                    f"от {ODIN} до {PETI})\n"
                                )
        settings_menu_item = int(settings_request)

        if settings_menu_item == ODIN:
            request_lvl_max: str = ''
            while (
                not request_lvl_max.isdigit()
                or not int(request_lvl_max) > EMPTY
            ):
                request_lvl_max = input("Введи корректное число уровней:\n")
            lvl_max = int(request_lvl_max)
            print(f"Теперь в игре будет {lvl_max} уровней")

        elif settings_menu_item == DWA:

            attempts_max: int
            popitke_request: str = ''
            while (
                not popitke_request.isdigit()
                or not int(popitke_request) > EMPTY
            ):
                popitke_request = input("Введи корректное число попыток:\n")

            attempts_max = int(popitke_request)
            print(f"Теперь в игре будет {attempts_max} попыток")

        elif settings_menu_item == TRI:

            reducing_attempts = ''
            while (
                not reducing_attempts.isdigit() or not
                int(reducing_attempts) > EMPTY
            ):
                reducing_attempts = input("Введи корректное число попыток:\n")

            DWA = int(reducing_attempts)
            print(f"Теперь в игре будет {DWA} попыток")

        elif settings_menu_item == THITERI:

            Increasing_the_desired_area: str = ''
            while (
                not Increasing_the_desired_area.isdigit()
                or not int(Increasing_the_desired_area) > EMPTY
            ):
                Increasing_the_desired_area = input(
                    "Введи увиличение разброса чисел:\n"
                )

            TRI = int(Increasing_the_desired_area)
            print(
                f"Теперь в игре будет {TRI}"
                "области чисел при перезоде на новый уровень"
            )

        elif settings_menu_item == PETI:
            print("Ваши изменение сохронены")

            process_menu_settings = False

        settings_request: str = ''
elif game_mode == MULTIPLAYER_MODE:
    print(
        'Вы выбрали режим с другом, '
        'загадывайте друг другу числа и соревнуйтесь '
    )
    user_name_eneme: str = authorization()
    wisher_player_1: str = ''
    wisher_player_2: str = ''
    rounds_total: int = EMPTY
    while (
        not wisher_player_1.isdigit() or
        not int(wisher_player_1) > rounds_total
    ):
        wisher_player_1 = input(
            f'{user_name}, введите желаемое'
            ' число раундов игры\n'
        )
    while (
        not wisher_player_2.isdigit() or not
        int(wisher_player_2) > rounds_total
    ):
        wisher_player_2 = input(
            f'{user_name_eneme}, введите '
            'желаемое число раундов игры\n'
        )
    rounds_total = randint(int(wisher_player_1), int(wisher_player_2))
    print(f'Всего будет сыграно {rounds_total} раундов')
    EMPTY = 0
    rounds_now: int = EMPTY
    player_1_points: int = EMPTY
    player_2_points: int = EMPTY
elif game_mode == EXIT_MODE:
    print('Программа завершина успешно')
if game_mode in (CLASSIC_MODE, CREATIVE_MODE):
    infa()


'''Оснавная петля.'''

while (
    game_mode in (CLASSIC_MODE, CREATIVE_MODE)
    and lvl_now < lvl_max or game_mode == MULTIPLAYER_MODE
    and rounds_now < rounds_total * DWA
):
    if game_mode in (CLASSIC_MODE, CREATIVE_MODE):
        lvl_now += ODIN
        print(f"{lvl_now}/{lvl_max} уровень игры")
        user_name, user_name_eneme = user_name_eneme, user_name
        request_area = ''
        while not request_area.isdigit() or not int(request_area) > ODIN:
            request_area = input(
                f'{user_name_eneme}, в какой области будет'
                ' находиться загаданное число?'
            )

        number_computer_max: int = int(request_area)
        if game_mode == MULTIPLAYER_MODE:
            points: int = int(log2(number_computer_max)) + ODIN

            attempts_max: int = points + TRI

            print(
                f'{user_name_eneme} успешно задал область загоданного '
                f'числа (от {ODIN} до {number_computer_max})'
            )
            print(
                f'При условии, что {user_name} успешно угадает число за'
                f' {attempts_max} попыток, он получит {points} балов'
            )
    elif game_mode == MULTIPLAYER_MODE:

        rounds_now += ODIN
        print(
            f'{(rounds_now+ODIN)//DWA}/{rounds_total} раунд игры'
            f"Ваша цель угадать число от "
            f"{number_computer_min} до {number_computer_max}"
            f" за {attempts_max} попыток"
        )
    '''Локакальные пирименные.'''

    number_user: int = EMPTY
    attempts: int = EMPTY
    extra_request: str = ''
    game_process: bool = True

    number_computer = randint(number_computer_min, number_computer_max)
    '''Игравой блок.'''
    while game_process:

        if extra_request:

            request: str = extra_request
            extra_request: int = EMPTY
        else:

            request: str = input(
                f"Введи {additional_printing(attempts)} число от "
                f"{number_computer_min} до {number_computer_max}\n"
            )
            print()
        if isinstance(request, int) or request.isdigit():
            attempts += ODIN
            number_user = int(request)
            if number_user == number_computer:
                print(
                    f"{user_name}, превосходно! Вы угадали"
                    "число, подзравляем!"
                )
                print(f"На это Вам потребовалось всего {attempts} попыток")
                game_process = False
            elif attempts == attempts_max:
                print(f"Загаданное число было - {number_computer}")
                print(
                    'К сожаление вы не угадали и израсходовали '
                    f'все {attempts_max} попыток :('
                )

                game_process: bool = False
            elif number_user < number_computer:
                print(f"Число загаданное компьютером больше {number_user}...")
            else:
                print(f"Число загаданное компьютером меньше {number_user}...")
            if attempts == attempts_max//2 and game_process:
                print(
                    'У Вас закончилась уже половина попыток, если '
                    'пожелаете сдаться напишите: "сдаться"  или "give up"'
                )
                extra_request = input(
                    "Если хочешь продолжить игру можешь сразу "
                    "написать новое число\n"
                ).lower().strip()
                if extra_request in ("сдаться", "give up"):
                    print(
                        "Обидно, конечно, что ты уходишь, но в следующий"
                        " раз у тебя обязательно получитсья!"
                    )
                    print(f"Загаданое число было - {number_computer}")

                    game_process: bool = False
                elif extra_request.isdigit():
                    extra_request = int(extra_request)
                else:
                    extra_request: bool = ''
            v: int = int(request)
        elif request.strip().lower() in (
            "сдаюсь",
            "хватит",
            "выход",
            "помоги пожалуйста"
        ):
            request_perfect = request.strip().lower()
            if request == "сдаюсь":
                print(
                    "Обидно, конечно, что ты уходишь, но в следующий"
                    " раз у тебя обязательно получитсья!"
                )
                print(f"Загаданое число было - {number_computer}")

                game_process: bool = False
            elif request.strip().lower() in ("хватит", "выход"):
                print("Программа завершилась успешна")

                game_process: bool = False
            elif request_perfect == "помоги пожалуйста":
                print("вежливым людям мы всегда рады памоч")
                how_much_less = randint(how_much_less_min, how_much_less_max)

                if abs(number_computer-v) < PETI:
                    print("Ты совсем плизко")
                elif number_computer-how_much_less < ODIN:
                    print(
                        f"это число находиться в диапазоне от {ODIN}"
                        f" до {number_computer+how_much_less}"
                    )
                elif abs(number_computer+how_much_less) > STO:
                    print(
                        "это число находиться в диапазоне от"
                        f" {number_computer-how_much_less} до {STO}"
                    )
                else:
                    print(
                        "это число находиться в диапазоне от "
                        f"{abs(number_computer-how_much_less)} "
                        f"до {abs(number_computer+how_much_less)}"
                    )
        else:
            print(
                "Введи ЧИСЛО от "
                f"{number_computer_min} до {number_computer_max}"
            )
    if (
        game_mode in (CLASSIC_MODE, CREATIVE_MODE)
        and number_user == number_computer
    ):
        number_computer_max *= TRI
        attempts_max //= DWA
        print("\n Поздравляю вы перешли на новый уровень!\n")
    elif game_mode == MULTIPLAYER_MODE:
        if number_computer == number_user:
            print(
                f'{user_name} успешно угадал число за {attempts}'
                f' попыток и получил {points} баллов '
            )
            if rounds_now % DWA == EMPTY:
                player_1_points += points
            else:
                player_2_points += points

        else:
            print(
                f'К сожилению, {user_name} не справился  с задачей '
                f'{user_name_eneme} и не угадал число {number_computer}'
            )

        lvl_now -= ODIN

if lvl_now == lvl_max and game_mode == CLASSIC_MODE:
    print("Поздравляем вы прошли классический режим")
elif lvl_now == lvl_max and game_mode == CREATIVE_MODE:
    print("Поздравляем вы прошли креотивный режим")
elif game_mode == MULTIPLAYER_MODE:
    if player_1_points > player_2_points:
        print(f'{user_name} одержал опбеду,заработав {player_2_points} баллов')
        print(
            f"Он обогнал {user_name} на "
            f"{player_1_points - player_2_points} очков"
        )
    elif player_2_points > player_1_points:
        print(
            f'{user_name_eneme} одержал опбеду'
            f',заработав {player_1_points} баллов'
        )
        print(
            f"Он обогнал {user_name} на "
            f"{player_2_points - player_1_points} очков"
        )
    else:
        print("Ничья")
        print(f'Кадый абрал по {player_1_points} баллов')

tame_end: datetime = datetime.now()
delta: datetime = tame_end - time_start
print(
    f'Время работы приложения - '
    f'{delta.seconds//SHESDISET} : {delta.seconds % SHESDISET}.'
)
