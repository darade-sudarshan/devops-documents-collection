# Step by Step setup of a CI-CD pipeline with 

**Step 1** - 
Provision 2 servers - a Jenkins and a Maven Server.

**Step 2** - 
Install Jenkins on Jenkins server.

**Step 3** - 
Login to the Jenkins server, enable and start the Jenkins and login to it with http://<ip>:8080 and complete all the pre-requisites.

**Step 4** - 
Install Maven on the provisioned Maven server and test it with - /opt/maven-3.9/bin/mvn clean

**Step 5** - 
Add Maven credentials  and maven node to Jenkins be following below steps -
A - Add Credentials

a) Manage Jenkins --> Manage Credentials --> System --> Global credentials --> Add credentials

b) Provide the below info to add credentials
kind: ssh username with private key
Scope: Global
ID: maven_slave
Username: ec2-user
private key: kubedemo.pem key content

B - Add node

a) Goto Manage Jenkins --> Manage nodes and clouds --> New node --> Permanent Agent

b) Provide the below info to add the node
Number of executors: 3
Remote root directory: /home/ec2-user/jenkins
Labels: maven
Usage: Use this node as much as possible
Launch method: Launch agents via SSH
Host: <Private_IP_of_Slave>
Credentials: <Jenkins_Slave_Credentials>
Host Key Verification Strategy: Non verifying Verification Strategy
Availability: Keep this agent online as much as possible

**Step 6 - Create a 'Jenkinsfile' to execute the builds in Jenkins server stage by stage(ex: build, scan, deploy, etc)**. 

Sample code -

```
pipeline {
    agent {
        node {
            label 'maven'
        }
    }
environment {
    PATH = "/opt/apache-maven-3.9.2/bin:$PATH"
}
    stages {
        stage("build"){
            steps {
                 echo "----------- build started ----------"
                sh 'mvn clean deploy -Dmaven.test.skip=true'
                 echo "----------- build complted ----------"
            }
        }
        stage("test"){
            steps{
                echo "----------- unit test started ----------"
                sh 'mvn surefire-report:report'
                 echo "----------- unit test Complted ----------"
            }
        }
}
```

**Step 7** - 
Creating a Multibranch Pipeline and setting it up with the respective git url and JenkinFile file reference.

**Step 8** - 
Create a webhooks for auto build when the code is checked-in. 

Steps for setup is below - 

i) Install "multibranch scan webhook trigger" plugin
From dashboard --> manage jenkins --> manage plugins --> Available Plugins
Search for "Multibranch Scan webhook Trigger" plugin and install it.

ii) Go to multibranch pipeline job job --> configure --> Scan Multibranch Pipeline Triggers --> Scan Multibranch Pipeline Triggers --> Scan by webhook
Trigger token: <token_name>

iii) Add webhook to GitHub repository Github repo --> settings --> webhooks --> Add webhook
Payload URl: <jenkins_IP>:8080/multibranch-webhook-trigger/invoke?token=<token_name>
Content type: application/json
Which event would you like to trigger this webhook: just the push event

**Step 9** -
Setting up SonarQube for code scan and quality check. Steps as below

i) Create Sonar cloud account on https://sonarcloud.io

ii) Generate an Authentication token on SonarQube     Account --> my account --> Security --> Generate Tokens

iii) On Jenkins create credentials    Manage Jenkins --> manage credentials --> system --> Global credentials --> add credentials  - Credentials type: Secret text  - ID: sonarqube-key

iv) Install SonarQube plugin     Manage Jenkins --> Available plugins     Search for sonarqube scanner

v) Configure sonarqube server    Manage Jenkins --> Configure System --> sonarqube server    Add Sonarqube server    - Name: sonar-server    - Server URL: https://sonarcloud.io/    - Server authentication token: sonarqube-key

vi) Configure sonarqube scanner    Manage Jenkins --> Global Tool configuration --> Sonarqube scanner    Add sonarqube scanner    - Sonarqube scanner: sonar-scanner

**Step 10 -** 

Writing sonar scan step in Jenkinsfile for analysis. Sample code as below -

```
 stage('SonarQube analysis') {
    environment {
      scannerHome = tool 'my-sonar-scanner'
    }
    steps{
    withSonarQubeEnv('my-sonarqube-server') { // If you have configured more than one global server connection, you can specify its name
      sh "${scannerHome}/bin/sonar-scanner"
    }
    }
  }
  stage("Quality Gate"){
    steps {
        script {
        timeout(time: 1, unit: 'HOURS') { // Just in case something goes wrong, pipeline will be killed after a timeout
    def qg = waitForQualityGate() // Reuse taskId previously collected by withSonarQubeEnv
    if (qg.status != 'OK') {
      error "Pipeline aborted due to quality gate failure: ${qg.status}"
    }
  }
}
    }
  }
```

**Step 11** - 
Jfrog setup for publishing jar and war file.

