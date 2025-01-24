import generate_data
from extract import read_csv
from transform import transform_data
from load import load_data_to_db

CSV_FILE = "data/users.csv"
    
if __name__ == "__main__":
    generate_data.generate_fake_users_csv(CSV_FILE)
    data = read_csv(CSV_FILE)
    transformed_data = transform_data(data)
    load_data_to_db(transformed_data)
