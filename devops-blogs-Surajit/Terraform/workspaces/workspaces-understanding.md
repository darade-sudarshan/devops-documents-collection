Terraform workspaces enables us to manage multiple set of deployments from the same set of configuration file.

To check terraform workspace list -
```
terraform workspace list
```

To switch to different workspace -
```
terraform workspace select <workspace_name>
```

To check in which workspace i m currently in -

```
terraform workspace show
```

To create a new workspace - 

```
terraform workspace new <name of the workspace>
```

Now, lets say based on env we need diff instance_type. Like, t2.micro for dev and m5.large for prod. In this case we will choose Types and Values expression. 

```
local{
 instance_type = {
  default = "t2.nano"
  dev     = "t2.micro"
  prod    = "m5.large"
 }
}
```
Then, in the resource, we can refer the local as 

```
local.instance_types[terraform.workspace]

```
Hashicorp link for this - https://developer.hashicorp.com/terraform/language/expressions/types

*****how can we create terraform workspace to create resources in different aws account?
