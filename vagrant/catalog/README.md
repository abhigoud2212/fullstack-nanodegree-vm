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
### Databse Setup  
'$ python database_setup.py'

### Adding menus
`$ python lotsofmenus.py`

###Run the tests
`$ python tournament_test.py`

If successful, you should see a message **added menu items!**

### Run finalproject.py by following to see the website at http://localhost:5000 
`$ python finalproject.py` 
