import os
import os.path
import xml.etree.ElementTree as ET
import sys


# ******************************* Function Definitions *************************

# uses an xpath condition as criteria in drill down search
# returns an element tree object
def get_element(element, plant):
    condition = "*/[" + element + " = '" + plant + "']/PRICE"
    for x in root.findall(condition):
        return x



# receives text value of element tree object along with user passed percent value
# returns a new price after a percent adjustment
def update_price_by_percent(element_value, percent):
    original_value = float(element_value)
    change_by = original_value * percent
    new_value = round(original_value + change_by, 2)
    return new_value


# searches and displays the siblings of the price element
# reports if no record is to be found found
def show_record_to_be_updated(element, plant):
    found = True
    for parent_type in root.findall('PLANT'):
        child = parent_type.find(element)
        if child.text == plant:
            print('Record to be updated \n')
            for sibling in parent_type.findall('*'):
                print(sibling.tag, ':', sibling.text)
            return True
        else:
            found = False
    print("No matching Record Found!")
    return found

# writes changes to file and creates a backup
def commit_changes(element, value):
    element.text = str(value)
    temp_file_name = 'temp.xml'
    tree.write(temp_file_name)
    backup_file = file_path.split('.')[0] + '.bak'
    if os.path.exists(backup_file):
        os.remove(backup_file)
    os.rename(file_path, backup_file)
    os.rename(temp_file_name, file_path)
    print('Changes Committed')

# displays the pre-edit price then the post-edit price
def print_update(element_to_update, new_price):
    print('\n***************************************\n')
    print(element_to_update.tag, ': From', element_to_update.text, 'To', str(new_price))


# ************************ General Error Handling *********************************

# flag for program errors
errors = False
error_message = ""

# test for a valid file in directory
if not (os.path.exists(sys.argv[1])):
    errors = True
    error_message = f"\n\n Given file cannot be found! {sys.argv[1]}\n\n"

# test for valid argument quantities
elif len(sys.argv) != 4:
    errors = True
    error_message = f"\n\n Expecting 3 arguments: {len(sys.argv) - 1} given\n\n"


else:
    try:  # test for numeric percent value
        num_test = float(sys.argv[3])

        # test for proper percent range
        if not -90 < num_test <= 100:
            errors = True
            error_message = f"\n\n Percent value is out of range! {sys.argv[3]}\n\n"

    except ValueError as e:  # catch numeric value exception
        errors = True
        error_message = f"\n\n Percent given is an improper value! {sys.argv[3]}\n\n"

# ******************************* Main Logic Area **************************************
if not errors:  # run main logic given no program errors

    file_path = sys.argv[1]  # 'plant_catalog.xml'
    tree = ET.parse(file_path)
    root = tree.getroot()
    search_element = "COMMON"
    plant_name = sys.argv[2].capitalize()  # "Anemone"
    percent_change = float(sys.argv[3]) / 100

    print('\n***************************************\n')
    if show_record_to_be_updated(search_element, plant_name):
        element_to_update = get_element(search_element, plant_name)
        new_price = update_price_by_percent(element_to_update.text, percent_change)
        print_update(element_to_update, new_price)
        commit_changes(element_to_update, new_price)
    print('\n***************************************\n')

# **************************** End of Main Logic Area **********************************
else:
    print(error_message)  # print error message if main logic is not run
