Serverless solution I've implemented to significantly reduce our monthly AWS costs! 💰

We've automated the start and stop of non-production EC2, RDS, and Auto Scaling Group resources using AWS Lambda and Amazon EventBridge. This ensures our resources are only running during business hours (e.g., 8 AM to 7 PM, Monday-Friday), saving a substantial amount of money on compute resources.

## Key Components:

AWS Lambda (Python/Boto3): Serverless functions to execute the start and stop API calls for EC2, RDS, and ASGs.

Amazon EventBridge (Scheduler): Time-based rules (Cron expressions) to trigger the Lambda functions at scheduled times.

This setup is simple, cost-effective, and highly scalable. Check out the simplified code snippets and a full setup guide below.

 
