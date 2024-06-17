from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROFILE = {
    'name': 'Abiola Shittu',
    'bio': 'Abiola Shittu is an experienced Cloud Engineer with over 10 years of expertise in information technology. Throughout his career, he has worked extensively with key DevOps tools to facilitate seamless web application deployments, showcasing his proficiency in cloud infrastructure and deployment automation. His dedication and technical skills have made him a valuable asset in the IT field.',
    'email': 'mailto abiola.shiba@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/abiola-shittu/',
    'github': 'https://github.com/shittuay'
    
}

ACCOMPLISHMENTS = [
    {'title': 'Project 1', 'webapplicatin deployment': 'web-application project deployment on AWS Cloud using Terraform and Jenkins'},
    {'title': 'Project 2', 'python-flask Project': 'Python-flask webapplication deployment on kubernetes cluster using Helm and kustomize'},
    {'title': 'Aws Cloud Practitioner Certification', 'Aws Cloud Proffessional': 'Aws Cloud Practitioner Certification'},
    {'title': 'Aws Cloud Quest Certification', 'Aws Cloud Proffessional': 'Aws Cloud Quest Certification'},
    {'title': 'Aws Devops Engineer Certification', 'Aws Cloud Proffessional': 'Aws Devops Engineer Certification'},
    {'title': 'ITIL Foundation Certification', 'ITSM': 'ITIL Foundation Certification'},
    # Add more accomplishments as needed
]

BLOG_POSTS = [
    {
        'title': 'The Importance of Cloud Technology with the Addition of AI',
        'content': '''
            The integration of Artificial Intelligence (AI) into cloud technology is transforming the landscape of IT and business operations. Cloud technology has already revolutionized the way organizations manage and deploy their applications, providing scalable, flexible, and cost-effective solutions. With the addition of AI, the cloud environment is set to become even more powerful and efficient.

            AI enhances cloud technology by offering advanced data analytics, machine learning, and automation capabilities. This integration allows for more intelligent data processing, improved decision-making, and streamlined operations. For instance, AI-powered analytics can process vast amounts of data quickly, providing insights that were previously unattainable.

            Moreover, AI-driven automation in the cloud can optimize resource management, reduce operational costs, and improve service delivery. Tasks that used to require manual intervention can now be automated, leading to increased efficiency and reduced risk of human error.

            The combination of AI and cloud technology also supports the development and deployment of intelligent applications. These applications can learn from user interactions, adapt to changing environments, and provide personalized experiences. This capability is particularly beneficial in industries such as healthcare, finance, and retail, where real-time data analysis and adaptive responses are crucial.

            In summary, the addition of AI to cloud technology is set to transform the cloud environment by enhancing data analytics, automation, and the development of intelligent applications. This transformation promises to drive innovation, improve operational efficiency, and deliver better user experiences across various industries.
        '''
    },
    {
        'title': 'Harnessing the Power of Kubernetes for Deployments',
        'content': '''
            Kubernetes has become a cornerstone in modern application deployments due to its powerful orchestration capabilities and ability to manage containerized applications at scale. It automates deployment, scaling, and operations of application containers across clusters of hosts, providing a resilient and efficient system.

            One of the key benefits of using Kubernetes is its ability to provide a consistent and reproducible deployment environment. This ensures that applications run the same way in development, testing, and production environments, reducing the risk of environment-related issues.

            Users can take full advantage of Kubernetes by integrating it with various DevOps tools to create a robust tech stack. Tools such as Jenkins for CI/CD, Prometheus for monitoring, and Helm for package management work seamlessly with Kubernetes to enhance its capabilities. Jenkins pipelines can automate the build, test, and deployment process, ensuring that new code changes are continuously integrated and deployed with minimal human intervention.

            Prometheus, combined with Grafana, provides powerful monitoring and visualization, allowing users to gain insights into their applications and infrastructure. This helps in proactively identifying and resolving issues before they impact end users.

            Helm simplifies the deployment of complex applications by using Helm charts, which are packages of pre-configured Kubernetes resources. This makes it easier to deploy and manage applications on Kubernetes clusters, saving time and reducing complexity.

            By leveraging Kubernetes alongside these DevOps tools, users can build a tech stack that is not only powerful and scalable but also resilient and future-proof. This combination supports rapid development cycles, improved reliability, and efficient operations, ensuring that the tech stack can withstand the test of time.

            In summary, Kubernetes, when used with complementary DevOps tools, provides a robust foundation for modern application deployments. Its ability to automate and manage containerized applications, combined with the power of CI/CD, monitoring, and package management tools, enables organizations to build a resilient and enduring tech stack.
        '''
    }
    # Add more blog posts as needed
]

@app.route("/")
def home():
    return render_template('home.html', profile=PROFILE, accomplishments=ACCOMPLISHMENTS)

@app.route("/blog")
def blog():
    return render_template('blog.html', blog_posts=BLOG_POSTS)

@app.route("/api/accomplishments")
def list_accomplishments():
    return jsonify(ACCOMPLISHMENTS)

@app.route("/api/blog")
def list_blog_posts():
    return jsonify(BLOG_POSTS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
