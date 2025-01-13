# Integrating Ansible with Terraform

Terraform handles provisioning, while Ansible can take care of configuration management and application deployment. 

Here’s a step-by-step guide on how to integrate them:

### 1. **Provision Infrastructure with Terraform**

First, We’ll use Terraform to provision Our infrastructure. Here’s a basic example of a Terraform configuration file (`main.tf`) to provision an AWS EC2 instance:

```hcl
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # Update with a valid AMI ID
  instance_type = "t2.micro"

  tags = {
    Name = "example-instance"
  }
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}
```

### 2. **Apply Terraform Configuration**

Run Terraform to apply the configuration and provision Our resources:

```bash
terraform init
terraform apply
```

### 3. **Fetch Terraform Outputs**

Terraform can generate outputs that can be used by Ansible. For example, We might want to get the public IP of an EC2 instance to use in Ansible:

```bash
terraform output instance_ip
```

### 4. **Create an Ansible Inventory File**

Create an Ansible inventory file that uses the Terraform output. This file can be generated dynamically by using a script. For example, save the following as `inventory.ini`:

```ini
[web]
instance ansible_host=<INSTANCE_IP> ansible_user=ec2-user
```

We can also generate this dynamically with a script if We have many instances or want automation:

```bash
#!/bin/bash

# Fetch the IP address from Terraform
INSTANCE_IP=$(terraform output -raw instance_ip)

# Generate the Ansible inventory file
cat <<EOF > inventory.ini
[web]
instance ansible_host=${INSTANCE_IP} ansible_user=ec2-user
EOF
```

### 5. **Write Our Ansible Playbook**

Create an Ansible playbook (`playbook.yml`) to configure Our instance:

```yaml
- hosts: web
  become: yes
  tasks:
    - name: Ensure Nginx is installed
      yum:
        name: nginx
        state: present

    - name: Start Nginx service
      service:
        name: nginx
        state: started
        enabled: yes
```

### 6. **Run Ansible Playbook**

Run OurAnsible playbook using the generated inventory file:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

### 7. **Automate the Integration**

For better automation, We can combine these steps into a single script. Here’s an example script that runs Terraform, generates the inventory file, and then runs Ansible:

```bash
#!/bin/bash

# Apply Terraform
terraform apply -auto-approve

# Fetch the IP address
INSTANCE_IP=$(terraform output -raw instance_ip)

# Generate Ansible inventory
cat <<EOF > inventory.ini
[web]
instance ansible_host=${INSTANCE_IP} ansible_user=ec2-user
EOF

# Run Ansible playbook
ansible-playbook -i inventory.ini playbook.yml
```

### Summary

1. **Provision infrastructure** with Terraform.
2. **Fetch outputs** from Terraform.
3. **Generate an Ansible inventory file** based on Terraform outputs.
4. **Write and run OurAnsible playbook** to configure the infrastructure.

This setup can be customized based on Ourspecific use case and infrastructure requirements.
