pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Show Python Version') {
      agent {
        docker {
          image 'python:3.5.1'
        }

      }
      steps {
        sh 'python --version'
      }
    }

    stage('Prepare Workspace') {
      steps {
        sh 'echo pwd “    $(pwd):/src/”'
      }
    }

    stage('Produce Build') {
      agent {
        docker {
          image 'python:3.5.1'
        }

      }
      post {
        success {
          archiveArtifacts 'dist/LoanApp.exe'
        }

      }
      steps {
        sh 'pwd'
      }
    }

  }
}