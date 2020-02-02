node {
    checkout scm
    docker.withRegistry('https://registry.hub.docker.com/', 'dockerhub'){
        def dockerfile = 'Dockerfile'
        def customImage = docker.build("gschatzman/autoloancalculator-linux:${env.BUILD_ID}", "-f${dockerfile} .")
    }
}