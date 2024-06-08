pipeline {
    agent { label 'gptnode' }

    environment {
        GIT_CREDENTIALS_ID = '123' // Replaced with your actual credentials ID
    }

    stages {
        stage('SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/Abhinav-36/Webserver_Dockerfile_Gpt.git'
            }
        }
        stage('Making docker file') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python *.py'
            }
        }
        stage('Docker file to SCM') {
            steps {
                script {
                    // Cloning the target repository
                    sh 'rm -rf ./Gpt*'
                    sh 'git clone https://github.com/Abhinav-36/Gpt_Dockerfile.git'
                    
                    // Copying files
                    sh 'cp Dockerfile Gpt_Dockerfile'
                    
                    // Changing to the repository directory
                    dir('Gpt_Dockerfile') {
                        // Configuring git to use the credentials
                        sh 'git config user.name "Abhinav-36"'
                        sh 'git config user.email "vabhinav991222@gmail.com"' // Use your email or a placeholder

                        // Adding files and committing
                        sh 'git add .'
                        sh 'git commit -m "Dockerfile from Gpt node"'
                        
                        // Pushing changes
                        withCredentials([gitUsernamePassword(credentialsId: '123', gitToolName: 'Default')]) {
    // some block
                            sh 'git push'
                        }
                    }
                }
                
            }
            
        }
        stage('Dockerimage'){
            agent{label 'imagenode'}
            steps{
                git branch: 'main', url: 'https://github.com/Abhinav-36/Gpt_Dockerfile.git'
                sh 'sudo podman build . -t webserver'
                sh 'sudo podman tag  webserver abhinav36/webserver:${BUILD_NUMBER}'
                withCredentials([usernamePassword(credentialsId: '429469c5-0096-48d5-9776-35864efd9314', passwordVariable: 'docker_pass', usernameVariable: 'docker_username')]) {
    // some block
                        sh 'sudo podman login docker.io -u $docker_username -p $docker_pass'
                }
                sh 'sudo podman push abhinav36/webserver:${BUILD_NUMBER}'
            
            }
        }
        stage('Webserver Launching'){
            agent {label 'servernode'}
            steps{
                sh 'sudo docker run -dit -p 8080:80  abhinav36/webserver:${BUILD_NUMBER}'
            }
            
            
            
        }
    }
}
