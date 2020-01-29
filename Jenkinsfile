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
        echo 'https://github.com/Capstone-Galen/AutoLoanApp reached'
      }
    }

    stage('Build Executable') {
      steps {
        sh 'pyinstaller LoanApp.py'
      }
    }

    stage('Clean Workspace on complete') {
      steps {
        cleanWs(cleanWhenFailure: true, cleanWhenAborted: true, cleanWhenNotBuilt: true)
      }
    }

  }
}