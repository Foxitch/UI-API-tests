pipeline {
    agent any

    stages {
        stage('Run tests') {
            steps {
                sh """
                    pip install -r ./requirements.txt
                    ./run_tests.sh ./litecart/web_ui/tests
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