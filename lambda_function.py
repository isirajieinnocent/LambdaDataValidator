import csv
import boto3
from datetime import datetime

# STAGE-1: Initialization
def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-east-1')

    try:
        billing_bucket = event['Records'][0]['s3']['bucket']['name']
        csvfile = event['Records'][0]['s3']['object']['key']
        error_bucket = 'error-rec-bucket'

        error_found = False 

        # STAGE-2: Retrieve and Parse the File
        obj = s3.get_object(Bucket=billing_bucket, Key=csvfile)
        content = obj['Body'].read().decode('utf-8')
        lines = content.splitlines()
        csv_reader = csv.reader(lines)
        data = list(csv_reader)[1:] 

        if not data:
            print("Error: No data found in CSV file after header.")
            return {'statusCode': 400, 'body': 'CSV file is empty after the header.'}

        # STAGE-3: Data Validation
        valid_product_line = ['Bakery', 'Meat', 'Dairy']
        valid_currencies = ['USD', 'CAD', 'EUR']

        for row in data:
            date = row[6]
            product_line = row[4]
            currency = row[7]
            bill_amount = float(row[8])  # Parse bill amount as float

            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                error_found = True
                print(f"Error in record {row[0]}: Incorrect format for date: {date}.")
                break

            if product_line not in valid_product_line:
                error_found = True
                print(f"Error in record {row[0]}: Unrecognized Product Line {product_line}.")
                break

        # STAGE-4: Error Handling
        if error_found:
            copy_source = {'Bucket': billing_bucket, 'Key': csvfile}

            try:
                s3.copy_object(CopySource=copy_source, Bucket=error_bucket, Key=csvfile)
                print(f"Moved erroneous file to: {error_bucket}")
                s3.delete_object(Bucket=billing_bucket, Key=csvfile)
                print("Deleted original file from bucket.")
            except Exception as e:
                print(f"Error while moving file: {str(e)}")
        else:
            return {'statusCode': 200, 'body': 'No error found in the CSV files!'}

    except Exception as e:
        print(f"Error in lambda_handler: {str(e)}")
        return {'statusCode': 500, 'body': 'Error processing the CSV file.'}
