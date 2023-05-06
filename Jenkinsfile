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
            post {
                success {
                    echo "Test suite passed"
                }
                failure {
                    echo "Test suite failed"
                }
                always {
                    powershell "docker stop $GIT_BRANCH"
                    powershell "docker rm $GIT_BRANCH"
                }
            }
        }
    }
}