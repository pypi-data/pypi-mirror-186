# ci-cmg-cruise-schema-orm

## Setting Up a Virtual Environment with pyenv

Install pyenv-virtualenv if you have not already

```bash
brew install pyenv-virtualenv
pyenv install 3.9.13
```

If setting up pyenv for the first time, you will need to add these lines to your `~/.bash_profile`
or `~/.zprofile` (if using zsh, the default in macos Catalina and later) file in order for pyenv 
to automatically activate / deactivate python environments configured for a given directory (next step).
```bash
eval "$(pyenv init -)"  
eval "$(pyenv virtualenv-init -)"
```

configure python environment for project directory

```bash
pyenv virtualenv 3.9.13 cruise-schema-orm-3.9.13
pyenv local cruise-schema-orm-3.9.13
```

install dependencies into python environment
```bash
pip install -r requirements.txt
pip install -r test-requirements.txt
```

## Building
Since this project can use JDBC divers, Apache Maven is used to build and test the library.
Java 8+ and Maven must be installed and on the PATH.  JAVA_HOME and MAVEN_HOME
environment variables should be set.

This project uses a docker container running an Oracle database to run tests.  Docker must be installed.

To build and test, run the following from the root of the project:
```bash
mvn clean install
```

## Developing

