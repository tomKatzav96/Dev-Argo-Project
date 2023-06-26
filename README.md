# CI-CD Pipeline with GitOps 

This project demonstrates the implementation of a CI/CD pipeline with GitOps using GitHub Actions, Docker, and Argo CD. The pipeline aims to streamline the software delivery process, ensuring consistent builds, testing, and deployments while leveraging GitOps principles for managing Kubernetes deployments.  

The CI pipeline, powered by GitHub Actions, automates the build, test, and publishing processes. It begins with the creation of a Docker image, incorporating the latest changes from the source code. The pipeline then runs comprehensive unit tests using pittest and functional tests using Selenium to validate the application's behavior.  

Upon successful testing, the Docker image is published to a Docker registry, making it accessible for deployment. Simultaneously, the deployment configuration for the pre-production environment is updated, ensuring that the latest changes are reflected in the application's configuration.  

GitOps is implemented using Argo CD, which synchronizes the deployment configuration stored in the Pra Production repository to a Kubernetes cluster within the Pra Production namespace. Argo CD employs Helm charts to define and deploy the application, ensuring consistency and reproducibility across environments.  

To enhance visibility and communication, the CI/CD pipeline also includes an automated email notification feature. Status updates regarding the pipeline's progress, including successful deployments or encountered issues, are sent via email to relevant stakeholders.  

By adopting this CI/CD pipeline with GitOps approach, the project aims to optimize the software delivery process, reduce manual intervention, and maintain a consistent and reliable deployment pipeline. It empowers teams to focus on building high-quality applications while ensuring efficient and automated software releases.  


![Image](argo-project.png "Architecture of the project")


## Acknowledgements
...

## Badges

![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

![ArgoCD](https://img.shields.io/badge/Argo%20CD-1e0b3e?style=for-the-badge&logo=argo&logoColor=#d16044)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=Helm&labelColor=0F1689)

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)

## Roadmap

- **...**
