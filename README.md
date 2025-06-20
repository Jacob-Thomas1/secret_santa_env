# Secret Santa Manager
## Description
This project, `secret_santa_env`, is a solution designed to manage and organize Secret Santa gift exchanges efficiently. It automates the process of assigning participants and ensures fairness while avoiding repetitions from previous year.

## Features
- Randomized participant assignment.
- Ensures no self-assignment.
- Avoids repetitions by taking into consideration of previous years results if any. 

## Assumptions
- All employees joining this year may or may not have a previous secret santa (took part last year). 
- Some employees can have same names, but differentiated by their email ID. Different email IDs are considered as separate entities (employees), since in input some employees have same name but  different email IDs. 

## Classes
This involves two classes :-

`Employee`: This class represents a participant in a Secret Santa event. Each employee has a name, email, a record of their previous Secret Santa if any, and their current Secret Santa assignment. 

`SecretSanta`: This class manages the assignment of Secret Santas for a group of employees. It ensures that no one is assigned themselves or their previous year's Secret Santa. The `assign_secret_santa` method handles the assignments, while `check_employees` validates the employee list and ensures the rules are followed.

## Folder Structure
- **input/**: Contains input files such as `Employee-List.xlsx` and `Secret-Santa-Game-Result-2023`.
- **output/**: Stores the generated current year Secret Santa assignments.
- **models/**: Contains the used classes like `Employee` and `Secret Santa`. 
- **utils/**: Has helper functions aiding main function to read excel.
- **tests/**: Holds test cases to ensure the program functions correctly.



## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/secret_santa_env.git
    ```
2. Navigate to the project directory:
    ```bash
    cd secret_santa_env
    ```
3. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Add `Employee-List.xlsx` and `Secret-Santa-Game-Result-2023` to the `input` folder in the required format.
2. Run the program:
    ```bash
    python3 main.py
    ```
3. The assignments will be generated and saved in the `output` directory.

## Additional Information
- Ensure Python 3.8 or higher is installed.
- Ensure requirements.txt is met. 

## Contact
For any questions or feedback, please reach out to jacob.thomas1@gmail.com.