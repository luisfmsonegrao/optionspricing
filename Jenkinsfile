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
                powershell 'docker images ls'
                powershell 'docker build -t lfmsonegrao/pipeline-jenkins'
            }
        }
    }
}