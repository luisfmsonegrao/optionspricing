pipeline {
    agent any

    stages {
        stage{'Hello World'}{
            steps {
                echo "Hello Universe"
            }
        }
        stage('Branch name') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
    }
}