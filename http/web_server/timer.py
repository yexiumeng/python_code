from datetime import datetime
print('''\
<html>
<body>
<title>cgi shell</title>
<p>Generated {0}</p>
</body>
</html>'''.format(datetime.now()))
