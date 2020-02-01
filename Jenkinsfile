pipeline {
    agent any
    stages {

        stage('Show Python Version'){
            agent {docker {image 'python:3.5.1'}}
            steps{
                sh 'python --version'
            }
        }
        stage('Prepare Workspace') {
            steps{
                sh 'echo pwd “    $(pwd):/src/”'
            }
        }
        stage('Produce Build'){
            agent {docker{image 'python:3.5.1'}}
            
                steps{
                    sh 'pwd'
                    sh 'pyinstaller --onefile --windowed --icon=icons8carbadge.ico LoanApp.py'
                }
                post {
                    success {
                        archiveArtifacts 'dist/LoanApp.exe'
                    }
                }  
        }
    }
}