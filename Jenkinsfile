pipeline {
  agent {
    docker {
      image 'cdrx/pyinstaller-windows'
    }

  }
  stages {
    stage('Produce Build') {
      steps {
        sh 'pyinstaller --onefile --windowed --icon=icons8carbadge.ico LoanApp.py'
      }
    }

  }
}