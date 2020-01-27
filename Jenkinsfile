pipeline {
  agent docker {image 'cdrx/pyinstaller-windows:python3'}
  stages {
    stage('Build Distributable') {
      
    }
      steps {
        echo 'Initial Pipeline started. Building with Pyinstaller'
        sh 'pyinstaller LoanApp.py'
      }
      post{
        success{
          archiveArtifacts 'dist/LoanApp'
    }

  }
}
  }
