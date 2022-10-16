import gui
import commands

init_command = gui.chose_file_type()
if init_command == '1':
    command = gui.chose_func()
    if command == '1':
        commands.add_contact()
    if command == '2':
        commands.find_contact()
    if command == '3':
        commands.delete_contact()
    if command == '4':
        commands.show_all_contacts()
elif init_command == '2':
    command = gui.chose_func()
    if command == '1':
        commands.add_contact_json()
    if command == '2':
        commands.find_contact_json()
    if command == '3':
        commands.delete_contact_json()
    if command == '4':
        commands.show_all_contacts_json()
else:
    print('Вы ошиблись с выбором команды')


# command = gui.chose_func()
# if command == '1':
#     commands.add_contact()
# if command == '2':
#     commands.find_contact()
# if command == '3':
#     commands.delete_contact()
# if command == '4':
#     commands.show_all_contacts()