i) Create Artifactory account
ii) Generate an access token with username (username must be your email id)
iii) Add username and password under jenkins credentials
iv) Install Artifactory plugin
v) Update Jenkinsfile with jar publish stage - 

```
     def registry = 'https://my.jfrog.io'
         stage("Jar Publish") {
        steps {
            script {
                    echo '<--------------- Jar Publish Started --------------->'
                     def server = Artifactory.newServer url:registry+"/artifactory" ,  credentialsId:"artifactory_token"
                     def properties = "buildid=${env.BUILD_ID},commitid=${GIT_COMMIT}";
                     def uploadSpec = """{
                          "files": [
                            {
                              "pattern": "jarstaging/(*)",
                              "target": "libs-release-local/{1}",
                              "flat": "false",
                              "props" : "${properties}",
                              "exclusions": [ "*.sha1", "*.md5"]
                            }
                         ]
                     }"""
                     def buildInfo = server.upload(uploadSpec)
                     buildInfo.env.collect()
                     server.publishBuildInfo(buildInfo)
                     echo '<--------------- Jar Publish Ended --------------->'  
            
            }
        }   
    }   
```

vi) Check-point: Ensure below are update

a) your jfrog account details in place of https://my.jfrog.io in the defination of registry def registry = 'https://my.jfrog.io'

b) Credentials id in the place of jfrogforjenkins in the def server = Artifactory.newServer url:registry+"/artifactory" ,  credentialsId:"artifactory_token"

c) Maven repository name in the place of libs-release-local in the "target": "ttrend-libs-release-local/{1}".

**Step 12** - 
Build and Publish a Docker image

i) Write and add dockerfile in the source code
```
	FROM openjdk:8
	ADD jarstaging/com/my/demo-workshop/2.0.2/demo-workshop-2.0.2.jar demo-workshop.jar
	ENTRYPOINT ["java", "-jar", "demo-workshop.jar"]
```

Check-point: version number in pom.xml and dockerfile should match

ii) Create a docker repository in the Jfrog
    repository name: my-docker

iii) Install docker pipeline plugin

iv) Update Jenkins file with the below stages - 
```
   def imageName = 'my01.jfrog.io/my-docker/ttrend'
   def version   = '2.0.2'
    stage(" Docker Build ") {
      steps {
        script {
           echo '<--------------- Docker Build Started --------------->'
           app = docker.build(imageName+":"+version)
           echo '<--------------- Docker Build Ends --------------->'
        }
      }
    }

    stage (" Docker Publish "){
        steps {
            script {
               echo '<--------------- Docker Publish Started --------------->'  
                docker.withRegistry(registry, 'artifactory_token'){
                    app.push()
                }    
               echo '<--------------- Docker Publish Ended --------------->'  
            }
        }
    }

```
v) Check-point:

