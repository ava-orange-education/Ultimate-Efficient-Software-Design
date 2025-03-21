name: Lint Code

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    # Step 1: Check out the code from the repository
    - name: Checkout code
       uses: actions/checkout@v3

    # Step 2: Set up Node.js environment
    - name: Set up Node.js
       uses: actions/setup-node@v3   

      with:
        node-version: 16

    # Step 3: Install dependencies
    - name: Install dependencies
       run: npm install
    
    # Step 4: Run ESLint
    - name: Run ESLint 
    run: npm run lint
