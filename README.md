<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FINAL_PROJ</h1>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Samkit02/final_proj.git?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Samkit02/final_proj.git?style=flat-square&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Samkit02/final_proj.git?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Samkit02/final_proj.git?style=flat-square&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat-square&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Contributing](#-contributing)
</details>
<hr>

##  Overview

"InsureMeNow" is an advanced insurance quoting platform designed to simplify the process of obtaining automobile and health insurance quotes. By leveraging sophisticated algorithms, users can input their city/zipcode and daily mileage to receive accurate insurance quotes tailored to their specific circumstances. The platform provides a user-friendly interface where individuals can easily navigate through various coverage options and customize their quotes according to their needs. With integrated mapping services, users can visualize insurance premiums based on geographic location, empowering them to make informed decisions about their coverage.

“InsureMeNow” prioritizes user security and privacy, implementing robust encryption protocols and secure authentication mechanisms to safeguard sensitive information. The platform also offers features such as automated notifications for policy renewals and access to customer support agents for assistance with insurance inquiries. Through seamless integration with third-party e-commerce platforms, users can effortlessly transition from quote generation to policy purchase, streamlining the insurance buying process. Overall, InsureMeNow aims to redefine the insurance quoting experience, providing a comprehensive and efficient solution for individuals seeking automobile and health insurance coverage.

---

##  Features

•	User Registration and Authentication: Users can create accounts and securely log in to the platform to request insurance quotes.

• Quote Generation: Users provide details such as city/zipcode and miles traveled daily, and the system generates insurance quotes for both automobile and health insurance.

•	Customization Options: Users can customize their insurance quotes by adjusting parameters such as coverage levels, deductibles, and additional features.

•	Comparison Tool: The platform includes a tool for users to compare quotes from different insurance providers and select the most suitable option.

•	Interactive Maps: Integration with mapping services to visualize insurance premiums based on geographic location, allowing users to make informed decisions.

•	Notifications: Automated email notifications to remind users of upcoming policy renewals and provide updates on insurance quotes.

•	Customer Support: Access to customer support agents for assistance with insurance inquiries and policy-related questions.

---

##  Repository Structure

```sh
└── final_proj/
    ├── final_pro
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── forms.py
    │   ├── route.py
    │   ├── static
    │   └── templates
    ├── requirements.txt
    └── run.py
```

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.10.7`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the final_proj repository:
>
> ```console
> $ git clone https://github.com/Samkit02/final_proj.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd final_proj
> ```
>
> 3. Install the dependencies:
> ```console
> $ > pip install mysqlclient
> $ > pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run final_proj using the command below:
> ```console
> $ > python run.py
> ```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Samkit02/final_proj.git/issues)**: Submit bugs found or log feature requests for the `final_proj` project.
- **[Submit Pull Requests](https://github.com/Samkit02/final_proj.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Samkit02/final_proj.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Samkit02/final_proj.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
