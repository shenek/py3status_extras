Custom py3status modules
########################

Installation
------------
change you status command in i3 config e.g.::

    status_command py3status -i ~/<path_to_this_repo>/ -c ~/.config/i3/i3status.conf

insert you GL key to::

    ~/.gitlab-token

Don't foget to update the permissions of the file (0600).


Plugins
-------

gitlab
______
* shows the count of the gitlab issues which are assigned to you
