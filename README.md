C3-PRO Website
==============

Website for the **C3-PRO** technology toolchain.
Hosted at [c3-pro.chip.org](http://c3-pro.chip.org).

Building the Site
-----------------

The site uses [Jinja2]() templates, rendered using a Python script, and uses [SASS](http://sass-lang.com/install) and requires [Bourbon](http://bourbon.io).
To develop the website, install the **Python requirements**, best into a virtual environment:

```bash
virtualenv -p python3 env
. env/bin/activate
pip install -r requirements.txt
./build.py
```

You will need the **sass gem** to let sass update the CSS:

```bash
gem install bourbon
cd sass
bourbon install
cd ..
sass --watch -t compact sass:static
```
