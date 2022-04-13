def alljob = JOB_NAME.tokenize('/') as String[]
def proj_name = alljob[1] //to capture a simple pipeline project name inside a manually created folder

def pushImage(image){
  image.push()
  image.push(env.BRANCH_NAME.replace("/", "_") + '_' + BUILD_ID)
  image.push(env.BRANCH_NAME.replace("/", "_"))
}

pipeline {
  environment {
    registry = "docker.somko.be"
    registryCredential = 'docker-jenkins'
  }
  agent any
  stages {
    stage('Build image') {
      steps {
        script {
          docker.withRegistry("https://" + registry, registryCredential) {
            pushImage(docker.build(proj_name.replace('-', '_') + "/odoo", '--pull .'))
          }
        }
      }
    }
  }
}
