
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Freeze dependencies') {
            steps {
                sh 'cd employee-api && python3 -m pip freeze > requirements.txt'
            }
        }

        stage('Build versioned package') {
            steps {
                sh 'zip -j employee-api-build-${BUILD_NUMBER}.zip employee-api/main.py employee-api/requirements.txt'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'employee-api-build-*.zip', fingerprint: true
            }
        }
    }
}
