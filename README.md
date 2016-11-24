tornado_circus_heroku
=====================

Manage a bunch of Tornado app processes on one Heroku dyno with[Circus](http://circus.readthedocs.org/).

Just click the button
---------------------

[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/mrluanma/tornado_circus_heroku)

Or hardcore mode
----------------

```bash
$ heroku create
$ heroku buildpacks:set heroku/python
$ heroku buildpacks:add https://github.com/ryandotsmith/nginx-buildpack.git
$ git push heroku master
$ heroku open
```
