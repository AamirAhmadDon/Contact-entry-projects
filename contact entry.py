import PySimpleGUI as sg
import csv

# Setting the theme and default font with named colors
sg.theme_background_color('SaddleBrown')  # Background color for the theme
sg.theme_text_element_background_color('SaddleBrown')  # Background color for text elements
sg.set_options(font='Arial 16', text_color='DarkGoldenrod', titlebar_background_color='Firebrick')

# Creating the layout for the project
layout = [
    # Input section
    [sg.Text('Enter First Name:', text_color='DarkGoldenrod'), sg.InputText(key='-FNAME-', expand_x=True)],
    [sg.Text('Enter Last Name:', text_color='DarkGoldenrod'), sg.InputText(key='-LNAME-', expand_x=True)],
    [sg.Text('Enter Gender:', text_color='DarkGoldenrod'), sg.Combo(['Male', 'Female', 'Other'], key='-GENDER-', expand_x=True)],
    [sg.Text('Enter Age:', text_color='DarkGoldenrod'), sg.InputText(key='-AGE-', expand_x=True)],
    [sg.Text('Enter Email:', text_color='DarkGoldenrod'), sg.InputText(key='-EMAIL-', expand_x=True)],
    [sg.Text('Enter Number:', text_color='DarkGoldenrod'), sg.InputText(key='-NUMBER-', expand_x=True)],
    [sg.Text('Enter Address:', text_color='DarkGoldenrod'), sg.Multiline(key='-ADDRESS-', size=(40, 4))],
    [sg.Button('Save', button_color=('white', 'DarkGoldenrod')), sg.Button('Cancel', button_color=('white', 'Firebrick'))],
    sg.HorizontalSeparator(color='DarkGoldenrod'),
    
    # Search section
    [sg.Text('Search by First Name:', text_color='DarkGoldenrod'), sg.InputText(key='-SEARCHTEXT-', expand_x=True)],
    [sg.Button('Search', button_color=('white', 'DarkGoldenrod')), sg.Button('Clear', button_color=('white', 'Firebrick'))],
    [sg.Text('', key='-SEARCHOUTPUT-', size=(40, 4), text_color='DarkGoldenrod')],
]

# Create the window
window = sg.Window('Contact Entry', layout)

while True:
    # Read user events and inputs
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    # Capture input values
    fname = values.get('-FNAME-', '').strip()
    lname = values.get('-LNAME-', '').strip()
    gender = values.get('-GENDER-', '').strip()
    age = values.get('-AGE-', '').strip()
    email = values.get('-EMAIL-', '').strip()
    number = values.get('-NUMBER-', '').strip()
    address = values.get('-ADDRESS-', '').strip()

    # Save logic
    if event == 'Save':
        if fname and lname:  # Ensure required fields are filled
            # Validate age and contact number
            if not age.isdigit():
                sg.popup_error('Age must be a valid number!', title='Error', keep_on_top=True)
                continue
            if not number.isdigit():
                sg.popup_error('Contact number must be a valid number!', title='Error', keep_on_top=True)
                continue
            
            info = [fname, lname, gender, int(age), email, int(number), address]
            with open('info.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(info)
            sg.popup('Data Saved Successfully!', title='Success', keep_on_top=True)
            
            # Clear input fields
            for key in ['-FNAME-', '-LNAME-', '-GENDER-', '-AGE-', '-EMAIL-', '-NUMBER-', '-ADDRESS-']:
                window[key].update('')
        else:
            sg.popup_error('First Name and Last Name are required!', title='Error', keep_on_top=True)

    # Search logic
    elif event == 'Search':
        search_text = values.get('-SEARCHTEXT-', '').strip()
        if search_text:
            found = False
            try:
                with open('info.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row and row[0].lower() == search_text.lower():  # Match first name
                            window['-SEARCHOUTPUT-'].update(
                                f"First Name: {row[0]}\nLast Name: {row[1]}\nGender: {row[2]}\nAge: {row[3]}\n"
                                f"Email: {row[4]}\nNumber: {row[5]}\nAddress: {row[6]}"
                            )
                            found = True
                            break
                if not found:
                    window['-SEARCHOUTPUT-'].update('No match found.')
            except FileNotFoundError:
                sg.popup_error('No data file found!', title='Error', keep_on_top=True)
        else:
            sg.popup_error('Please enter a first name to search!', title='Error', keep_on_top=True)

    # Clear search
    elif event == 'Clear':
        window['-SEARCHTEXT-'].update('')
        window['-SEARCHOUTPUT-'].update('')

# Close the window
window.close()
