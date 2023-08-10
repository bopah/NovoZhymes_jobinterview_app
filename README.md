**Problem Statement**

This project aims to provide an interactive application that allows users to explore and compare the statistical attributes of Pokémon from different generations. The primary objective is to enable users to analyze the strongest and weakest Pokémon within a chosen generation, and to visualize their individual and average statistics through graphs and tables.

**Objectives**
- **Dataset Utilization**: Load Pokémon statistics data from various generations. Process and filter the data to provide accurate and relevant information to users.

- **Interactive User Interface**: Develop an intuitive user interface that allows users to select a Pokémon generation and choose between viewing the strongest or weakest Pokémon within that generation.

- **Statistical Visualization**: Display Pokémon statistics through tables and graphs, providing users with a clear understanding of each Pokémon's attributes and how they compare to the average for their generation.

- **Visual Representation**: Include images of Pokémon to enhance user experience, allowing users to see what each Pokémon looks like visually.

- **Code Quality**: Follow best coding practices and adhere to SOLID principles to ensure maintainability, readability, and reusability of the codebase.

- **Version Control**: Maintain a well-structured Git history in a GitHub repository to track code changes and facilitate collaboration.

- **Unit Testing**: Implement unit tests to verify the correctness of critical functionalities, ensuring reliable and accurate results.

- **Dockerization**: Dockerize the application to enable seamless deployment across different environments with minimal dependencies.




**Using the Dockerized Pokémon Dash App**

1. Docker: Make sure you have Docker installed on your system

2. Pull the Docker Image. Open a terminal/command prompt and run the following command: <br />
docker pull bopah91/my-pokemon-dash-app

3. Run the Docker container with the following command. This will start the Pokémon Dash App within a Docker container: <br />
docker run -p 8050:8050 bopah91/my-pokemon-dash-app

4. Access the Application: <br />
Open a web browser. In the address bar, copy and paste the url and then press enter: http://localhost:8050

5. To stop the running container, find its container ID using 'docker ps' and then use the following command: <br />
docker stop <container_id>

**Using the Dockerized Pokémon Dash App to run tests**

1. In docker desktop app, navigate to 'Containers' tab in top left corner.

2. Find under 'Image' bopah91/my-pokemon-dash-app and click on it.

3. Then click run in top left corner, and then click run again.

4. Then click on terminal and write+enter: <br />
pytest test_functions.py


**Running the Application in a terminal with Virtual Environment**

1. Open a terminal or command prompt.

2. Navigate to the directory with the 'main.py' file location

3. Create a virtual environment: <br />
python -m venv myenv

4. Activate the virtual environment: <br />
myenv\Scripts\activate

5. Install required dependencies using the provided requirements.txt file: <br />
pip install -r requirements.txt

6. Run the application: <br />
python main.py

7. Open a web browser. In the address bar, copy and paste the url and then press enter: http://localhost:8050

8. To stop the application, press Ctrl+C in the terminal, and then deactivate the virtual environment: <br />
deactivate


**Running unit tests**

1. If you have not already done step 1 to 5 from above, then do them.

2. Run the unit tests: <br />
pytest test_functions.py

3. Decativate virtual environment: <br />
deactivate