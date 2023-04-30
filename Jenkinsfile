pipeline {

    agent any

    stages {

        stage('GIT BRANCH') {

            steps {

                echo "Current branch name is: $GIT_BRANCH"

            }
        }

        stage('Docker Build') {

            steps {
                pwsh(script: 'docker images ls")
            }
        }
    }
}