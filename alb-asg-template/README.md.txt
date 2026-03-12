# AWS CloudFormation - ALB & Auto Scaling Project

This project deploys a scalable web infrastructure on AWS using CloudFormation.

## Architecture

The CloudFormation template creates:

- Application Load Balancer (ALB)
- Auto Scaling Group (ASG)
- Launch Template
- Target Group
- Security Group
- Target Tracking Scaling Policy

## Features

- Infrastructure as Code with CloudFormation
- Automatic EC2 scaling based on CPU utilization
- Highly available architecture across multiple Availability Zones
- Apache web server installation using User Data
- Displays instance information (IP and date)

## AWS Services Used

- AWS CloudFormation
- EC2
- Auto Scaling
- Application Load Balancer
- VPC
- Security Groups

## How to Deploy

1. Go to AWS CloudFormation
2. Create a new stack
3. Upload the YAML template
4. Select VPC, Subnets and KeyPair
5. Deploy the stack

## Output

After deployment, CloudFormation outputs the **ALB DNS address** to access the web server.

Example:

http://your-alb-dns

---

Author: Abdulkadir Tutar
Junior DevOps Engineer