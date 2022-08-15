pipeline {

    stages {
        stage('Run tests') {
            steps {
                sh """
                    pip install -r ./requirements.txt
                    ./run_tests.sh
                    cp reports/* ${WORKSPACE}
                """
            }
        }
    }

    post {
        always {
            cleanWs()
            dir("${env.WORKSPACE}@tmp") {
                deleteDir()
            }
        }
    }
}