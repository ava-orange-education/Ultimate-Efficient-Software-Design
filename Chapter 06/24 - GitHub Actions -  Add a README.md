# Hello World Action

This action prints "Hello World" and a customizable name.

## Inputs

### `name`

**Required** The name of the person to greet. Default is "World".

## Example usage

```yaml
uses: actions/hello-world-action@v1
with:  name: 'Alice'




#### Step 5: Testing and Publishing Your Action

Before using your action in workflows, you should test it locally or within a temporary GitHub workflow. Once tested, commit your files to a GitHub repository.

To use the custom action in your workflows, reference it by your repository and the specific version or branch:

```yaml
jobs:
  hello-world-job:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Run custom action
      uses: your-username/your-repository@v1
      with:
        name: 'Alice'

