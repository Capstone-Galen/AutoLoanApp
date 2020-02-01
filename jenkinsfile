pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stage('Prepare') {
        steps {
            ws('/var/jenkins_home/workspace/AutoLoanCalculator@~/Capstone/AutLoanApp/src')
            sh 'echo pwd'
        }
    }
    stage('Produce Build') { 
            agent {
                any
            }
            steps {
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
