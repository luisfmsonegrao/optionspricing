pipeline {
    agent any

    stages {
        stage('Branch name') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
        stage('Docker Build'){
            steps{
                pwsh(script: 'docker images -a')
                pwsh(script: """
                    cd binomialoptionspricing/
                    docker images -a
                    docker built -t jenkins-pipeline
                    docker images -a
                    cd ..
                """)
            }
        }
    }
}