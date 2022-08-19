pipeline {
    agent any
    stages {
        stage('Run tests') {
            
            steps {
                sh """
                    sudo apt update && sudo apt install python3.10-venv
                    python3.10 -m venv tests_env
                    . tests_env/bin/activate
                    pip install -r ./litecart/requirements.txt
                    pip install -r ./petstore/requirements.txt
                    ./run_ui_tests.sh ./litecart/web_ui/tests/
                    ./run_api_tests.sh ./petstore/api/tests/
                """

                script {
                    allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}