import boto3
from botocore.config import Config
import json
from datetime import datetime


def generate_code_using_bedrock(message: str, language: str) -> str:
    prompt_text = f"Write {language} code for the following task:\n{message}"

    body = {
        "text": prompt_text,
        "max_tokens": 2048,
        "temperature": 0.1,
        "top_p": 0.2,
        "top_k": 250
    }

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="ap-south-1",
            config=Config(read_timeout=300, retries={"max_attempts": 3})
        )

        response = bedrock.invoke_model(
            modelId="google.gemma-3-12b-it",
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )

        response_data = json.loads(response["body"].read().decode("utf-8"))
        code = response_data["candidates"][0]["text"].strip()
        return code

    except Exception as e:
        print(f"Error generating the code: {e}")
        return ""


def save_code_to_s3_bucket(code: str, s3_bucket: str, s3_key: str):
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=code
    )


def lambda_handler(event, context):
    body = json.loads(event["body"])
    message = body["message"]
    language = body["key"]

    generated_code = generate_code_using_bedrock(message, language)

    if not generated_code:
        return {
            "statusCode": 500,
            "body": json.dumps("Code generation failed")
        }

    timestamp = datetime.now().strftime("%H-%M-%S")
    s3_key = f"code-output/{timestamp}.txt"
    s3_bucket = "bedrock-course-bucket29"

    save_code_to_s3_bucket(generated_code, s3_bucket, s3_key)

    return {
        "statusCode": 200,
        "body": json.dumps("Code generated successfully")
    }
