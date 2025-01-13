# Sample Jenkins File

```
pipeline {
    agent any

    environment {
        // Define environment variables
        APP_ENV = 'production'
        BUILD_VERSION = "v${env.BUILD_ID}"
    }

    options {
        // Timeout the pipeline if it runs longer than 1 hour
        timeout(time: 1, unit: 'HOURS')
        // Skip stages if they already exist with the same state
        skipStagesAfterUnstable()
    }

    parameters {
        // Parameterize the pipeline for dynamic input
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build from')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests after build')
    }

    triggers {
        // Schedule pipeline runs (Cron syntax)
        cron('H 12 * * 1-5') // Run daily at 12 PM, Monday to Friday
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Fetch code from version control
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies using a package manager
                script {
                    if (fileExists('package.json')) {
                        sh 'npm install'
                    } else {
                        echo 'No package.json found, skipping...'
                    }
                }
            }
        }

        stage('Build Application') {
            steps {
                // Compile the code or package the app
                sh 'npm run build'
            }
        }

        stage('Run Tests') {
            when {
                expression {
                    return params.RUN_TESTS == true
                }
            }
            steps {
                // Run unit tests
                sh 'npm test'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                // Deploy code to production
                sh 'npm run deploy'
            }
        }
    }

    post {
        always {
            // Actions to run at the end regardless of the pipeline result
            cleanWs() // Clean the workspace
            echo 'Cleaning workspace...'
        }

        success {
            // Actions when the pipeline succeeds
            echo 'Pipeline succeeded!'
            archiveArtifacts artifacts: '**/build/**', allowEmptyArchive: true
        }

        failure {
            // Actions when the pipeline fails
            echo 'Pipeline failed!'
            mail to: 'dev-team@example.com', subject: 'Build Failed', body: "Build ${env.BUILD_VERSION} failed"
        }
    }
}
```

### Detailed Explanation of Each Component

#### 1. `pipeline`
The `pipeline` block is the root of a Jenkinsfile, defining the entire pipeline. It organizes everything from agent allocation to stages and post-actions.

#### 2. `agent`
```groovy
agent any
```
Specifies where the pipeline or stage should run. `any` means the pipeline can run on any available Jenkins agent. You can specify particular agents with labels.

#### 3. `environment`
```groovy
environment {
    APP_ENV = 'production'
    BUILD_VERSION = "v${env.BUILD_ID}"
}
```
Defines environment variables accessible throughout the pipeline. These can be used in the `steps`, `stages`, or `post` sections.

#### 4. `options`
```groovy
options {
    timeout(time: 1, unit: 'HOURS')
    skipStagesAfterUnstable()
}
```
Pipeline options, such as timeout control and behavior when stages fail or become unstable:
- `timeout`: Aborts the pipeline if it runs for more than the specified time.
- `skipStagesAfterUnstable`: Prevents executing stages after a stage is marked unstable.

#### 5. `parameters`
```groovy
parameters {
    string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build from')
    booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests after build')
}
```
Defines build parameters that can be used when starting the pipeline. Examples:
- `string`: Input a string value, e.g., branch name.
- `booleanParam`: A checkbox for enabling/disabling options (e.g., running tests).

#### 6. `triggers`
```groovy
triggers {
    cron('H 12 * * 1-5')
}
```
Automatically triggers the pipeline based on a schedule. This example uses a cron expression to run every weekday at 12 PM.

#### 7. `stages`
The `stages` block contains multiple `stage` blocks that define distinct pipeline phases.

##### Stage: `Checkout Code`
```groovy
stage('Checkout Code') {
    steps {
        checkout scm
    }
}
```
This stage checks out code from the source control repository defined in the pipeline job (e.g., GitHub or GitLab).

##### Stage: `Install Dependencies`
```groovy
stage('Install Dependencies') {
    steps {
        script {
            if (fileExists('package.json')) {
                sh 'npm install'
            }
        }
    }
}
```
Executes a script to install dependencies using `npm` if a `package.json` is found in the workspace.

##### Stage: `Build Application`
```groovy
stage('Build Application') {
    steps {
        sh 'npm run build'
    }
}
```
Builds or compiles the application using `npm run build`.

##### Stage: `Run Tests`
```groovy
stage('Run Tests') {
    when {
        expression {
            return params.RUN_TESTS == true
        }
    }
    steps {
        sh 'npm test'
    }
}
```
Runs tests if the `RUN_TESTS` parameter is `true`. The `when` block controls conditional execution.

##### Stage: `Deploy to Production`
```groovy
stage('Deploy to Production') {
    when {
        branch 'main'
    }
    steps {
        sh 'npm run deploy'
    }
}
```
Deploys the code to production only when the `main` branch is built. The `when` block limits this to production environments.

#### 8. `post`
The `post` block defines actions that should occur after the pipeline runs, regardless of success or failure.

```groovy
post {
    always {
        cleanWs() // Always clean the workspace
        echo 'Cleaning workspace...'
    }

    success {
        echo 'Pipeline succeeded!'
        archiveArtifacts artifacts: '**/build/**', allowEmptyArchive: true
    }

    failure {
        echo 'Pipeline failed!'
        mail to: 'dev-team@example.com', subject: 'Build Failed', body: "Build ${env.BUILD_VERSION} failed"
    }
}
```
- `always`: Executes regardless of pipeline outcome.
- `success`: Runs only if the pipeline succeeds.
- `failure`: Runs only if the pipeline fails. In this case, an email is sent to the dev team.

### Summary of Jenkinsfile Components:
1. **Pipeline**: Top-level container for the pipeline.
2. **Agent**: Specifies where the pipeline will run.
3. **Environment**: Defines environment variables.
4. **Options**: Global options like timeouts.
5. **Parameters**: Allows passing dynamic inputs into the pipeline.
6. **Triggers**: Automatically runs pipelines on a schedule or other triggers.
7. **Stages**: Contains the individual steps that run sequentially.
8. **Post**: Defines actions to take after the pipeline finishes (success or failure).

