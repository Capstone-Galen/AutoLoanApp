pipeline {
  agent {
    docker {
      image 'cdrx/pyinstaller-windows:python3'
    }

  }
  stages {
    stage('Retrieve Repository') {
      steps {
        git(url: 'https://github.com/Capstone-Galen/AutoLoanApp', branch: 'master')
        echo 'https://github.com/Capstone-Galen/AutoLoanApp reached'
      }
    }

    stage('Build Executable') {
      agent {
        docker {
          image 'cdrx/pyinstaller-windows'
        }

      }
      steps {
        sh 'pyinstaller LoanApp.py'
      }
    }

  }
}