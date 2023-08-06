

# Start here
FAO AWS CDK is library to build FAO-compliant AWS infrastructure in near-zero time-to-market.

CSI Cloud Team developed a set of highly reusable AWS infrastructural building-blocks in collaboration with the Unix Admin Team and Statistical Working System (SWS) development team.

To adopt FAO AWS CDK enhances the projects' robustness over the time as they will inherit the benefits of a centralized infrastructural development, they can keep the focus on application features development.

These shared infrastructural building-blocks natively implement FAO AWS best practices and abstract low-level technical details, while enabling AWS developers to focus on code production.

As a major positive side effect, the overal sustainability of the FAO AWS cloud environment reaches the stars 🚀.

- [Python package index of FAO AWS CDK](https://pypi.org/project/aws-cdk-constructs/)
- [Source on Bitbucket of FAO AWS CDK](https://bitbucket.org/cioapps/aws-cdk-constructs)

## Prerequisites
Make sure your local machine is configured to meet the [FAO AWS prerequisites](https://aws.fao.org/docs/tutorials/getting_started/)
Before to proceed, make sure you have a general undestanding of what AWS CDK is and how to use it. 

- [AWS CDK introuction](https://aws.amazon.com/cdk/)
- [AWS CDK - YouTube video](https://www.youtube.com/watch?time_continue=1&v=bz4jTx4v-l8)
- [AWS CDK Workshop - Python](https://cdkworkshop.com/30-python.html)

## Tutorials
CSI Cloud Team produced a number of tutorials about FAO AWS CDK (and FAO AWS in general).
This is the link to the [video tutorials](https://aws.fao.org/docs/tutorials/video_tutorials/).

## Getting started


### Local project initialization
 - Request a Bitbucket.org repo and clone it locally (the repository name should contain `-iac` postfix)
 - Initialize CDK project with `cdk init sample-app --language python` command
 - Follow the auto-generated instructions to enable the Python Virtual env contained in the README file. The virtual env mustn't be called `.env`. In case the auto-generation of the python env generates a `.env` virtual env, re-create it following the instructions in the `README.md` with a different name
 - Activate the python virtual env following the README file
 - Install the project dependencies following the README file
 - Test that everything is working with the command `cdk synth`

### Let's start coding
 - Install the AWS CDK constucts as project dependencies `pip install aws_cdk_constructs`
 - Install any other python dependency (e.g. `python-dotenv`)
 - Create the .env.example and three `.env.<ENV>-iac` (with `<ENV>` as one of the value `development`, `qa`, `production`, e.g. `.env.development-iac`) according to AWS standard (you can extend the set of variables as you like)
 - Configure the `.env.<ENV>-iac` files according to application needs

### Let's configure CD/CI
 - Create the [CDK service user](https://cdk.fao.org/service_user_for_iac.html) from AWS CDK consturct
 - Deploy the infrastructure using CDK 
 - Retrieve the newly created User credentials from `AWS console` > `IAM` > `Users` > select your user > `Security Credentials` tab > create `Access Keys`
 - Configure the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `ENVIRONMENT` bitbucket pipeline environment variables or request support in case you do not have enough permissions
 - Create and develop the `bitbucket-pipeline.yml` file
 - On push, the pipeline will run automatically

## Bootstrap you project

Your project is set up like a standard Python project. The initialization process should also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ ENVIRONMENT=<ENV> cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

### Useful commands

`<ENV>` possible values: `development`, `qa`, `production`.
Kindly note, that the correspondent `.env.<ENV>-iac` file must exist to run a given command. For more information please refer to [How to configure your FAO CDK stack](https://aws.fao.org/docs/cdk/cd_ci/#how-to-configure-your-fao-cdk-stack)

 - `ENVIRONMENT=<ENV> cdk ls`          list all stacks in the app
 - `ENVIRONMENT=<ENV> cdk synth`       emits the synthesized CloudFormation template
 - `ENVIRONMENT=<ENV> cdk deploy`      deploy this stack to your default AWS account/region
 - `ENVIRONMENT=<ENV> cdk diff`        compare deployed stack with current state
 - `ENVIRONMENT=<ENV> cdk docs`        open CDK documentation
 - `ENVIRONMENT=<ENV> cdk ls`: to list the available stacks in the projects
 - `ENVIRONMENT=<ENV> cdk synth MY_STACK --profile my-dev`: to synthetize (generate) the cloud formation template of MY_STACK stack
 - `ENVIRONMENT=<ENV> cdk deploy MY_STACK --profile my-dev`: to deploy the the MY_STACK stack


### How to generate the AWS CDK costructs documention
The documentation follows Google format.

 * Browse the `./docs` directory
 * Run the `make html` to generate the static HTML documentation in the  `/docs/_build/` directory

The documentation release is scripted in the pipeline. So you will simply need to release your code in the `master` branch of the repository to see the FAO CDK documentation published. 

### How to release a new version of AWS CDK constructs

The release of the constructs in `pypi` is automated in the CD/CI pipeline. So you will simply need to release your code in the `master` branch of the repository to see the FAO CDK documentation published and your consturcts available on `pypi`. 
Before to move your code in the `master` branch, remember to upgrade the version of the costructs as following:
- Commit your changes, each commit in the repository should follow the convention: [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)
- Run `npm run release` to auto generate the `CHANGELOG.md` file and upgrade the constructs version.
- Pull request the code to the master branch of the repo

If you try to release a version already published (i.e. you forget to upgrade the package version in the mentioned file) the release will fail. 
Check out the CD/CI pipeline for additional information.

### How can I test my new FAO CDK version before to publish it?

- Open the `IAC` project your are woring on, and create a `git` branch for the feature you are developing
- Install the project dependencies using `pip install -r requirements.txt`
- Locally install the `FAO CDK` constructs using `pip install -e ../../cdk/aws-cdk-constructs/` (NB: the path in your file system may vary). This implies that you cloned the `FAO CDK` repository on your local machine, and the repository is configured to use the `develop` branch
- Modify in the local `FAO CDK` repo the code to implement the desired infrastructural resources
- You can test the `FAO CDK` deployment from the `IAC` repository, using the `CDK CLI` (e.g. `cdk deploy YOUR_STACK --profile YOUR_PROFILE`). This will read from your local `FAO CDK` repository the new modifications you just developed to include them in the deployement
- Once the `FAO CDK` development is completed, release the new `FAO CDK` version as described above and update the `requirements.txt` files in the `IAC` repository
- Once the `IAC` repository is pushed on Bitbucket, it'll download the newly release `FAO CDK` version during the CD/CI pipeline execution.


