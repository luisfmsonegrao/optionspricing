pipeline {
    agent any

    stages {
        stage('Branch name') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
        stage('Docker Build') {
            steps {
                powershell(script: 'docker images -a')
                powershell(script: """
                    cd binomialoptionspricing/
                    docker images -a
                    docker build -t jenkins-pipeline
                    docker images -a
                    cd ..
                """)
            }
        }
    }
}