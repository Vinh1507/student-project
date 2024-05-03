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
                    echo 'Clone code from branch create-ansible-cd (trigger v4)'
                    // Clone code from a specific branch
                    git branch: 'create-ansible-cd', url: 'https://github.com/Vinh1507/student-project'
                }
            }
        }
        stage('Get Tag Version') {
            steps {
                script {
                    def tagVersion = sh(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
                    echo "Tag version: ${tagVersion}"
                    TAG_NAME = tagVersion
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
        stage('Execute Ansible Playbook') {
            steps {
                ansiblePlaybook credentialsId: 'ansible-private-key', disableHostKeyChecking: true, installation: 'ansible2', inventory: './ansible/inventory.yml', playbook: './ansible/playbooks/ansible.yml', vaultTmpPath: ''
            }
        }
    }
}
