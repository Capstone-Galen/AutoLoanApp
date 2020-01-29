pipeline {
  agent {
    docker {
      image 'cdrx/pyinstaller-windows'
    }

  }
  stages {
    stage('Retrieve Repository') {
      steps {
        git(url: 'https://github.com/Capstone-Galen/AutoLoanApp', branch: 'master')
      }
    }

    stage('Build Executable') {
      steps {
        sh 'pyinstaller LoanApp.py'
      }
    }

  }
}