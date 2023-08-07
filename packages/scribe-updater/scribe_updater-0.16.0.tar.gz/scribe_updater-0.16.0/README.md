#### Run
`poetry run updater`

#### Test
`poetry run pytest` 

#### Coverage
`poetry run pytest --cov`

### Publish to PyPi
After adding credentials to be able to push to the python package index run the following cmd:
`poetry publish --build`

#### Caveats
if you are getting an error that looks like this :<br> `Failed to create the collection: Prompt dismissed..`<br>
then export the following environment variable: <br>
`export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring`