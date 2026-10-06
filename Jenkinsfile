pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ehtashamraja44/ml-project.git'
            }
        }

        stage('Create Python Environment') {
            steps {
                sh 'python3 -m venv .dk'
            }
        }

        stage('Install Requirements') {
            steps {
                sh '.dk/bin/pip install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh '.dk/bin/python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t docker-flask-app:latest .'
            }
        }
    }
}