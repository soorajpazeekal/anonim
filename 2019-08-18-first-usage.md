---
title: anonim first usage.
description: first blog post.
categories: blog
---



<div class="markdown-body">
<h2>Welcome to anonim wiki!</h2>
<p><span style="text-decoration: underline;"><em>(This is anonim web post <a href="anonim.gq">(anonim.gq)</a> 18/05)</em></span></p>
<p>&nbsp;</p>
<p>anonim is a platform, you can use to send-receive files without tracking and public visibility! this wiki page help you to set-up anonim for first usage.</p>
<h2><a id="user-content-so-get-started" class="anchor" href="https://github.com/soorajpazeekal/anonim/wiki/Wiki-First-use!#so-get-started" aria-hidden="true"></a>so get started!</h2>
<h3><a id="user-content-steps" class="anchor" href="https://github.com/soorajpazeekal/anonim/wiki/Wiki-First-use!#steps" aria-hidden="true"></a>steps:</h3>
<ol>
<li>
<p>First run&nbsp;<strong>setup.py</strong>&nbsp;file on your terminal. (it will automatically detects system conflagrations and install requirements via pip install)</p>
</li>
<li>
<p>After successful set-up, next open your&nbsp;<strong>settings.py</strong>&nbsp;file. (inside of anonim root folder, please see anonim structure wiki page!</p>
</li>
<li>
<p>No go to line 12 --SECRET_KEY = ''-- variable. then add a secret key, not use as an empty value! (Eg: SECRET_KEY = 'lejgfitlqetieqgiy586813rvfuy') Nb: DO NOT SHARE THIS WITH ANYONE!</p>
</li>
</ol>
<p>4)Inside&nbsp;<strong>settings.py</strong>&nbsp;go to line 18: --ALLOWED_HOSTS =-- variable. here you'll need to add your connection address. please follow this sub steps:</p>
<p>4.1) Run&nbsp;<strong>Findlocalip.py</strong>&nbsp;script. (make sure you are now connected to any network. if not, connect now!)</p>
<p>4.2) After script running you'll get an local IP address. and copy the address and paste to: --ALLOWED_HOSTS = -- (eg:ALLOWED_HOSTS = [ '192.<em><strong>.</strong>.</em>', '133.2.**.*']) carefully add values, separate with commas and ('')).</p>
<ol start="5">
<li><strong>All set! Now run 'anonim.py' script to start using!</strong></li>
</ol>
</div>
<div id="wiki-footer" class="mt-5 muted-link wiki-footer"><a href="https://github.com/soorajpazeekal/anonim/wiki/Wiki-First-use!">Click this link to read wiki!</a></div>
