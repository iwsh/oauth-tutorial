# OAUTH TUTORIAL

## Requirement
- Docker
- Docker Compose
## Usage

1. Create OAuth App on github  
    https://docs.github.com/developers/apps/building-oauth-apps/creating-an-oauth-app

2. Clone this repository  
    ```
    git clone https://github.com/iwsh/oauth-tutorial
    cd oauth-tutorial
    ```

3. Create `.env` with your Github Client ID and Secret (Created in Step 1.)  
    (You can refer to `.env.template`)

4. Run application containers  
    ```
    docker compose up
    ```
