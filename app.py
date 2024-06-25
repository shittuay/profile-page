from flask import Flask, render_template, jsonify
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import logging
import requests

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your NewsAPI key
API_KEY = os.getenv('NEWS_API_KEY')
if not API_KEY:
    raise ValueError("No NEWS_API_KEY found in environment variables. Please add it to your .env file.")

# Create a custom session to disable SSL verification
session = requests.Session()
session.verify = False

newsapi = NewsApiClient(api_key=API_KEY, session=session)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['NEWS_API_KEY'] = os.getenv('NEWS_API_KEY', 'default_api_key')


PROFILE = {
    'name': 'Abiola Shittu',
    'bio': 'Abiola Shittu is an experienced Cloud Engineer with over 10 years of expertise in information technology. Throughout his career, he has worked extensively with key DevOps tools to facilitate seamless web application deployments, showcasing his proficiency in cloud infrastructure and deployment automation. His dedication and technical skills have made him a valuable asset in the IT field.',
    'email': 'abiola.shiba@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/abiola-shittu/',
    'github': 'https://github.com/shittuay',
    'resume': 'images/Docs/resume.docx',
    'picture': 'images/Abiola.jpeg',
    'profile': 'images/Docs/Profile.pdf'
}

ACCOMPLISHMENTS = [
    {'title': 'Project 1', 'description': 'Deployed a web application project on AWS Cloud using Terraform and Jenkins'},
    {'title': 'Project 2', 'description': 'Automated IAM key rotation using AWS Lambda and CloudWatch Events'},
    {'title': 'Project 3', 'description': 'Created bulk EC2 instances using Terraform'},
    {'title': 'Project 4', 'description': 'Set up a VPC with public and private subnets using CloudFormation'},
    {'title': 'Project 5', 'description': 'Monitored AWS resources for security compliance using AWS Security Hub'},
    {'title': 'Project 6', 'description': 'Created a MySQL database on AWS RDS and connected it to an EC2 instance using Terraform'},
    {'title': 'Project 7', 'description': 'Led multiple migration projects from on-premises to AWS Cloud using AWS Server Migration Service'},
    {'title': 'Project 8', 'description': 'Implemented Control Tower and landing zone using AWS Organizations and Service Catalog'},
    {'title': 'Project 9', 'description': 'Configured auto-scaling, target groups, and load balancers using Terraform and attached a WAF to the load balancer'},
    {'title': 'Project 10', 'description': 'Executed a blue-green deployment using AWS ECS and CodeCommit, CodeDeploy, and CodePipeline'},
    {'title': 'Project 11', 'description': 'Deployed a Python-Flask web application on a Kubernetes cluster using Helm and Kustomize'},
    {'title': 'Project 12', 'description': 'Developed a CI/CD pipeline using Jenkins, SonarQube, Nexus, and GitHub'},
    {'title': 'Project 13', 'description': 'Created an S3 bucket and enabled versioning and lifecycle policy using Terraform'},
    {'title': 'Award', 'description': 'AWS Cloud Practitioner Certification'},
    {'title': 'Award', 'description': 'AWS Cloud Quest Certification'},
    {'title': 'Award', 'description': 'AWS DevOps Engineer Certification'},
    {'title': 'Award', 'description': 'ITIL Foundation Certification'},
]

