pipeline {
    agent none
    
    stages {

        stage('Prepare Workspace') {
            steps{
                ws('/var/jenkins_home/workspace/AutoLoanCalculator@~/Capstone/AutLoanApp/src')
                sh 'echo pwd “$(pwd):/src/”'
            }
        }

        stage('Produce Build'){
            agent {
                any
            }
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