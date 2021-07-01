[![Discord](https://img.shields.io/discord/853667307506368542?color=%23235379%20&label=Join%20our%20community&style=for-the-badge)](https://discord.gg/2XzgH4bZYp)&nbsp;&nbsp;![GitHub contributors](https://img.shields.io/github/contributors/privalise/social-network?color=%234369aa%20&style=for-the-badge)&nbsp;&nbsp;![GitHub top language](https://img.shields.io/github/languages/top/privalise/social-network?style=for-the-badge)
# PrivaLise 
### Social Media Network Focuses On Data Security And Being Community Driven Web App

## The Main Idea:
Can you imagine a centralized, but privacy-respecting social network? One that is modern, easy to use, fast and provides security and protection for everyone. That is why we created PrivaLise!

Encrypted credentials, 2 factor authentication, no associated personal information to hack... To Put It Simply: The Web App will not record anything about its users. <br/>
We actively avoid using any 3rd party software, such as google APIs, google analytics, any FAANG framework (React, Vue...), so rest assured that you will be totally anonymous :D

We also plan on creating an onion version of the web, so stay tunned!!

## Community: contribute or hang out with the developers!
Join our [discord server](https://discord.gg/2XzgH4bZYp) now!

## The Technology Behind It:
   * Python 3.9.2
   * Django 2.2.22
   * Pure HTML/CSS/JS

## Main Features:
   * Sign IN/UP/OUT
   * Post CRUD
   * Update Username / Profile Pic
   * Infinite Scroll On The Home Page
   * Password Recovery / Change
   * 2 factor authentication

## New front-end
The entire front-end is being completely re-designed from the ground up. In order to iterate faster, it has been separated into its own repository, and in the near future it will be incorporated into this one.
Links:
* [Login](https://margual56.github.io/demo-web/login)
* [Sign up](https://margual56.github.io/demo-web/register)
* [Home page](https://margual56.github.io/demo-web/)
* [Profile page](https://margual56.github.io/demo-web/profile)

Any feedback or suggestion is appreciated and can be sent to [margual56@gmail.com](margual56@gmail.com) or to the discord server.

 ## Set Up: 
  * Clone The Repository `git clone https://github.com/privalise/social-network.git && cd privalise`
  * Install Requirements `pip install -r requirements.txt && cd privalises`
  * Let\`s Migrate And Make Migrations `python manage.py makemigrations && python manage.py migrate`
  * Now Finally We Will Run The Server `python manage.py runserver`
  
 ### Additional Steps:
  1. Create '.env' file in the root directory
  2. Specify The Following
	  * email (Add The EMAIL_HOST_USER)
	  * pass (Specify The EMAIL_HOST_PASSWORD)
	  * port  (Specify The EMAIL_PORT)
	  * hash  (Specify The SECRET_KEY)
	  * backend (Specify The EMAIL_BACKEND)
	  * host (Specify The EMAIL_HOST)
	  * tls (Specify The EMAIL_USE_TLS)
	 ### In The End It Should Look Like This:
	  ```python
	  email=email@email.email
	  pass=password
	  hash=gjkmjgbkjbgmoirejoibjgboikejrgkjstojmsvoiigormjoiysmdfvmg
	  port=587
	  tls=True
	  host=smtp.provider.com
	  backend=django.core.mail.backends.smtp.EmailBackend	
	  ```

# LICENSE
	Privalise, A Secure Privacy Friendly Social Network
	Copyright (C) 2021 PrivaLise foundation
	
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	any later version.
	
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	










