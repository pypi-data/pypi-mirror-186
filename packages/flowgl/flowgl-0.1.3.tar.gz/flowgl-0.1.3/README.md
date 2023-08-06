# Flow Immersive Python Client

An easy way to push data from pandas to Flow.

## Usage

Push data to Flow, identifying the dataset with a title. 
Pushing a new dataset with the same title will create a new dataset version.

```python
import pandas as pd

# Example pandas dataframe
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Joe'],
    'age': [30, 25, 40],
    'city': ['New York', 'San Francisco', 'Los Angeles']
})

from flowgl import Client

# Import the client and create an instance with your credentials
client = Client(
    username=...,
    password=...,
)

# Push the dataframe to Flow by title
client.push_data(
    df,
    dataset_title='My Dataset',
)
```

## Development

### Installation

First, install python and poetry. If on Windows, ensure you add poetry's bin directory to your PATH environment variable (search for "environment variables" in the start menu).

Then, clone the repository and step into it.
```bash
git clone git@bitbucket.org:flowvr/flow-scripts.git
cd flow-scripts
```
#### Create Virtual Environment

Create a virtual environment (replace python with python3 or py as per your installation).

```bash
python -m venv venv
```

#### Activate Virtual Environment

This will activate the virtual environment for the current terminal session. You should see (venv) at the start of your terminal prompt.

On Windows Powershell:
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
.\venv\Scripts\Activate.ps1
```

On Windows Command Prompt:
```cmd
.\venv\Scripts\activate.bat
```

On Mac/Linux/WSL:
```bash
source venv/bin/activate
```

#### Install Dependencies

Finally, install the dependencies with poetry.

```bash
poetry install
```

### Publishing

To publish a new version of the package, first update the version number in `pyproject.toml`.  
Then, run the following commands: 

```bash
poetry build
poetry publish
```
