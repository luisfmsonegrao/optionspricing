pipeline {
    agent any

    stages {
        stage{'Hello World'}{
            steps {
                echo "Hello World Hello World Hello World" 
                 
            }
        }
        stage('Branch name') {
            steps {
                echo "$GIT_BRANCH"
            }
        }
    }
}