a) Provide jfrog repo URL in the place of my01.jfrog.io/my-docker in def imageName = 'my01.jfrog.io/my-docker/ttrend'
b) Match version number in def version   = '2.0.2' with pom.xml version number
c) Ensure you have updated credentials in the field of artifactory_token in docker.withRegistry(registry, 'artifactory_token'){

Note: make sure docker service is running on the slave system, and docker should have permissions to /var/run/docker.sock

**Step 13** - 
Setup Kubernetes cluster using terraform 
1. EKS module code is available over [here](https://github.com/ravdy/RTP-03/tree/main/terraform/v7-EC2_VPC_and_EKS/eks)  
   Through this eks module we are creating  
     - IAM Roles
     - IAM Policies
     - EKS Cluster
     - Node Group

2. Copy eks and sg_eks modules onto terraform folder.

3. Create vpc folder and move existing files inside to this.

4. Add sg_eks module and eks modules in the vpc.tf file.
   ```sh 
     module "sgs" {
       source = "../sg_eks"
       vpc_id     =     aws_vpc.dpp-vpc.id
    }

     module "eks" {
          source = "../eks"
          vpc_id     =     aws_vpc.dpp-vpc.id
          subnet_ids = [aws_subnet.dpp-public-subnet-01.id,aws_subnet.dpp-public-subnet-02.id]
          sg_ids = module.sgs.security_group_public
    }
   ```
 by this time we are ready with our terraform modules to create a cluster

**Step 14** -
Integrate build server with Kubernetes cluster 

1. Setup kubectl   
   ```sh 
     curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.24.9/2023-01-11/bin/linux/amd64/kubectl
     chmod +x ./kubectl
     mv ./kubectl /usr/local/bin
     kubectl version
   ``` 

2. Make sure you have installed awscli latest version. If it has awscli version 1.X then remove it and install awscli 2.X  
    ```sh 
     yum remove awscli 
     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     unzip awscliv2.zip
     sudo ./aws/install --update
    ```

3. Configure awscli to connect with aws account  
    ```sh 
     aws configure
     Provide access_key, secret_key
    ```

4. Download Kubernetes credentials and cluster configuration (.kube/config file) from the cluster  

   ```sh 
    aws eks update-kubeconfig --region us-east-1 --name my-eks-01
   ```

**Step 15** - 
Integrate Jfrog with Kubernetes cluster
  
1. Create a dedicated user to use for a docker login   
     user menu --> new user  
     `user name`: jfrogcred  
     `email address`: logintoaws@gmail.com  
     `password`: <passwrod>  

2. To pull an image from jfrog at the docker level, we should log into jfrog using username and password   
```sh 
 docker login https://my.jfrog.io
```

3. genarate encode value for ~/.docker/config.json file 
  ```sh 
   cat ~/.docker/config.json | base64 -w0
   ```
   
`Kubernetes Documentation for reference:` https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
Make sure secret value name `regcred` is updated in the deployment file.  

  `copy auth value to encode` cat ~/.docker/config.json | base64 -w0 `use above command output in the secret`
```

**Step 16** -

Helm setup 

1. Install helm
   ```sh 
   curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
   chmod 700 get_helm.sh
   ./get_helm.sh
   ```
2. Validate helm installation 
   ```sh
   helm version
   helm list
   ```
3. [optional] Download .kube/config file to build the node 
   ```sh
   aws eks update-kubeconfig --region ap-south-1 --name ed-eks-01
   ```

4. Setup helm repo 
   ```sh 
   helm repo list
   helm repo add stable https://charts.helm.sh/stable
   helm repo update
   helm search repo <helm-chart>
   helm search repo stable
   ```

5. Install mysql charts on Kubernetes 
   ```sh 
   helm install demo-mysql stable/mysql 
   ```
6. To pull the package from repo to local 
   ```sh 
   helm pull stable/mysql 
   ```

  *Once you have downloaded the helm chart, it comes as a zip file. You should extract it.* 

  In this directory, you can find 
  - templates
  - values.yaml
  - README.md
  - Chart.yaml

If you'd like to change the chart, please update your templates directory  and modify the version (1.6.9 to 1.7.0) in the chart.yaml then you can run the command to pack it after your update.

```sh
 helm package mysql
```

To deploy helm chat
```sh 
 helm install mysqldb mysql-1.6.9.tgz
```

Above command deploy MySQL 
To check deployment 
```sh 
 helm list 
```
To uninstall 
```sh 
 helm uninstall mysqldb
```

To install nginx 
```sh 
 helm repo search nginx 
 helm install demo-nginx stable/nginx-ingress
```

**Step 17** - 
Helm chart for ttrend(Create a custom Helm chart)

1. To create a helm chart template 
   ```sh 
   helm create ttrend
   ```

    by default, it contains 
    - values.yaml
    - templates
    - Charts.yaml
    - charts

2. Replace the template directory with the manifest files and package it
   ```sh
   helm package ttrend
   ```
3. Change the version number in the 
   ```sh 
   helm install ttrend ttrend-0.1.0.tgz
   ```

4. Create a jenkins job for the deployment 
   ```sh 
   stage(" Deploy ") {
          steps {
            script {
               echo '<--------------- Helm Deploy Started --------------->'
               sh 'helm install ttrend ttrend-0.1.0.tgz'
               echo '<--------------- Helm deploy Ends --------------->'
            }
          }
        }
   ```

5. To list installed helm deployments
   ```sh 
   helm list -a
   ```

Other useful commands
1. to change the default namespace to valaxy
   ```sh
   kubectl config set-context --current --namespace=valaxy
   ```

**Step 18** - 
Prometheus & grafana setup

**pre-requisites**
1. Kubernetes cluster
2. helm

**Setup Prometheus**

1. Create a dedicated namespace for prometheus 
   ```sh
   kubectl create namespace monitoring
   ```

2. Add Prometheus helm chart repository
   ```sh
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts 
   ```

3. Update the helm chart repository
   ```sh
   helm repo update
   helm repo list
   ```

4. Install the prometheus

   ```sh
    helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring
   ```

5. Above helm create all services as ClusterIP. To access Prometheus out side of the cluster, we should change the service type load balancer
   ```sh 
   kubectl edit svc prometheus-kube-prometheus-prometheus -n monitoring
   
   ```
6. Loginto Prometheus dashboard to monitor application
   https://ELB:9090

7. Check for node_load15 executor to check cluster monitoring 

8. We check similar graphs in the Grafana dashboard itself. for that, we should change the service type of Grafana to LoadBalancer
   ```sh 
   kubectl edit svc prometheus-grafana
   ```

9.  To login to Grafana account, use the below username and password 
    ```sh
    username: admin
    password: prom-operator
    ```
10. Here we should check for "Node Exporter/USE method/Node" and "Node Exporter/USE method/Cluster"
    USE - Utilization, Saturation, Errors
   
11. Even we can check the behavior of each pod, node, and cluster.

