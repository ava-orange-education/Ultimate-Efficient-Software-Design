pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Add build commands here
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add test commands here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add deployment commands here
            }
        }
    }
    post {
        always {
            slackSend (channel: '#build-notifications', message: "Build ${currentBuild.fullDisplayName} finished with status: ${currentBuild.currentResult}")
        }
    }
}
