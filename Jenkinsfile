pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = 'dockerhub_vinhbh'
        IMAGE_NAME = 'vinhbh/student-api-django'
        DJANGO_NGINX_DOCKERFILE_PATH = './ansible/roles/web_servers/files/student-django'
        DJANGO_NGINX_DOCKER_COMPOSE_FILE_PATH = './ansible/roles/web_servers/files/django-nginx/docker-compose.yml'
    }
    stages {
        stage('Clone') {
            steps {
                script {
                    echo "Clone code from branch ${env.BRANCH_NAME}"
                    git branch: env.BRANCH_NAME, url: 'https://github.com/Vinh1507/student-project'
                }
                script {
                    def tagVersion = sh(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
                    env.TAG_NAME = tagVersion
                    echo "Tag version: ${env.TAG_NAME}"
                }
            }
        }
        stage('Build Image') {
            steps {
                script {
                    // docker.build('vinhbh/simple_image_jenkins:lastest', '.')
                    echo "Image version: ${env.IMAGE_NAME}:${env.TAG_NAME}"
                    sh "docker build -t ${env.IMAGE_NAME}:${env.TAG_NAME} ${DJANGO_NGINX_DOCKERFILE_PATH}"
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
        stage('Deploy web server') {
            steps {
                ansiblePlaybook credentialsId: 'ansible-private-key', 
                disableHostKeyChecking: true, 
                installation: 'ansible2', 
                inventory: './ansible/inventory.yml', 
                playbook: './ansible/playbooks/ansible.yml', 
                vaultTmpPath: '',
                extras: "-t api_server -e DJANGO_IMAGE_VERSION=${env.TAG_NAME}"
            }
        }
    }
}
