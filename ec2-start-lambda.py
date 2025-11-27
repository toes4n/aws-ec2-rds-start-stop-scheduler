import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    autoscaling = boto3.client('autoscaling')

    try:
        # Start EC2 instances
        instance_ids = ['i-00000000000000000', 'i-00000000000000000', 'i-00000000000000000',
                        'i-00000000000000000'] # Replace with your EC2 instance IDs

        # Check which instances are stopped before starting
        describe_response = ec2.describe_instances(InstanceIds=instance_ids)
        instances_to_start = []

        for reservation in describe_response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'stopped':
                    instances_to_start.append(instance['InstanceId'])

        if instances_to_start:
            ec2.start_instances(InstanceIds=instances_to_start)
            print(f"Started instances: {instances_to_start}")

        # Update Auto Scaling groups
        autoscaling.update_auto_scaling_group(
            AutoScalingGroupName='Your-Autoscaling-Group-Name',
            MinSize=1, DesiredCapacity=1, MaxSize=1)

        autoscaling.update_auto_scaling_group(
            AutoScalingGroupName='Your-Autoscaling-Group-Name',
            MinSize=2, DesiredCapacity=2, MaxSize=2)

        return {'statusCode': 200, 'message': 'Operation completed successfully'}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'error': str(e)}
