import json

def save_notes(notes, file_path):

    with open(file_path, 'w') as file:

        json.dump(notes, file, indent=4)



import json

def load_notes(file_path):

    with open(file_path, 'r') as file:

        notes = json.load(file)

    return notes
    

def add_note(notes, new_note):

    # Получаем максимальный идентификатор из существующих заметок

    max_id = max(note['id'] for note in notes) if notes else 0

    new_note['id'] = max_id + 1

    notes.append(new_note)


def edit_note(notes, note_id, new_title=None, new_body=None, new_datetime=None):

    for note in notes:

        if note['id'] == note_id:

            if new_title:

                note['title'] = new_title

            if new_body:

                note['body'] = new_body

            if new_datetime:

                note['datetime'] = new_datetime

            break
    
def delete_note(notes, note_id):

    notes[:] = [note for note in notes if note['id'] != note_id]

    
def main():

    import json

    file_path = 'notes.json'  # Путь к файлу заметок

    notes = load_notes(file_path)  # Загружаем заметки из файла



    while True:

        print('1. Вывести все заметки')

        print('2. Добавить заметку')

        print('3. Редактировать заметку')

        print('4. Удалить заметку')

        print('5. Выйти')



        choice = input('Выберите действие: ')



        if choice == '1':

            print('Заметки:')

            for note in notes:

                print(f"ID: {note['id']}")

                print(f"Заголовок: {note['title']}")

                print(f"Текст: {note['body']}")

                print(f"Дата/время: {note['datetime']}")

                print()

        elif choice == '2':

            title = input('Введите заголовок заметки: ')

            body = input('Введите текст заметки: ')

            datetime = input('Введите дату/время заметки (в формате "гггг-мм-дд чч:мм:сс"): ')



            new_note = {

                'title': title,

                'body': body,

                'datetime': datetime

            }

            add_note(notes, new_note)

            save_notes(notes, file_path)

        elif choice == '3':

            note_id = int(input('Введите ID заметки для редактирования: '))

            new_title = input('Введите новый заголовок заметки (или оставьте пустым): ')

            new_body = input('Введите новый текст заметки (или оставьте пустым): ')

            new_datetime = input('Введите новую дату/время заметки (или оставьте пустым): ')



            edit_note(notes, note_id, new_title, new_body, new_datetime)

            save_notes(notes, file_path)

        elif choice == '4':

            note_id = int(input('Введите ID заметки для удаления: '))



            delete_note(notes, note_id)

            save_notes(notes, file_path)

        elif choice == '5':

            break

        else:

            print('Неверный выбор. Попробуйте еще раз.')



if __name__ == '__main__':

    main()