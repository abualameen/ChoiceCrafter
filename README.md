![Choice Crafter Banner](https://drive.google.com/file/d/1zUeqpv0McVr_jpqtK47BHdkwHkSvPfLz/view?usp=sharing)

# Choice Crafter

Choice Crafter is an online decision-making tool designed to assist engineers, researchers, and students in making optimal choices based on multi-criteria decision-making (MCDM) principles. It provides a simple yet powerful platform for evaluating and selecting the best alternative from a set of options, considering various criteria, their associated weight and performance values.
## Inspiration
The inspiration behind developing Choice Crafter stemmed from my experience as a mechanical engineer specializing in solving engineering optimization problems. Often, in such scenarios, we encounter the challenge of selecting one solution from a plethora of options generated by multi-objective optimization methods like NSGAII. These methods converge solutions to the optimal Pareto front, presenting us with an array of potential solutions.

Traditionally, I performed these computations using Microsoft Excel, which was time-consuming and prone to errors. Recognizing the need for a more efficient and user-friendly solution, I embarked on developing Choice Crafter. This project streamlines the decision-making process by allowing users to input their criteria and swiftly obtain the best choice. By automating this process, Choice Crafter enhances productivity and accuracy, empowering engineers, researchers, and students alike to make informed decisions effectively.

## Features

- **Decision Matrix Generation**: Easily create decision matrices by specifying the number of alternatives and criteria (User specified).
- **Normalization of Decision Matrix**: Normalize the decision matrix based on beneficial and non-beneficial criteria.
- **Weightage Normalized Decision Matrix**: Compute weightage normalized decision matrix based on equal weightage assignment for criteria and handling of odd number criteria and assigning weightage accordingly
- **Performance Score Calculation**: Calculate the performance score for each alternative based on the weightage normalized decision matrix.
- **Interactive User Interface**: Intuitive and user-friendly interface for inputting data and viewing results.
- **Dynamic Table Generation**: Generate decision matrices dynamically based on user input.
- **API** A API is also a good feature of Choice Crafter that help user interact with the application

## How it Works

1. **Create Decision Matrix**: Specify the number of alternatives and criteria to generate a decision matrix.
2. **Input Performance Values**: Enter performance values for each alternative and criteria in the generated matrix.
3. **Normalize Decision Matrix**: Normalize the decision matrix based on the type of criteria (beneficial or non-beneficial).
4. **Compute Weightage Normalization**: Assign equal weightage to criteria and compute weightage normalized decision matrix for each alternative.
5. **Calculate Performance Score**: Calculate the performance score for each alternative using the weightage normalized decision matrix.
6. **Identify Best Alternative**: Determine the alternative with the highest performance score as the optimal choice.

## Usage

To use Choice Crafter, follow these steps:

1. Visit the [Choice Crafter website](https://your-choice-crafter-website.com).
2. Specify the number of alternatives and criteria.
3. Enter performance values for each alternative and criteria.
4. Click on the "submit bottom" 
5. The optimal solution with the highest performance score would be displayed upon the click of the submit bottom

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: MySQL (for storing user data)
- **Deployment**: Fabric, Git pages

## API
In addition to the user interface, Choice Crafter features a robust API that interacts seamlessly with the app's database. This API serves as the backbone of the application, enabling efficient retrieval of data from the result table, criteria table, and alternative table.

The API offers versatile functionality, providing two GET methods or endpoints for retrieving data from the database. Users can utilize these methods to access all data within the tables or retrieve specific data by ID, depending on their requirements.

By incorporating this API into Choice Crafter, users gain access to a powerful toolset for managing and analyzing their decision-making processes. Whether retrieving comprehensive datasets for in-depth analysis or accessing specific records for targeted insights, the API enhances the versatility and usability of the application, empowering users to make informed decisions with ease.

Choice Crafter's API offers the following endpoints for seamless interaction with the application's database:

1. **Criteria Endpoint**:
   - `/api/v1/criteria/`: This endpoint allows users to retrieve all criteria data from the database.
   - `/api/v1/criteria/<criteria_id>`: Users can access specific criteria data by providing the ID of the desired criteria.

2. **Alternative Endpoint**:
   - `/api/v1/alternative/`: Users can retrieve all alternative data from the database using this endpoint.
   - `/api/v1/alternative/<alternative_id>`: Specific alternative data can be retrieved by providing the ID of the desired alternative.

3. **Result Endpoint**:
   - `/api/v1/result/`: This endpoint enables users to retrieve all result data stored in the database.
   - `/api/v1/result/<result_id>`: Users can access specific result data by providing the ID of the desired result.

These endpoints facilitate efficient data retrieval, allowing users to access comprehensive datasets or specific records as needed. Whether querying criteria, alternatives, or results, the API endpoints provide a streamlined approach to data access, enhancing the functionality and usability of Choice Crafter.

## Contributing

Contributions to Choice Crafter are welcome! If you have any ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.

## License

Choice Crafter is licensed under the [MIT License](LICENSE).
