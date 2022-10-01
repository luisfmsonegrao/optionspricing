pipeline {
    agent any

    stages {
        stage('Branch name') {
            steps {
                echo '$GIT_BRANCH'
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Goodbye') {
            steps {
                echo 'Goodbye World'
            }
        }
    }
}