# Choice Crafter

Choice Crafter is an online decision-making tool designed to assist engineers, researchers, and students in making optimal choices based on multi-criteria decision-making (MCDM) principles. It provides a simple yet powerful platform for evaluating and selecting the best alternative from a set of options, considering various criteria, their associated weight and performance values.

## Features

- **Decision Matrix Generation**: Easily create decision matrices by specifying the number of alternatives and criteria (User specified).
- **Normalization of Decision Matrix**: Normalize the decision matrix based on beneficial and non-beneficial criteria.
- **Weightage Normalized Decision Matrix**: Compute weightage normalized decision matrix based on equal weightage assignment for criteria and handling of odd number criteria and assigning weightage accordingly
- **Performance Score Calculation**: Calculate the performance score for each alternative based on the weightage normalized decision matrix.
- **Interactive User Interface**: Intuitive and user-friendly interface for inputting data and viewing results.
- **Dynamic Table Generation**: Generate decision matrices dynamically based on user input.

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

## Contributing

Contributions to Choice Crafter are welcome! If you have any ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.

## License

Choice Crafter is licensed under the [MIT License](LICENSE).
