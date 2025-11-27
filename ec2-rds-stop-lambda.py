import boto3

def lambda_handler(event, context):
    # Initialize AWS clients
    ec2 = boto3.client('ec2')
    autoscaling = boto3.client('autoscaling')
    rds = boto3.client('rds')

    try:
        # Stop individual EC2 instances
        ec2_instances = ['i-00000000000000000', 'i-00000000000000000', 'i-00000000000000000', 'i-00000000000000000', 'i-0a86c4f0caff65942', 'i-06929c02e55537bfa', 'i-0a2d84b590bb20774']
        ec2.stop_instances(InstanceIds=ec2_instances)
        print(f"Stopped EC2 instances: {ec2_instances}")

        # Stop Auto Scaling groups
        asg_names = ['Your-Autoscaling-Group1', 'Your-Autoscaling-Group2']  # Replace with your Auto Scaling group names
        for asg_name in asg_names:
            autoscaling.update_auto_scaling_group(
                AutoScalingGroupName=asg_name,
                MinSize=0,
                DesiredCapacity=0
            )
            print(f"Scaled down Auto Scaling group: {asg_name} to 0 instances")

        # Stop RDS instances
        rds_instances = ['your-rds-instance-id-00000000']  # Replace with your RDS instance IDs
        for rds_instance in rds_instances:
            rds.stop_db_instance(DBInstanceIdentifier=rds_instance)
            print(f"Stopped RDS instance: {rds_instance}")

        return "Stop operation completed for EC2 instances, Auto Scaling groups, and RDS instances"

    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error occurred: {str(e)}"
