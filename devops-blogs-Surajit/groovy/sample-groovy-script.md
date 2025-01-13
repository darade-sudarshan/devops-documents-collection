1. gitCheckout.groovy
```
def call(Map stageParams) {
 
    checkout([
        $class: 'GitSCM',
        branches: [[name:  stageParams.branch ]],
        userRemoteConfigs: [[ url: stageParams.url ]]
    ])
  }
```

2. mvnTest.groovy
```
def call(){
    sh 'mvn test'
}
```

3. mvnIntegrationTest.groovy
```
def call(){
    sh 'mvn verify -DskipUnitTests'
}
```
4. statiCodeAnalysis.groovy
```
def call(credentialsId){

    withSonarQubeEnv(credentialsId: credentialsId) {
         sh 'mvn clean package sonar:sonar'
    }
}
```
5. QualityGateStatus.groovy
```
def call(credentialsId){
waitForQualityGate abortPipeline: false, credentialsId: credentialsId
}
```

6. mvnBuild.groovy
```
def call(){
    sh 'mvn clean install'
}
```
7. dockerBuild.groovy
```
def call(String aws_account_id, String region, String ecr_repoName){
    
    sh """
     docker build -t ${ecr_repoName} .
     docker tag ${ecr_repoName}:latest ${aws_account_id}.dkr.ecr.${region}.amazonaws.com/${ecr_repoName}:latest
    """
}
```
8. dockerImageScan.groovy
```
def call(String aws_account_id, String region, String ecr_repoName){
    
    sh """
    trivy image ${aws_account_id}.dkr.ecr.${region}.amazonaws.com/${ecr_repoName}:latest > scan.txt
    cat scan.txt
    """
}
```
9. dockerImagePush.groovy
```
def call(String aws_account_id, String region, String ecr_repoName){
    
    sh """
     aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${aws_account_id}.dkr.ecr.${region}.amazonaws.com
     docker push ${aws_account_id}.dkr.ecr.${region}.amazonaws.com/${ecr_repoName}:latest
    """
}
```
10. dockerImageCleanup.groovy
```
def call(String aws_account_id, String region, String ecr_repoName){
    
    sh """
     docker rmi ${ecr_repoName}:latest ${aws_account_id}.dkr.ecr.${region}.amazonaws.com/${ecr_repoName}:latest
    """
}
```
