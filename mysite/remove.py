import csv
import os


def remove_double_quotes(input_file, encoding='utf-8'):
    cleaned_data = []
    with open(input_file, 'r', encoding=encoding) as csv_input:
        reader = csv.reader(csv_input)

        for row in reader:
            cleaned_row = [cell.replace('"', '') for cell in row]
            cleaned_data.append(cleaned_row)

    return cleaned_data


if __name__ == "__main__":
    input_filename = r"C:\Users\gpayu\PycharmProjects\pythonProject1\mysite\Data\chunk_1.csv"  # Change this to your input CSV filename

    # Assuming the CSV file is in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(r'C:\Users\gpayu\PycharmProjects\pythonProject1\mysite\Data\chunk_2.csv'))
    input_file_path = os.path.join(script_dir, input_filename)

    cleaned_data = remove_double_quotes(input_file_path)

    # Displaying the cleaned data
