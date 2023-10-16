# Data Processing Lambda Function

This Lambda function is designed to process data from a GitHub repository and upload it to an S3 bucket. It performs the following tasks:

- Retrieves an access token from AWS Secrets Manager.
- Calls a GitHub API to fetch JSON files from a specified repository and folder.
- Parses the JSON files and extracts specific data into a CSV format.
- Uploads the CSV data to an S3 bucket.

## Usage

To use this Lambda function, follow these steps:

1. Configure your AWS Lambda function with the necessary environment variables, including `repository_owner`, `repository_name`, `branch_name`, `folder_path`, `s3_bucket`, and `s3_folder`.

2. Make sure you have stored the GitHub access token in AWS Secrets Manager with the name `data_dict_access_token`.

3. Deploy the Lambda function.

4. The Lambda function will automatically fetch data from the GitHub repository, process it, and upload the result to the specified S3 bucket.

## Prerequisites

- AWS Lambda
- AWS Secrets Manager
- GitHub API Token

## Environment Variables

- `repository_owner`: Owner of the GitHub repository.
- `repository_name`: Name of the GitHub repository.
- `branch_name`: Name of the branch in the GitHub repository.
- `folder_path`: Path to the folder containing JSON files in the GitHub repository.
- `s3_bucket`: Name of the S3 bucket to upload data.
- `s3_folder`: Folder path within the S3 bucket.

## License

This project is licensed under the XYZ License - see the [LICENSE](LICENSE) file for details.
