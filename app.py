from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROFILE = {
    'name': 'Abiola Shittu',
    'bio': 'Abiola Shittu is an experienced Cloud Engineer with over 10 years of expertise in information technology. Throughout his career, he has worked extensively with key DevOps tools to facilitate seamless web application deployments, showcasing his proficiency in cloud infrastructure and deployment automation. His dedication and technical skills have made him a valuable asset in the IT field.',
    'email': 'mailto:abiola.shiba@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/abiola-shittu/',
    'github': 'https://github.com/shittuay',
    'resume': 'images/Docs/resume.docx',  # Update this with the actual path to your resume
    'picture': 'images/Abiola.jpeg',
    'profile': 'images/Docs/Profile.pdf'
}

ACCOMPLISHMENTS = [
    {'title': 'Project 1', 'description': 'Web-application project deployment on AWS Cloud using Terraform and Jenkins'},
    {'title': 'Project 2', 'description': 'Python-flask web application deployment on Kubernetes cluster using Helm and Kustomize'},
    {'title': 'Award', 'description': 'AWS Cloud Practitioner Certification'},
    {'title': 'Award', 'description': 'AWS Cloud Quest Certification'},
    {'title': 'Award', 'description': 'AWS DevOps Engineer Certification'},
    {'title': 'Award', 'description': 'ITIL Foundation Certification'},
    # Add more accomplishments as needed
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
