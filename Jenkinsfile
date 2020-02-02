node {
    checkout scm
    docker.withRegistry('https://registry.hub.docker.com/', 'dockerhub'){
        def dockerfile = 'Dockerfile'
        def customImage = docker.build("gschatzman/loanappwindows:1.${env.BUILD_ID}", "-f ${dockerfile} .")
    }
}