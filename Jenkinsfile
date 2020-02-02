pipeline {
    agent{any}
    stages {
        stage('Push to DockerHub'){
            steps{
                checkout scm

                docker.withRegistry('https://registry.hub.docker.com/', 'dockerhub') {
                    def customImage = docker.build("gschatzman/autoloancalculatorlinux:${env.BUILD_ID}")

                    customImage.push()
                }
            }
        }
    }    
}