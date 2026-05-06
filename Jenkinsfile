pipeline {
    agent any

    stages {
        stage('Clone/Pull Repository') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest -v'
            }
        }
    }
}