BLOG_POSTS = [
    {
        'title': 'The Importance of Cloud Technology with the Addition of AI',
        'content': '''
            <p>The integration of Artificial Intelligence (AI) into cloud technology is transforming the landscape of IT and business operations. Cloud technology has already revolutionized the way organizations manage and deploy their applications, providing scalable, flexible, and cost-effective solutions. With the addition of AI, the cloud environment is set to become even more powerful and efficient.</p>

            <p>AI enhances cloud technology by offering advanced data analytics, machine learning, and automation capabilities. This integration allows for more intelligent data processing, improved decision-making, and streamlined operations. For instance, AI-powered analytics can process vast amounts of data quickly, providing insights that were previously unattainable.</p>

            <p>Moreover, AI-driven automation in the cloud can optimize resource management, reduce operational costs, and improve service delivery. Tasks that used to require manual intervention can now be automated, leading to increased efficiency and reduced risk of human error.</p>

            <p>The combination of AI and cloud technology also supports the development and deployment of intelligent applications. These applications can learn from user interactions, adapt to changing environments, and provide personalized experiences. This capability is particularly beneficial in industries such as healthcare, finance, and retail, where real-time data analysis and adaptive responses are crucial.</p>

            <p>In summary, the addition of AI to cloud technology is set to transform the cloud environment by enhancing data analytics, automation, and the development of intelligent applications. This transformation promises to drive innovation, improve operational efficiency, and deliver better user experiences across various industries.</p>
        '''
    },
    {
        'title': 'Harnessing the Power of Kubernetes for Deployments',
        'content': '''
            <p>Kubernetes has become a cornerstone in modern application deployments due to its powerful orchestration capabilities and ability to manage containerized applications at scale. It automates deployment, scaling, and operations of application containers across clusters of hosts, providing a resilient and efficient system.</p>

            <p>One of the key benefits of using Kubernetes is its ability to provide a consistent and reproducible deployment environment. This ensures that applications run the same way in development, testing, and production environments, reducing the risk of environment-related issues.</p>

            <p>Users can take full advantage of Kubernetes by integrating it with various DevOps tools to create a robust tech stack. Tools such as Jenkins for CI/CD, Prometheus for monitoring, and Helm for package management work seamlessly with Kubernetes to enhance its capabilities. Jenkins pipelines can automate the build, test, and deployment process, ensuring that new code changes are continuously integrated and deployed with minimal human intervention.</p>

            <p>Prometheus, combined with Grafana, provides powerful monitoring and visualization, allowing users to gain insights into their applications and infrastructure. This helps in proactively identifying and resolving issues before they impact end users.</p>

            <p>Helm simplifies the deployment of complex applications by using Helm charts, which are packages of pre-configured Kubernetes resources. This makes it easier to deploy and manage applications on Kubernetes clusters, saving time and reducing complexity.</p>

            <p>By leveraging Kubernetes alongside these DevOps tools, users can build a tech stack that is not only powerful and scalable but also resilient and future-proof. This combination supports rapid development cycles, improved reliability, and efficient operations, ensuring that the tech stack can withstand the test of time.</p>

            <p>In summary, Kubernetes, when used with complementary DevOps tools, provides a robust foundation for modern application deployments. Its ability to automate and manage containerized applications, combined with the power of CI/CD, monitoring, and package management tools, enables organizations to build a resilient and enduring tech stack.</p>
        '''
    },
    {
        'title': 'Deploying a Flask App on Render',
        'content': '''
            <h3>Steps to Deploy a Flask App on Render</h3>
            <ol>
                <li>
                    <strong>Create a Render Account:</strong>
                    <p>Sign up for a free account on <a href="https://render.com/">Render</a>.</p>
                </li>
                <li>
                    <strong>Prepare Your Flask App for Deployment:</strong>
                    <p>Ensure your Flask app is structured properly. Your project directory should include all necessary files and dependencies.</p>
                    <p>Create a <code>requirements.txt</code> file to list all the Python dependencies. You can generate this file by running:</p>
                    <pre><code>pip freeze > requirements.txt</code></pre>
                    <p>Create a <code>Procfile</code> to specify the command to run your application. The <code>Procfile</code> should contain:</p>
                    <pre><code>web: gunicorn app:app</code></pre>
                    <p>Replace <code>app</code> with the name of your main Python file, without the <code>.py</code> extension.</p>
                </li>
                <li>
                    <strong>Initialize a Git Repository:</strong>
                    <p>If you haven't already, initialize a Git repository in your project directory:</p>
                    <pre><code>git init</code></pre>
                    <p>Commit your files:</p>
                    <pre><code>git add .\ngit commit -m "Initial commit"</code></pre>
                </li>
                <li>
                    <strong>Push Your Code to GitHub:</strong>
                    <p>Create a new repository on GitHub and push your local repository to GitHub:</p>
                    <pre><code>git remote add origin https://github.com/yourusername/your-repo-name.git\ngit branch -M main\ngit push -u origin main</code></pre>
                </li>
                <li>
                    <strong>Create a New Web Service on Render:</strong>
                    <p>Log in to your Render account.</p>
                    <p>Click on the "New" button and select "Web Service".</p>
                    <p>Connect your GitHub account and select the repository you want to deploy.</p>
                    <p>Render will automatically detect the Flask app. Configure the following settings:</p>
                    <ul>
                        <li><strong>Environment:</strong> Python 3</li>
                        <li><strong>Build Command:</strong> (Render will use the default <code>pip install -r requirements.txt</code>)</li>
                        <li><strong>Start Command:</strong> <code>gunicorn app:app</code> (Replace <code>app</code> with your main Python file name)</li>
                    </ul>
                </li>
                <li>
                    <strong>Deploy Your App:</strong>
                    <p>Click "Create Web Service".</p>
                    <p>Render will start the deployment process, which includes building the environment, installing dependencies, and starting your Flask app.</p>
                    <p>Once the deployment is complete, Render will provide you with a URL to access your live Flask app.</p>
                </li>
            </ol>
            <h3>Summary</h3>
            <p>Deploying a Flask app on Render is a user-friendly process, ideal for developers working on projects like a profile page website with Python, HTML, and CSS. Render takes care of the infrastructure, allowing you to focus on building your application without worrying about server management. The integration with GitHub makes it easy to update your app by simply pushing new commits to your repository.</p>
        '''
    },
    
    {
    'title': 'Securing Secrets in Deployment with .env Files and .gitignore',
    'content': '''
        <p>In today's software development landscape, securing sensitive information such as API keys, database credentials, and other secrets is paramount. One of the most effective ways to manage and protect these secrets is by using .env files in combination with .gitignore. This approach ensures that sensitive information is not exposed in your version control system, thereby mitigating the risk of accidental leaks.</p>

        <p><strong>What is a .env File?</strong></p>
        <p>A .env file is a simple text file used to store environment variables. These variables can be loaded into your application at runtime, allowing you to configure your app without hardcoding sensitive information directly into your source code.</p>

        <p><strong>Example .env File</strong></p>
        <pre><code>API_KEY=your_api_key_here
DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
SECRET_KEY=supersecretkey</code></pre>

        <p><strong>Using .gitignore to Protect Your .env File</strong></p>
        <p>The .gitignore file is a special file that tells Git which files or directories to ignore in a project. By adding your .env file to .gitignore, you ensure that it is not tracked by Git, thus keeping your sensitive information out of your version control system.</p>

        <p><strong>Example .gitignore File</strong></p>
        <pre><code># Ignore the .env file
.env</code></pre>

        <p><strong>Setting Up Your Project</strong></p>

        <p><strong>1. Create Your .env File</strong></p>
        <p>Create a .env file in the root of your project directory and add your environment variables to it.</p>
        <pre><code>API_KEY=your_api_key_here
DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
SECRET_KEY=supersecretkey</code></pre>

        <p><strong>2. Update Your .gitignore File</strong></p>
        <p>Ensure your .gitignore file contains an entry to ignore the .env file.</p>
        <pre><code># Ignore the .env file
.env</code></pre>

        <p><strong>3. Load Environment Variables in Your Application</strong></p>
        <p>In your application code, use a library like python-dotenv to load environment variables from your .env file. Here’s an example in a Python Flask application:</p>

        <p><strong>Install python-dotenv</strong></p>
        <pre><code>pip install python-dotenv</code></pre>

        <p><strong>Update app.py</strong></p>
        <pre><code>from flask import Flask, render_template
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the API key from the environment variables
api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("No API_KEY set for Flask application")

newsapi = NewsApiClient(api_key=api_key)

@app.route("/tech-news")
def tech_news():
    top_headlines = newsapi.get_top_headlines(category='technology')
    articles = top_headlines.get('articles', [])
    return render_template('news.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)</code></pre>

        <p><strong>Deploying to Production</strong></p>
        <p>When deploying to a production environment, you can securely provide your environment variables directly to the environment where your application runs. For example, in a Kubernetes deployment, you can use Kubernetes Secrets to manage and inject sensitive information.</p>

        <p><strong>Example Kubernetes Secret</strong></p>
        <pre><code>apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  API_KEY: base64_encoded_api_key_here</code></pre>

        <p><strong>Using the Secret in a Deployment</strong></p>
        <pre><code>apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app-image
        env:
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: API_KEY</code></pre>

        <p><strong>Conclusion</strong></p>
        <p>Using .env files and .gitignore is a simple yet powerful way to manage and protect your secrets during development. By ensuring that sensitive information is not exposed in your version control system, you can reduce the risk of accidental leaks and enhance the security of your applications. When moving to production, consider using more robust secret management solutions like Kubernetes Secrets to securely manage your environment variables.</p>
    '''
},
{
    'title': 'Hosting Your Own Kubernetes (K8s) Cluster Locally with NVIDIA GPU, 2TB Storage, and 64/128GB Memory',
    'content': '''
        <h3>Introduction</h3>
        <p>Setting up a Kubernetes (K8s) cluster locally can provide a robust environment for testing and deploying applications, especially when equipped with powerful hardware such as an NVIDIA GPU, 2TB storage, and 64/128GB memory. This guide will walk you through the process of setting up your K8s cluster, installing necessary tools, configuring port forwarding on your home WiFi, and leveraging Cloudflare's free services for hosting web applications.</p>

        <h3>Hardware Requirements</h3>
        <ul>
            <li><strong>NVIDIA GPU:</strong> Ideal for workloads requiring intensive computational power such as machine learning or AI applications.</li>
            <li><strong>Storage:</strong> 2TB SSD/HDD to handle large datasets and provide ample storage for applications.</li>
            <li><strong>Memory:</strong> 64GB or 128GB RAM to ensure smooth operation of multiple pods and services.</li>
        </ul>

        <h3>Software Requirements</h3>
        <ul>
            <li><strong>Operating System:</strong> Ubuntu 20.04 LTS or a similar Linux distribution.</li>
            <li><strong>Docker:</strong> Container runtime for Kubernetes.</li>
            <li><strong>Kubernetes:</strong> For orchestrating containers.</li>
            <li><strong>kubectl:</strong> Command-line tool for interacting with the Kubernetes cluster.</li>
            <li><strong>k3s:</strong> Lightweight Kubernetes distribution.</li>
            <li><strong>NVIDIA Docker:</strong> To run GPU-accelerated containers.</li>
            <li><strong>Helm:</strong> Kubernetes package manager.</li>
        </ul>

        <h3>Step-by-Step Guide</h3>

        <h4>1. Setting Up Your Environment</h4>
        <p><strong>Install Docker:</strong></p>
        <pre><code>
        sudo apt-get update
        sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
        sudo apt-get update
        sudo apt-get install -y docker-ce
        sudo usermod -aG docker ${USER}
        </code></pre>

        <p><strong>Install NVIDIA Docker:</strong></p>
        <pre><code>
        distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
        curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
        curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
        sudo apt-get update && sudo apt-get install -y nvidia-docker2
        sudo systemctl restart docker
        </code></pre>

        <p><strong>Install k3s:</strong></p>
        <pre><code>
        curl -sfL https://get.k3s.io | sh -
        </code></pre>

        <p><strong>Install kubectl:</strong></p>
        <pre><code>
        sudo snap install kubectl --classic
        </code></pre>

        <p><strong>Install Helm:</strong></p>
        <pre><code>
        curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
        </code></pre>

        <h4>2. Configuring Kubernetes for GPU</h4>
        <p><strong>Install NVIDIA Kubernetes Device Plugin:</strong></p>
        <pre><code>
        kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.9.0/nvidia-device-plugin.yml
        </code></pre>

        <h4>3. Configuring Port Forwarding on Your Home WiFi</h4>
        <p><strong>Access Your Router:</strong> Open a web browser and enter the IP address of your router (typically `192.168.1.1` or `192.168.0.1`).</p>
        <p><strong>Login:</strong> Enter your router's username and password.</p>
        <p><strong>Navigate to Port Forwarding Section:</strong> Usually found under "Advanced" or "Firewall".</p>
        <p><strong>Create a New Port Forwarding Rule:</strong></p>
        <ul>
            <li><strong>Service Name:</strong> Kubernetes</li>
            <li><strong>Protocol:</strong> TCP/UDP</li>
            <li><strong>External Port:</strong> 80, 443 (HTTP, HTTPS)</li>
            <li><strong>Internal IP:</strong> Enter the local IP address of your Kubernetes master node.</li>
            <li><strong>Internal Port:</strong> 80, 443</li>
        </ul>

        <h4>4. Leveraging Cloudflare for Free Hosting</h4>
        <p><strong>Sign Up for Cloudflare:</strong> Go to <a href="https://www.cloudflare.com/">Cloudflare</a> and create a free account.</p>
        <p><strong>Add Your Domain:</strong> Follow the prompts to add your domain and update your DNS settings with the provided Cloudflare nameservers.</p>
        <p><strong>Set Up SSL/TLS:</strong></p>
        <ul>
            <li>Go to the SSL/TLS section in Cloudflare dashboard.</li>
            <li>Choose "Flexible" or "Full" to enable HTTPS.</li>
        </ul>
        <p><strong>Configure DNS:</strong></p>
        <ul>
            <li>Add an A record pointing to your home's external IP address (found via `whatismyip.com`).</li>
            <li>Add a CNAME record for `www` pointing to your domain.</li>
        </ul>

        <p><strong>Install Cloudflare Argo Tunnel:</strong></p>
        <pre><code>
        curl -L https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.deb -o cloudflared.deb
        sudo dpkg -i cloudflared.deb
        cloudflared tunnel login
        </code></pre>

        <p><strong>Create and Run Tunnel:</strong></p>
        <pre><code>
        cloudflared tunnel create my-tunnel
        cloudflared tunnel route dns my-tunnel example.com
        cloudflared tunnel run my-tunnel
        </code></pre>

        <h4>Conclusion</h4>
        <p>By following these steps, you can set up a robust local Kubernetes cluster with powerful hardware, configure it to leverage your home network for external access, and utilize Cloudflare’s free services to host web applications. This setup not only provides a great environment for development and testing but also leverages powerful resources for high-performance applications.</p>
    '''
},
{
        'title': 'Managing Single Sign-On with Temporary Access Keys and Automating Key Rotation with AWS Lambda',
        'content': '''
            <h3>Introduction</h3>
            <p>In the world of cloud computing, securing access to resources is paramount. One common approach is using Single Sign-On (SSO) with temporary access keys. However, for workloads that cannot be terminated if the temporary keys expire, a different strategy is needed to avoid disruptions. In such cases, creating an IAM user with permanent access keys is a viable solution. As a DevOps engineer, it's crucial to implement an automation process to reissue these keys regularly to maintain security and compliance. This post will walk you through how to set up this automation using AWS Lambda, Secrets Manager, and EventBridge.</p>

            <h3>Why Use Single Sign-On with Temporary Access Keys?</h3>
            <p>SSO with temporary access keys is a widely used method for providing secure, time-limited access to AWS resources. It reduces the risk of long-term credentials being compromised since the keys are short-lived and automatically expire. However, some workloads require uninterrupted access and cannot afford the disruption caused by expiring keys.</p>

            <h3>The Challenge of Expiring Keys</h3>
            <p>For workloads that cannot tolerate interruptions, relying solely on temporary keys can be problematic. When these keys expire, the workload loses access until new keys are issued. To avoid this, we can create an IAM user with permanent access keys, ensuring continuous access. However, permanent keys come with their own risks if not managed properly.</p>

            <h3>Solution: Automating Key Rotation</h3>
            <p>To mitigate the risks associated with permanent keys, it is essential to rotate them regularly. AWS Lambda, combined with Secrets Manager and EventBridge, provides a powerful automation framework to achieve this.</p>

            <h3>Step-by-Step Guide</h3>
            <ol>
                <li><strong>Create an IAM User with Permanent Access Keys</strong>
                <p>First, create an IAM user and generate access keys for it. These keys will be used by the workload that requires uninterrupted access.</p>
                </li>
                <li><strong>Store the Keys in AWS Secrets Manager</strong>
                <p>Store the generated access keys in AWS Secrets Manager to keep them secure and easily retrievable. Create a new secret and add the access key ID and secret access key.</p>
                <pre><code>aws secretsmanager create-secret --name myAccessKeys --secret-string '{"AccessKeyId":"AKIA...", "SecretAccessKey":"wJal..."}'</code></pre>
                </li>
                <li><strong>Set Up AWS Lambda Function for Key Rotation</strong>
                <p>Create an AWS Lambda function that will rotate the access keys every three months. The function will generate new keys, update the secret in Secrets Manager, and deactivate the old keys.</p>
                <pre><code>import boto3
import json
from datetime import datetime

iam_client = boto3.client('iam')
secretsmanager_client = boto3.client('secretsmanager')

def rotate_access_keys(event, context):
    user_name = 'your-iam-user-name'
    secret_name = 'myAccessKeys'
    
    # Create new access key
    response = iam_client.create_access_key(UserName=user_name)
    new_access_key = response['AccessKey']
    
    # Update the secret with new access keys
    new_secret_string = json.dumps({
        "AccessKeyId": new_access_key['AccessKeyId'],
        "SecretAccessKey": new_access_key['SecretAccessKey']
    })
    secretsmanager_client.update_secret(SecretId=secret_name, SecretString=new_secret_string)
    
    # List all access keys and delete the oldest one if there are more than two
    response = iam_client.list_access_keys(UserName=user_name)
    access_keys = sorted(response['AccessKeyMetadata'], key=lambda x: x['CreateDate'])
    if len(access_keys) > 2:
        iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_keys[0]['AccessKeyId'])
    
    print(f"Access keys rotated at {datetime.now()}")

# Example event to test the function locally
if __name__ == "__main__":
    rotate_access_keys({}, {})</code></pre>
                </li>
                <li><strong>Deploy the Lambda Function</strong>
                <p>Deploy the Lambda function and configure it to have the necessary IAM roles and permissions to manage IAM users and access keys, as well as Secrets Manager.</p>
                </li>
                <li><strong>Set Up EventBridge to Trigger Lambda Function</strong>
                <p>Use EventBridge (formerly CloudWatch Events) to schedule the Lambda function to run every three months.</p>
                <pre><code>aws events put-rule --schedule-expression "rate(90 days)" --name RotateAccessKeysRule
aws events put-targets --rule RotateAccessKeysRule --targets "Id"="1","Arn"="arn:aws:lambda:region:account-id:function:function-name"</code></pre>
                </li>
            </ol>

            <h3>Conclusion</h3>
            <p>By automating the rotation of IAM user access keys using AWS Lambda, Secrets Manager, and EventBridge, you can ensure your workloads have continuous access to AWS resources without the risk of key expiration. This approach enhances security by regularly updating access keys and minimizes the potential for disruptions in your operations. Implementing this solution demonstrates the proactive measures a DevOps engineer can take to maintain a secure and resilient infrastructure.</p>

            <h3>Further Reading</h3>
            <ul>
                <li><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html">AWS IAM Best Practices</a></li>
                <li><a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html">Using AWS Secrets Manager</a></li>
                <li><a href="https://docs.aws.amazon.com/lambda/latest/dg/welcome.html">AWS Lambda Documentation</a></li>
                <li><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html">Amazon EventBridge Documentation</a></li>
            </ul>

            <p>Feel free to reach out if you have any questions or need further assistance with setting up this automation!</p>
        '''
    }
]

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/profile")
def profile():
    return render_template('profile.html', profile=PROFILE, accomplishments=ACCOMPLISHMENTS)

@app.route("/blog")
def blog():
    return render_template('blog.html', blog_posts=BLOG_POSTS)

@app.route("/tech_news")
def tech_news():
    try:
        top_headlines = newsapi.get_top_headlines(category='technology', country='us')
        articles = top_headlines.get('articles', [])
        if not articles:
            logger.info("No articles found")
        else:
            logger.info(f"Fetched {len(articles)} articles")
        return render_template('tech_news.html', articles=articles)
    except Exception as e:
        logger.error(f"Error fetching tech news: {e}")
        return render_template('tech_news.html', articles=[])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
