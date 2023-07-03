import csv
import gzip
import shutil
import glob
import os

## handles errors with emojis in description, or any other column
def write_csv_row(writer, row_data):
    try:
        writer.writerow(row_data)
    except UnicodeEncodeError:
        encoded_row = [value.encode("utf-8", errors="ignore").decode("utf-8") if isinstance(value, str) else value for value in row_data]
        writer.writerow(encoded_row)

# write to csv file
def write_to_csv(csv_file: str, data_dir: str, headers: list, row_data: list):
    with open(f"{data_dir}{csv_file}", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in row_data:
            write_csv_row(writer, row)

# compress csv file
def compress_csv_file(data_dir: str = "directory of the data folder"):
    csv_files = glob.glob(f"{data_dir}/*.csv")
    for csv_file in csv_files:
        compressed_file = f"{csv_file}.gz"
        with open(csv_file, "rb") as f_in, gzip.open(compressed_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        os.remove(csv_file) # remove the original csv files