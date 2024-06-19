pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('1f6db55a-8b60-4ab1-81df-b5e28ebae8fc')
        NVDAPIKEY = credentials('ed62b912-6db4-4d3a-a445-a1799077253e')
        SCANNER_HOME = tool 'sonar-scanner'
        DOCKERHUB_USERNAME = 'shittuay'
        DEPLOYMENT_NAME = 'profile_page'
        IMAGE_TAG = "v.0.${env.BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/${DEPLOYMENT_NAME}:${IMAGE_TAG}"
        NAMESPACE = 'profile_page'
        BRANCH_NAME = "${GIT_BRANCH.split('/')[1]}"
    }

    stages {
        stage('Clean workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/shittuay/profile_page.git']]])
            }
        }
        stage('Sonarqube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('sonar-server') {
                        sh "$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=profile_page -Dsonar.projectName=profile_page"
                    }
                }
            }
        }
        // stage('Quality Gate') {
        //     steps {
        //         script {
        //             withSonarQubeEnv('sonar-server') {
        //                 waitForQualityGate abortPipeline: false, credentialsId: 'sonar-token'
        //             }
        //         }
        //     }
        // }
        // stage('Pytest') {
        //     steps {
        //         script {
        //             sh "python3 -m venv venv"
        //             sh "source venv/bin/activate"
        //             sh "pip install -r requirements.txt --no-cache-dir"
        //             sh "pip install pytest pytest-flask"
        //             sh "pytest"
        //         }
        //     }
        // }
        stage('OWASP') {
            steps {
                dependencyCheck additionalArguments: "--scan ./ --disableYarnAudit --disableNodeAudit --nvdApiKey ${NVDAPIKEY}", odcInstallation: 'DP-Check'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
        stage('Trivy FS Scan') {
            steps {
                script {
                    sh "trivy fs ."
                }
            }
        }
        stage("Login to DockerHub") {
            steps {
                script {
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    echo "Login Successful"
                }
            }
        }
        stage("Docker Build") {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                    echo "Image built successfully"
                }
            }
        }
        stage("Trivy Image Scan") {
            steps {
                script {
                    sh "trivy image ${IMAGE_NAME}"
                }
            }
        }
        stage("Docker Push") {
            steps {
                script {
                    sh "docker push ${IMAGE_NAME}"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'shittuay-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'kubectl --kubeconfig=$KUBECONFIG apply -f k8s/deployment.yaml'
                    sh 'kubectl --kubeconfig=$KUBECONFIG apply -f k8s/service.yaml'
                }
            }
        }
    }
    post {
        success {
            slackSend channel: '#alerts', color: 'good', message: "${currentBuild.currentResult}: \nJOB_NAME: ${env.JOB_NAME} \nBUILD_NUMBER: ${env.BUILD_NUMBER} \nBRANCH_NAME: ${env.BRANCH_NAME}. \n More Info ${env.BUILD_URL}"
        }
        failure {
            slackSend channel: '#alerts', color: 'danger', message: "${currentBuild.currentResult}: \nJOB_NAME: ${env.JOB_NAME} \nBUILD_NUMBER: ${env.BUILD_NUMBER} \nBRANCH_NAME: ${env.BRANCH_NAME}. \n More Info ${env.BUILD_URL}"
        }
        always {
            cleanWs()
        }
    }
}
