pipeline {
    agent any
    
    stages {
        stage('Checkout1') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/vanessakovalsky/python-api-handle-it']]])
            }
        }
        stage('Build1') {
            steps {
                git url: 'https://github.com/vanessakovalsky/python-api-handle-it'
                sh 'python3 app/main.py'
            }
        }
        stage('Test1') {
            steps {
                echo "tested"
            }
        }
    }
}