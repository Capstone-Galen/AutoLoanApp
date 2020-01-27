pipeline {
  agent none {
  stages {
    stage('Build Distributable') {
      docker {
      image 'cdrx/pyinstaller-windows:python3'
      }
    }
      steps {
        echo 'Initial Pipeline started. Building with Pyinstaller'
        sh 'pyinstaller --onefile -w icon=icons8carbadge.ico LoanApp.py'
      }
      post{
        success{
          archiveArtifacts 'dist/LoanApp'
    }

  }
}
  
}
