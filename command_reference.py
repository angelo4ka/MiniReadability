# Список команд
commands_list = {
    "HELP": "команда",
    "BEGIN": "команда",
    "EXIT": "команда",
    "": "вспомогательный элемент"
}

# Справочник всех команд
def CommandReference():
    print("Команды:")
    print("---")
    print("BEGIN - формирует текстовый документ с полезной информацией из веб-страницы")
    print("HELP - выводит справочную информацию о командах утлиты")
    print("EXIT - выходит из утилиты")
    print()

# Помощь по формированию текстового документа с полезной информацией из веб-страницы 
def CR_Begin():
    print("Формирует текстовый документ с полезной информацией из веб-страницы:")
    print("|  BEGIN [<url>]")
    print("|  <url> - ссылка на веб-страницу")
    print()

# Помощь по команде
def CR_Help():
    print("Вывод справочных сведений о командах утилиты:")
    print("|  HELP [<команда>]")
    print("|  <команда> - команда, интересующая пользователя")
    print()

# Помощь по выходу из утилиты
def CR_Exit():
    print("Вывод из утилиты:")
    print("|  EXIT")
    print()

# Неизвестная команда 
def CR_UnknownCommand(command):
    print("\"{command}\" не является внутренней или внешней командой утилиты.".format(command = command))
    print("Воспользуйтесь командой HELP для просмотра всех команд.")
    print()

# Проверка наличия команды в списке команд
def IsUnknownCommand(command):
    if command in commands_list:
        return True
    else:
        return False

# Глобальная помощь по командам
def CR_GeneralHelp(command=""):
    # Информация о всех командах
    if command == "":
        print("Для получения сведений об определённой команде наберите HELP <имя команды>")
        print("---")
        CommandReference()
        
    # Информация по отдельной команде
    if command == "HELP":
        CR_Help()
    if command == "BEGIN":
        CR_Begin()
    if command == "EXIT":
        CR_Exit()
        
    # Ошибка ввода команды
    if not IsUnknownCommand(command):
        command = "HELP " + command
        CR_UnknownCommand(command)

    print()