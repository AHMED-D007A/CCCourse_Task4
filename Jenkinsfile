pipeline {
    agent any

    stages {
        stage('Clone/Pull Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/AHMED-D007A/CCCourse_Task4.git']]
                ])
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest -v'
            }
        }
    }
}