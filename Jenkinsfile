pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/vanessakovalsky/python-api-handle-it']]])
            }
        }
        stage('Build') {
            steps {
                git url: 'https://github.com/vanessakovalsky/python-api-handle-it'
                sh 'python3 app/main.py'
            }
        }
        stage('Test') {
            steps {
                echo "tested"
            }
        }
    }
}