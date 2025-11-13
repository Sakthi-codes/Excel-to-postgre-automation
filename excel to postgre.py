import pandas as pd
import psycopg2
from sqlalchemy import create_engine

db_user = "postgres"
db_password = "Canbd^1"
db_host = "localhost"
db_port = "5432"
db_name = "ocean2"



excel_file_path = r"C:\Users\sakth\Downloads\sample_data.xlsx"
sheet_name = "sample_data"
table_name = "ocean_info"

try:
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    print("Successfully read Excel data into a DataFrame.")

    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()
    print("Successfully connected to the PostgreSQL database.")

    engine_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(engine_string)

    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Successfully wrote data to the '{table_name}' table.")

    cursor.close()
    conn.close()
    print("Database connection closed.")

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
