### Restaurant Menu App
This program simulates the rounds using the Swiss system for pairing up players in each round: players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible.

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
'$ python lotsofmenus.py'
###Run the tests
`$ python tournament_test.py`

If successful, you should see a message **added menu items!**

