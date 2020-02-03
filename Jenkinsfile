node {
    checkout scm
    docker.withRegistry('https://registry.hub.docker.com/', 'dockerhub'){
        def dockerfile = 'Dockerfile'
        def customImage = docker.build("gschatzman/autoloancalculator-windows:1.${env.BUILD_ID}", "-f ${dockerfile} .")
        def dfile = 'Dockerfile'
        def linuxImage = docker.build("gschatzman/autoloancalculator-linux:1.${env.BUILD_ID}", "-f ${dfile} .")

        customImage.push()
        linuxImage.push()
    }
}