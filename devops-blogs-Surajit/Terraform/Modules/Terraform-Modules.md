# Terraform Modules

Terraform Modules - Terraform Modules are used for reusability. If multiple team members are creating any infra lets say EC2 instances multiple times, they dont have to write the EC2 resource creation code again and again, rather, we can create modules and they can be reused in our code with just link of the module and we can create the instance.

Syntax:
```
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.13.0"
}
```
-> We can create our custom modules or we can even use terraform provider (like AWS) created modules. We can keep our custom modules on Local, GIT, S3, etc.

-> Link to see how we can reference modules for each sources - https://developer.hashicorp.com/terraform/language/modules/sources .

-> Avoid hardcoding in the tf code for better reusability.

-> We should also use **required_provider** block with version constraints for module to work is important.
```
terraform {
  required_providers {
    mycloud = {
      source  = "mycorp/mycloud"
      version = "~> 1.0"
    }
  }
}

provider "mycloud" {
  # ...
}
```

-> **Route Module:** It resides in the main working directory of our terraform configuration. Its the entry point for your infrastructure definition.

example:
```
module "ec2"{
	source = "../modules/ec2"
}
```
-> **Child Module:** A module that has been called by another module is called child module.

example: the modules where the actual resource creation code is written are child modules like, ../modules/ec2 , ../modules/vpc , etc...


-> **Example of using Output**

Lets Say, I have a module to create an EC2 Instance. Now, I want to use it and create an EC2 and I also want to create an EIP and attach it to the instance. Here, creating an attaching an EIP to the will require us to create an child module Output.

Example: 
1. modules.tf
```
resource "aws_instance" "myec2"{
  ami = var.image_id
  instance = var.instance_type
}

output "instance_id"{
  value = "aws_instance.myec2.id"
}
```
2. main.tf
```
module "ec2" {
  source = "../modules/ec2"
}

resource "aws_eip" "lb" {
  instance = "module.ec2.instance_id"
  domain  = "vpc"
}
```
-> **Basic Industry standards Module Structure**

The standard module structure is a file and directory layout HashiCorp recommends for reusable modules.

A minimal recommended module following the standard structure is shown below -

|- README.md

|- main.tf

|- variable.tf

|- output.tf



