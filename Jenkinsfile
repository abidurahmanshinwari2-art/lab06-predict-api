pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/abidurahmanshinwari2-art/lab06-predict-api.git'
                sh 'docker compose down'
                sh 'docker compose up -d'
            }
        }
    }
}
