### Restaurant Menu App
A website in which each users can create multiple Restaurants with different menu items. It is designed using python flask framework and for frontend bootstrap. A Oauth 2.0 login service is provided using google plus and facebook. 

###Install VirtualBox
https://www.virtualbox.org/wiki/Downloads

**windows user:** If there are issues with version 5,  install version 4.3

### Install Vagrant
https://www.vagrantup.com/downloads

###Clone the Repository
```
$ git clone https://github.com/abhigoud2212/fullstack-nanodegree-vm.git
$ cd fullstack-nanodegree-vm
$ cd vagrant
```
###Launch Vagrant
```
$ vagrant up 
$ vagant ssh
```

###Restaurant Menu
```
$ cd /
$ cd vagrant
$ cd catalog
```

### If pip Already installed
If pip is already installed. Run the following command in Shell. Which will install all the necessary things to run the App.

`pip install -r requirments.txt `
### Databse Setup  
`$ python database_setup.py`

### Adding menus
`$ python lotsofmenus.py`

###Run the tests
`$ python tournament_test.py`

If successful, you should see a message **added menu items!**

### Run finalproject.py and goto http://localhost:5000 to see the website
`$ python finalproject.py` 
