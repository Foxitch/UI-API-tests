pipeline {
    agent any
    stages {
        stage('Run tests') {
            
            steps {
                sh """
                    sudo apt update && sudo apt install python3.10-venv
                    python3.10 -m venv functional_tests_env
                    . functional_tests_env/bin/activate
                    pip install -r ./litecart/requirements.txt
                    pip install -r ./petstore/requirements.txt
                    ./run_tests.sh ./litecart/web_ui/tests/ ./petstore/api/tests/
                    zip -r tests-result.zip /allure-results
                """               

                script {
                    allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: '/allure-results']]
                    ])
                }
            }
        }
    }
}