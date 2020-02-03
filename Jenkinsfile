node {
    checkout scm
    docker.withRegistry('https://registry.hub.docker.com/', 'dockerhub'){
        def dockerfile = 'Dockerfile'
        def customImage = docker.build("gschatzman/alc-windows:1.${env.BUILD_ID}", "-f ${dockerfile} .")
        def dfile = 'Dfilelinux'
        def linuxImage = docker.build("gschatzman/alc-linux:1.${env.BUILD_ID}", "-f ${dfile} .")
        customImage.push()
        linuxImage.push()
    }
}