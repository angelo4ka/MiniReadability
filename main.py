import command_reference as commands_hdbk
from download_article import Website
from converting_tags import TagConverter

if __name__ == '__main__':
    def UseCommandHelp(full_command, command):
        if len(command) == 2:
            commands_hdbk.CR_GeneralHelp(str(command[1]))
        if len(command) == 1:
            commands_hdbk.CR_GeneralHelp()
        if len(command) > 2:
            commands_hdbk.CR_UnknownCommand(str(full_command))
    
    def UseCommandBegin(full_command, command):
        if len(command) == 2:
            url = command[1]
            
            obj_website = Website(url)
            obj_website.get_content_from_url()


            ### Преобразование файла в txt (убираем теги) 
            #name_file = obj_website.file_name_generation()

            #with open(f"html_articles\{name_file}.txt", "r", encoding = "utf-8") as f:
            #    while True:
            #        line = f.readline()
            #    
            #        if not line:
            #            break
                    
                    # Выводим строку (временная проверка)
            #        line_tag_converter = TagConverter.strip_tags(line)
            #        print(TagConverter.strip_tags(str(line)))
        if len(command) == 1:
            print("Ошибка в синтаксисе команды.")
            print()
            print()
        if len(command) > 2:
            commands_hdbk.CR_UnknownCommand(str(full_command))
            print()

    def main():
        isExit = False
        print("Данная утилита формирует текстовый документ с полезной информацией из веб-страницы.")
        
        while not isExit:
            number_of_spaces = 0
            command = input("Введите команду: ")
            for symbol in command:
                if symbol == " ":
                    number_of_spaces = number_of_spaces + 1

            if command != "" and number_of_spaces != len(command):
                dop_command = command
                command = command.upper()

                full_command = command
                command = command.split()
                dop_command = dop_command.split()

                if commands_hdbk.IsUnknownCommand(str(command[0])):
                    if command[0] == "HELP":
                        UseCommandHelp(full_command, command)

                    if command[0] == "EXIT":
                        isExit = True
                        print("Выполнен выход из утилиты.")

                    if command[0] == "BEGIN":
                        UseCommandBegin(full_command, dop_command)
                else:
                    commands_hdbk.CR_UnknownCommand(str(full_command))
                    print()
            else:
                commands_hdbk.CR_CommandEntryError()
                print()

    main()