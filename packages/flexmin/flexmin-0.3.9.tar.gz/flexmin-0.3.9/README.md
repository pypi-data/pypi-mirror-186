# Flexmin #

Flexmin is an easy to customise web based management tool for the occasional
system administrator.

Flexmin is perfect for those who use Linux but don't want to be a full time 
Linux administrator; it makes common administration tasks easy. It is perfect
for web developers who want to use NGINX, uWSGI and Python based web tools as
it makes the set up and administration of these parts of a web stack easy.

If you have clients who need to run a server you can use Flexmin to give them
easy access to perform any common system administration tasks by themselves.

Flexmin is designed to be easy to extend to carry out your most frequent tasks,
provided you can create a suitable bash script. The bash scripts simply 
need to output text in YAML format to present forms, information, or tables
to the end user. The same script can be design to recongised submitted forms
and carry out the specified task.

Many common task scripts are supplied with the Flexmin system. Adding your
own scripts is easy, as is customising the menu items for your own purposes.
You own custome scripts and settings are hel separately from the built in
defaults, so an upgrade to the Flexmin system will not overwrite your custom
settings or scripts.

Flexmin consists of a python based service (daemon) that runs as root and 
handles tasks sent to it by the web based GUI. 

> **IMPORTANT**: Check the Flexmin security documentation to ensure you understand
how Flexmin security is implemented. The security has not been independently 
assessed; use at your own risk. Use on public networks is *not* recommended,
and additional precautions may be advisable.

## Install ##

### Prerequisites ###

Flexmin requires the following software packages:

- OpenSSL (openssl)
- Python 3 and Pip (python3 and python-pip or python3-pip)
- NGINX (nginx)
- uWSGI and uWSGI Python Plugins (uwsgi, uwsgi-plugin-python or uwsgi-plugin-python3)

> NOTE: Debian based distros (Raspbian and Ubuntu for example) seem to need packages
> python3-pip and uwsg-plug-python3, they also require the use of the **`pip3`**
> command instead of pip.

> **IMPORTANT**: Flexmin is expected to be installed on a fresh system ready 
> to manage using 
> the Flexmin tool. If installing on an existing system you should take care 
> to backup NGINX, uWSGI or OpenSSL configurations in case the Flexmin 
> installation affects them.

Python modules required (pip, or pip3 command for Debian and Ubuntu based distro):

- wheel *(install first, needed for subsequent installs)*
- pyyaml *(should be installed as a dependency by pip)*
- py4web *(should be installed as a dependency by pip)*
- click *(should be installed as a dependency by pip)*

Once the Prerequisites are all installed run these commands:

```bash
sudo pip install flexmin
sudo flexmin install
```

The first command should install the flexmin package, the second unpacks some 
associated files and folder and configures flexmin to run on your system. After
running these commands you should have a fully functioning web server and 
Flexmin web interface.

