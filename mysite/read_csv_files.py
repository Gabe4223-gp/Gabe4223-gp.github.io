import os
import csv

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Replace 'mysite' with the actual name of your Django project
import django

django.setup()

data_directory = os.path.join(os.getcwd(), 'Data')


def read_csv_files(directory):
    all_rows = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            print("Reading file:", file_path)
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = [row for row in reader]
                all_rows.extend(rows)
    return all_rows

    # if __name__ == "__main__":
    # Directory where CSV files are located (inside 'Data' directory)
    #data_directory = os.path.join(os.getcwd(), 'Data')

    # Call the function to read CSV files
    #rows = read_csv_files(data_directory)
