import pandas as pd

# Items not found on main list, tag #, location, item,
# Items on second list that are not on first list

original = pd.read_excel('Official Excel Inventory.xlsx')
second = pd.read_excel('assets.xlsx')

#original = pd.read_excel('TestExcel1.xlsx')
#second = pd.read_excel('TestExcel2.xlsx')

selected = input("Do you want to list all items not found (1) or all the items not on the main list(2)")
selected = int(selected)

# Gets the items not found
if selected == 1:

    not_found = pd.DataFrame(columns=['Tag', 'Item', 'Found'])

    for i in range(len(second)):
        temp_row = second.iloc[i]
        if temp_row[5] == "No":
            not_found.loc[len(not_found.index)] = [temp_row[0], temp_row[3], temp_row[5]]

    print(not_found)

    final_frame = pd.DataFrame(columns=['Tag', 'Item', 'Room', 'Found'])
    pd.set_option('display.max_rows', 1000)

    print(original)

    for i in range(len(original)):
        row = original.iloc[i]
        tag = int(row[0])

        for j in range(len(not_found)):
            second_row = not_found.iloc[j]
            if tag == int(second_row[0]):
                final_frame.loc[len(final_frame.index)] = [row[0], row[4], row[3], second_row[2]]
            elif tag < int(second_row[0]):
                break

    print(final_frame)

# Gets the items on the inventory site but not in the main spreadsheet
elif selected == 2:
    print(original)

    # Assuming the first column is the tag/id column in both DataFrames
    original_tags = set(original.iloc[:, 0])
    second_tags = set(second.iloc[:, 0])

    # Items in second but not in original
    missing_items = second[~second.iloc[:, 0].isin(original_tags)]

    # Output the missing items
    print(missing_items)
    missing_items.to_excel("missing_items.xlsx")

# Gets the items that are on the main spreadsheet but not in the inventory system
elif selected == 3:
    print(original)

    # Assuming the first column is the tag/id column in both DataFrames
    original_tags = set(original.iloc[:, 0])
    second_tags = set(second.iloc[:, 0])

    # Items in second but not in original
    missing_items = original[~original.iloc[:, 0].isin(second_tags)]

    # Output the missing items
    print(missing_items)
    missing_items.to_excel("missing_items_in_main_sheet.xlsx")
