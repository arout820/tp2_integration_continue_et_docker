// pipeline {
//     agent any
    
//     stages {
//         stage('Checkout1') {
//             steps {
//                 checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/vanessakovalsky/python-api-handle-it']]])
//             }
//         }
//         stage('Build1') {
//             steps {
//                 git url: 'https://github.com/vanessakovalsky/python-api-handle-it'
//                 sh 'python3 app/main.py'
//             }
//         }
//         stage('Test1') {
//             steps {
//                 echo "tested"
//             }
//         }
//     }
// }

pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
    steps {
        // Récupération du code depuis le dépôt Git
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], 
                  userRemoteConfigs: [[url: 'https://github.com/vanessakovalsky/python-api-handle-it.git']]])
    }
        }
        
        stage('Lint and Radon') {
            steps {
                // Construction de l'image pour les tests de lint et radon
                script {
                    docker.build('lint-radon', '-f docker-test/pylint/Dockerfile .')
                }
                
                // Exécution des tests de lint et radon
                script {
                    docker.image('lint-radon').inside {
                        sh 'lint-command' // Remplacer par la commande de lint
                        sh 'radon-command' // Remplacer par la commande de radon
                    }
                }
            }
        }
        
        stage('Unit Tests') {
            steps {
                // Construction de l'image pour les tests unitaires
                script {
                    docker.build('unittests', '-f docker-test/unittest/Dockerfile .')
                }
                
                // Exécution des tests unitaires
                script {
                    docker.image('unittests').inside {
                        sh 'python -m unittest discover -s app/test/unit -p "*_test.py"'
                    }
                }
            }
        }
        
        stage('Docker Build and Push') {
            steps {
                // Construction de l'image Docker de l'application
                script {
                    docker.build('my-python-app', '-f docker-app/python/Dockerfile .')
                }
                
                // Connexion à Docker Hub et poussée de l'image
                script {
                    withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_HUB_CREDENTIALS')]) {
                        sh 'docker login -u username -p $DOCKER_HUB_CREDENTIALS'
                        sh 'docker push my-python-app:latest'
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Nettoyage des images temporaires
            script {
                docker.image('lint-radon').withRun { c -> }
                docker.image('unittests').withRun { c -> }
            }
        }
    }
}
