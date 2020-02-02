pipeline {
    agent any
        stage('Push to Docker Hub'){
            steps{
                checkout scm

                docker.withRegistry('https://https://registry.hub.docker.com/', 'dockerhub') {

                def customImage = docker.build("gschatzman/autoloancalculatorlinux:${env.BUILD_ID}")

                /* Push the container to the custom Registry */
                customImage.push()
                }
        }
    }
