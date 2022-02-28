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
            
            print("Идёт формирование документа! Пожалуйста, подождите...")
            # Получаем текстовый html-файл
            try:
                obj_website = Website(url)
                obj_website.get_content_from_url()

                # Преобразовываем (очищаем) текстовый html-файл
                name_file = obj_website.file_name_generation()
                with open(f"html_articles\{name_file}.txt", "r", encoding = "utf-8") as f:
                    obj_tag_converter = TagConverter(f.read())
                    # Чистка от мусора
                    obj_tag_converter.tag_processing()
                    # Преобразование текста в максимально комфортный для чтения (форматирование)
                    obj_tag_converter.text_formatting()
                    # Сохраняем текст в файл
                    obj_tag_converter.save_text(url)
                
                print("Текстовый документ с полезной информацией из веб-страницы успешно сформирован!\n\n")
            except:
                print("Введён некорректный URL-сайта.\n\n")

        if len(command) == 1:
            print("Ошибка в синтаксисе команды.\n\n")
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