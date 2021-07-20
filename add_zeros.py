from csv import writer

def add_zeros(file_name, num_rows):
    new_row = [0.0,0.0]
    with open(file_name, 'a+', newline='', encoding='utf-8-sig') as asset:
        # Create a writer object from csv module
        csv_writer = writer(asset)
        # Add contents of list as last row in the csv file
        for i in range(num_rows):
            csv_writer.writerow(new_row)