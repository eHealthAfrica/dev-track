dev-track
=========

A simple django demonstration project -- collects software developer's password salts and private keys.

* at the moment, this is just an empty place-holder.

* this project is designed to be installed using Salt -- specifically, using https://github.com/eHealthAfrica/salt_demo

installation instructions
=========================

Do not install this project by git-cloning it into your private space.  

(Unless you plan to work on a new fork, in which case clone your new fork, not this one.)

Clone https://github.com/eHealthAfrica/salt_demo into your private working area. It will install this.

[Important: read the note about linking /opt/Envs to your personal Python virtual environment root.]

    git clone https://github.com/eHealthAfrica/salt_demo
    cd salt_demo
    nano saltpillar/demo_settings.sls  # customize usernames, passwords, etc.
    ./local_deployment.sh
    
Log off ond back on, so that you have connection to the virtual environments.

    workon demo-app
    ./manage.py syncdb  # provide the username and password for your new database administrator django user.
    ./manage.py collectstatic  # answer "yes" when prompted
    sudo service uwsgi restart
    sudo service nginx restart
    
That it.  Browse to http://localhost/index
  
Administer you new server using: http://localhost/admin


