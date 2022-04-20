<img src="https://user-images.githubusercontent.com/25334227/162142531-44377fdd-3b0c-40f3-b925-d907b57d5852.png" height="64" width="auto">

# Duo - Brains

Duo needs to be able to learn from changes to the UI and predict user actions to learn a task.

The Brains is responsible for this. It observes data from the UI Layer and determines how to represent them as queries on the Knowledge Graph before predicting following user actions.

![Duo Poc V2 Demo](DuoPocV2.gif)

## Table of Contents:
1. [Overview](#Overview)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Contributing](#Contributing)

<a name="Overview"/>

## Overview:
The Brains is divided into 3 layers:
- The Translation Layer communicates with the UI Layer.
- The Observation Layer manages disambiguation, UI updates, and error handling (during task executing).
- The Data layer manages query generation and predictions.

[Brains Flowchart](https://lucid.app/lucidchart/2b36c255-55c2-4e7b-9965-343c4060a76a/edit?invitationId=inv_777ad870-1198-4a5b-b842-63290bbfbd0b)

<a name="Installation"/>

## Installation:

```
# Clone the repo to your working directory
git clone https://github.com/aspirelabs-inc/DuoPoc-Brains.git

# Install required pip packages
pip install -r requirements.txt

```

Download [Neo4j Desktop](https://neo4j.com/download-center/)

<a name="Usage"/>

## Usage:

In order to run the full Duo Poc, you will need to have both the Brains and the UI layer running.

Go to the [UI Layer Repository](https://github.com/aspirelabs-inc/DuoPoc-UI-Layer.git) for setup instructions if needed.

You can also simulate data from the UI Layer by creating proto objects for testing. There is an example of how to do this at the bottom of the server.py file.

<a name="Contributing"/>

## Contributing:

### How to Contribute
- Fork the project from the master branch and submit a Pull Request (PR)
- Explain what the PR fixes or improves. Include screenshots if possible.
- Use descriptive commit messages

### Commit Messages:

- If your PR fixes a specific issue number, include it in the commit message: "Fixes XYZ error (fixes #123)"

For instructions on how to contribute, please refer to the [Aspire Python Style Guide](https://www.notion.so/aspirelabs/Style-Guides-4cadd884848841d1b254da238aac86e1).

**© Aspire, 2022**
