This project is a serverless AWS Lambda function designed to automate the validation of CSV files stored in an S3 bucket. The function is triggered by an event from S3 when a file is uploaded, and performs the following steps:

1. Initialization:
The Lambda function begins by initializing the AWS S3 client using boto3 and retrieves the S3 bucket and the file name (CSV) from the event object passed to it.
It also defines a separate error bucket where files with validation errors will be moved.

2. File Retrieval and Parsing:
The Lambda function fetches the CSV file from the S3 bucket specified in the event and reads its content.
It then decodes the content from bytes to string and parses the CSV data into a list, skipping the header row. If the CSV has no data after the header, it returns an error response.

3. Data Validation:
The function validates each row in the CSV:
It checks if the date field is in the correct format (%Y-%m-%d).
It verifies if the product_line is one of the allowed values (Bakery, Meat, Dairy).
If any validation fails, an error flag is set, and an error message is logged.

4. Error Handling:
If any errors are found, the function:
Moves the erroneous CSV file to an "error" bucket for tracking.
Deletes the original file from the billing bucket.
If no errors are found, it returns a success response indicating that the CSV is valid.

Key Features:
Error Handling: All errors, including incorrect date formats and invalid product lines, are logged and flagged for moving the file to an error bucket.
CSV File Parsing: The function reads, decodes, and parses CSV data for business logic validation.
Serverless: The Lambda function is fully serverless, leveraging AWS S3 to trigger the process and perform file operations.


In Summary;
This is a  serverless Lambda function that automates the validation of CSV files uploaded to an S3 bucket. It performs file retrieval, data parsing, validation, and error handling. If errors are detected, it moves the file to an error bucket and deletes the original file. This solution automates data validation, ensuring timely error detection with manual intervention
