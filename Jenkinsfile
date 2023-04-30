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
                pwsh(script: 'docker images -a')
                pwsh(script: """
                    docker build -t lfmsonegrao/jenkins-pipeline .
                    """
                )
            }
        }
        stage('Run Tests') {
            steps {
                pwsh(script: """
                docker run --name $GIT_BRANCH lfmsonegrao/jenkins-pipeline
                """
                )
            }
        }
    }
}