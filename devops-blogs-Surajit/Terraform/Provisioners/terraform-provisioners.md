### Terraform Provisioners
- Provisioners are used to execute scripts on a local or remote machine as part of resource creation or destruction.

ex - After VM is launched, install softwars required for app.

**-Types of provisioners**
1. Local exec - It invokes a local executable after a resource is created.

ex:- After ec2 is launched, fetch the ip and store it in file server_ip.txt

2. Remote exec - it allows to invoke scripts directly on the remote server.

ex:- After EC2 is launched, install apache software.

**- Defining Provisioners**
1. Provisioners are defined inside a specific resource.

	ex:

    ```
    resource "..." "..." {
			...
			<provisioners...>
		}
    ```


3. Provisioners are defined by "provisioner" followed by type of provisioner.
	ex:
  ```
      provisioner "local-exec" {}
	    provisioner "remote-exec" {}
  ```

4. for local provisioners, we have to specify command that needs to be run locally.

```
	provisioner "local-exec" {
		command = "..."
	    }
   ```

	example - (local-exec.tf)
 
	```
	resource "aws_instance" "myec2" {
		ami = "ami-1234"
		instance_type = "t2.micro"
		
		provisioner "local-exec" {
			command = echo ${self.public_ip} >> server_ip.txt
		}
	}
	```


6. for remote provisioner, since commands are executed on remote-server, we have to provide way for terraform to connect to remote server -

	example - (remote-exec.tf)
	```
			resource "aws_instance" "myec2" {
				ami = "ami-1234"
				instance_type = "t2.micro"
				key_name = "pvt-key.pem"
			}
			
			connection {
				type = 'ssh'
				user = 'ec2-user'
				private_key = file("./pvt-key.pem")
				host = self.public_ip
				vpc_security_group_ids = ["sg-17234dsnkjfsd1"]
			}

			provisioner "remote-exec" {
				inline = [
					"sudo yum install nginx -y",
					"sudo systemctl enable nginx",
					"sudo systemctl start nginx"
				]
			}
	```
	
**-Notes**

	If a creation-time provisioner fails, the resource is marked as tainted. 
	A tainted resource will be planned for destruction and recreation upon the next terraform apply.
	Terraform does this because a failed provisioner can leave a resource in a semi-configured state.

1. Apart from EC2, provisioners can be used with most of the resources as well.

2. Inside a resource block, we can even create multiple provisioners.

**- Creation-Time Provisioners**

By default, provisioners run when the resource they are defined within is created.

Creation-time provisioners are only run during creation, not during updating or any other lifecycle.

Note - 

**- Destroy-Time Provisioners**

Destroy provisioners are run before the resource is destroyed.

ex: Remove and De-link anti-virus software before EC2 gets terminated.

	ex: (local-exec.tf)
	```
	resource "aws_instance" "myec2" {
		ami = "ami-1234"
		instance_type = "t2.micro"
		
		provisioner "local-exec" {
			when = destroy
			command = "echo 'Destroy-Time provisioner'"
		}
	}
	```

**-Failure behaviour in provisioner**
1. By Default, provisioners that fail will also cause the terraform apply itself to fail. This will lead to resource being tainted and we have to re-create the resource. 

To change this default behaviour, i.e. even if provisioner fails, the terraform apply should succeed we can use on_failure setting.
	
Values excepted by on_failure are - continue[ignore the provisioner err] & fail[stop applying].
	
	ex: 
		provisioner "local-exec" {
			command = ""
			on_failure = continue
		}
