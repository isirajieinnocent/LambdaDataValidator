<h1> Project Overview </h1>

This project is a serverless AWS Lambda function designed to automate the validation of CSV files stored in an S3 bucket. The function is triggered when a file is uploaded to S3 and performs data validation, error handling, and file management to ensure data integrity.


<h1> Architectural Diagram </h1>

![image](https://github.com/user-attachments/assets/65cf1097-54c1-400e-a327-8341831ce5d7)

<h1> Solution Overview </h1>

**Initialization:**

The Lambda function initializes the AWS S3 client using Boto3.

Retrieves the S3 bucket and file name from the event object.

Defines an error bucket for storing files with validation errors.

**File Retrieval and Parsing:**

Fetches the CSV file from the S3 bucket and reads its content.

Decodes the content from bytes to a string and parses the CSV data into a list, skipping the header row.

Returns an error if the CSV has no data after the header.

**Data Validation:**

***Validates each row in the CSV:***

Checks if the date field is in the correct format (%Y-%m-%d).

Verifies if the product_line is one of the allowed values (e.g., Bakery, Meat, Dairy).

Logs an error message if validation fails.

**Error Handling:**

***If errors are found:***

Moves the erroneous CSV file to the error bucket.

Deletes the original file from the billing bucket.

If no errors are found, returns a success response.

<h1> Key Features </h1>

Error Handling: Logs and flags errors, moving invalid files to an error bucket for tracking.

CSV File Parsing: Reads, decodes, and parses CSV data for validation.

Serverless Architecture: Fully serverless, leveraging AWS Lambda and S3 for automation.

<h1> Key Technologies </h1>

**AWS Lambda:** Serverless compute service for automation.

**AWS S3:** Stores CSV files and triggers the Lambda function.

**Boto3:** AWS SDK for Python, used to interact with S3 and perform file operations.

<h1> Impact </h1>

**Automated Validation:** Eliminates manual intervention by automating CSV file validation.

**Error Detection:** Ensures timely detection of errors, improving data quality.

**Cost-Effective:** Leverages serverless architecture for scalability and cost efficiency.

<h1> Key Achievements </h1>

Designed a serverless solution for automated CSV file validation.

Implemented error handling to ensure data integrity and track invalid files.

Improved operational efficiency by automating a previously manual process.

**This project highlights my expertise in AWS serverless architecture, Python programming, and data validation. It demonstrates my ability to build scalable, efficient, and error-resistant solutions for data processing.** 
