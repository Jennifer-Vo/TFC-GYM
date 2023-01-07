# TFC-GYM

A Website for a fictional Toronto Fitness Club Gym as a Final Project for CSC309.

## Contributors: 
Sung Hyun Cho, Rohit Shetty, Jennifer Vo

## Tech Stack: 
Django, REST, and React.


## Instructions to Run:

1- Clone Repository and make sure you have latest version of Django and React Installed.

2- In terminal run startup.sh, renenw.sh and run.sh .

3- Project should run on localhost3000:

## Snippet of Website:
![alt text](https://user-images.githubusercontent.com/62463648/208800627-dd0a9f13-22bb-4c6c-b6fc-aaec6ef0e7ec.png)
![alt text](https://github.com/rshetty22166145/TFC-GYM/issues/2)


## User stories
### Accounts
As a user, I can sign up, log in, log out, and edit my profile. Profile information should include first and last name, email, avatar, and phone number.

### Studios
As the website admin (i.e., an account that has access to the admin panel), I can create/edit/delete studios. A studio has a name, address, geographical location, postal code, phone number, and a set of images. As the website admin, I can update the amenities of a studio (type and quantity).
As a user, I want to list studios based on geographical proximity to a speciCc location (e.g., my current location, a pinpoint on map, or a postal code). Studios must list starting from the closest one, each having a drop pin on the map. As a user, I can click on each of the studios and move to the studio page. This page should contain the general information of that studio, along with its address, location, and a link to get the directions.
Classes As the website admin, I can create/edit a class in a speciCc studio. A class has a name, description, coach, a list of keywords (e.g., upper-body, core, etc.), capacity, and times. Times indicate the recurring instances of the class. For example, a HIIT session is held on Mondays from 8:00- 9:00am.

### Classes:
As the website admin, I can cancel a specific class; either one instance or all the future occurrences of the class.
As a user, I want to see the class schedule of a specific studio on its page. Classes must appear in the order of their start time (from now), and the class information must be shown. Past or cancelled classes should not be listed. As a user, I can enrol/drop a class (either one instance or all future occurrences) that has not started yet and has not reached its capacity. This can only happen if I have an active subscription.
As a user, I want to see my class schedule and history in chronological order

### Searching and Filtering:
As a user, I want to search/filter through the listed studios (mentioned earlier). Search/filter includes stdio name, amenities, class names, and coaches that hold classes in those studios.
As a user, I want to search/filter a studio's class schedule. The search/Clter can be based on the class name, coach name, date, and time range.
### Subscriptions
As the website admin I can create/edit/delete the gym subscription plans (e.g., 14.99$ per month or $149.99 per year).
As a user, I can subscribe to one of the options; the first payment is made immediately after subscription, and each upcoming payment will be automatically made in the beginning of their period.
As a user, I can update my credit/debit card information. All subsequent payments must be made to the updated card.
As a user, I can see my payment history (amount, card info, date and time, etc.), as well as my future payments.
As a user, I can cancel or update my current subscription. The next payment will be either cancelled or updated. In case of cancellation, all class booking after the current billing period will be invalid.

### 


