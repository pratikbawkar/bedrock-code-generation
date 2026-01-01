# bedrock-code-generation

Using Aws Bedrock and ai model to generate code and save the output in S3 bucket. 
Serverless AI Code Generation using Amazon Bedrock

This project demonstrates a **serverless Generative AI application** built on AWS that generates programming code using **Amazon Bedrock** and stores the output in **Amazon S3**.  
The system exposes a REST API that accepts instructions and a programming language, invokes a foundation model, and saves the generated code automatically.

---
🚀 Features
- Serverless architecture using AWS Lambda
- AI-powered code generation with Amazon Bedrock (Claude model)
- REST API built with Amazon API Gateway
- Automatic storage of generated code in Amazon S3
- CloudWatch logging for monitoring and debugging
- Language-agnostic design (extensible)

---
🧩 Architecture

Client (Postman / Frontend)  
→ API Gateway (HTTP API)  
→ AWS Lambda (Python)  
→ Amazon Bedrock (Foundation Model)  
→ Amazon S3 (Code Storage)  
→ CloudWatch (Logs & Metrics)

---
🛠️ Tech Stack

- **Amazon Bedrock** – Generative AI models
- **AWS Lambda** – Serverless backend
- **Amazon API Gateway** – REST API
- **Amazon S3** – Code storage
- **Amazon CloudWatch** – Logging & debugging
- **Python (boto3)** – AWS SDK
- **Postman** – API testing

---
 📂 Project Structure

+-------------+       +---------------+       +------------------+
|   Client    | ----> | API Gateway   | ----> | AWS Lambda       |
| (Postman)   |       | (POST /code)  |       | (Python)         |
+-------------+       +---------------+       +------------------+
                                                     |
                                                     v
                                            +------------------+
                                            | Amazon Bedrock   |
                                            | (Claude Model)   |
                                            +------------------+
                                                     |
                                                     v
                                            +------------------+
                                            | Amazon S3        |
                                            | code-output/     |
                                            +------------------+

                        +------------------+
                        | CloudWatch Logs  |
                        +------------------+
