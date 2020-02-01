pipeline {
    agent none
    
    stages {

        stage('Show Python Version'){
            agent {docker {image 'python:3.5.1'}}
            steps{
                sh 'python --version'
            }
        }
        stage('Prepare Workspace') {
            steps{
                ws('/var/jenkins_home/workspace/AutoLoanCalculator@~/Capstone/AutLoanApp/src')
                sh 'echo pwd “$(pwd):/src/”'
            }
        }
        stage('Produce Build'){
            agent { docker {}
            
                steps{
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
}