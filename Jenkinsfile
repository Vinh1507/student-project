pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = 'dockerhub_vinhbh'
        IMAGE_NAME = 'vinhbh/student-api-django'
        TAG_NAME = '1.0'
    }
    stages {
        stage('Clone') {
            steps {
                script {
                    echo 'update'
                    // Clone code from a specific branch
                    git branch: 'main', url: 'https://github.com/Vinh1507/student-project'
                }
            }
        }
        stage('Build Image') {
            steps {
                script {
                    // docker.build('vinhbh/simple_image_jenkins:lastest', '.')
                    sh "docker build -t ${env.IMAGE_NAME}:${env.TAG_NAME} ./student-django"
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // Login to Docker Hub
                withCredentials([usernamePassword(credentialsId: 'dockerhub_vinhbh', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                }
                // Push Docker image to Docker Hub
                sh "docker push ${env.IMAGE_NAME}:${env.TAG_NAME}"
            }
        }
    }
}
