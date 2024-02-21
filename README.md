# MindShift 

MindShift its a toolkit that help you to get more control about your thoughts and actions.

# Features

• Track Thoughts: Allows you to track your thoughts over the time.

• Thoughts Charting: Observe the relationships and characteristics of your thoughts graphically.

• Search And Filter Thoughts: Allows you to smart search and filter your thoughts easily, intuitively and accurately.

• Dangerous Thought Alerts: You will be notified when a thought related to the emotions of sadness or anger is becoming too repetitive or constant in your daily life.

Note: This project is currently in a very early stage of development. This means that some features may be incomplete or under development, and it's possible that not all features will work as expected.

# Preview
![MindShift1](https://github.com/rojas-jesus/MindShift/assets/148916557/ad71ae11-8ce3-461f-8a7e-63fe35e92d33)

![MindShift2](https://github.com/rojas-jesus/MindShift/assets/148916557/48b7b50c-6d1c-4903-825c-23b5ce25c2d4)

# Contributions & Feedbacks
I value your interest in contributing or providing feedback. The project is still in its early stages, so I kindly ask that you wait until I have a more stable base before submitting significant contributions or feedback.

# Getting Started

First, clone the repository from Github. Then, navigate to the project directory and activate the virtual environment.
    
Install project dependencies:
```bash
pip install -r requirements.txt
```

Create the .env file:
- Navigate to the root directory of the Django project (where the manage.py file is located).
- Create a new file named .env (touch .env).
- Open the .env file you just created and add the following lines, replacing the example values with your own secret keys and configurations:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```
Apply the migrations:
```bash
python manage.py migrate
```
Create a superuser:
```bash
python manage.py createsuperuser
```
Run the development server:
```bash
python manage.py runserver
```

# Main Technologies Used

• Django

• Bootstrap

• JavaScript
