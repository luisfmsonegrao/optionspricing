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
                powershell 'docker build -t lfmsonegrao/pipeline-jenkins .'
            }
        }

        stage('Run Tests') {

            steps {
                powershell "docker run --name $GIT_BRANCH lfmsonegrao/pipeline-jenkins"
            }
        }
        stage('Docker Teardown') {

            steps {
                powershell "docker stop --name $GIT_BRANCH"
                powershell "docker rm --name $GIT_BRANCH"
            }
        }
    }
}