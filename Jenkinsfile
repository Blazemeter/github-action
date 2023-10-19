pipeline {
    agent {
        docker {
            registryUrl 'https://us-docker.pkg.dev'
            image 'verdant-bulwark-278/bzm-plugin-base-image/bzm-plugin-base-image:latest'
            registryCredentialsId 'push-to-gar-enc'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock -v $WORKSPACE:/build'
        }
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: "10"))
        ansiColor('xterm')
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Create Release') {
            environment {
                github_token = credentials('github_release_token')
            }
            steps {
                script {
                    sh'''
                    rversion=$(cat /build/versionToRelease.ini | awk '{print $3}')
                    python /build/release-to-github.py ${github_token} ${rversion}
                    '''
                }
            }
        }
        stage('Publish Release') {
            steps {
                script {
                    sh 'echo "Coming soon..."'
                }
            }
        }
    }
}
