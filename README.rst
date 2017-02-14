ungog
=====
ungoogleify your css


install
-------
::

  pip install ungog


usage
-----
::

  ungogmycss main.css
  [+] got https://fonts.googleapis.com/css?family=Gruppo|Scope+One
  [+] got https://fonts.gstatic.com/s/gruppo/v7/uU5IFiQZ8WKPhrRfLBLURw.ttf
  [+] replacing from:   src: local('Gruppo'),
  url(https://fonts.gstatic.com/s/gruppo/v7/uU5IFiQZ8WKPhrRfLBLURw.ttf)
  format('truetype');
  [+] replacing to:     src: local('Gruppo'), url('fonts/gruppo.ttf')
  format('truetype');
  [+] got
  https://fonts.gstatic.com/s/scopeone/v2/_52Fm41u4u2R3EEH0A9bn6CWcynf_cDxXwCLxiixG1c.ttf
  [+] replacing from:   src: local('Scope One'), local('ScopeOne-Regular'),
  url(https://fonts.gstatic.com/s/scopeone/v2/_52Fm41u4u2R3EEH0A9bn6CWcynf_cDxXwCLxiixG1c.ttf)
  format('truetype');
  [+] replacing to:     src: local('Scope One'), local('ScopeOne-Regular'),
  url('fonts/scope_one.ttf') format('truetype');
  [+] done

and then you should be ready to replace your original file with main.css.new.
do not forget to include the new fonts/ folder into your local assets.
