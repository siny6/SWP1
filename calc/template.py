html = b"""
<html>
    <body>
        <form method="get" action="">
             num1 = <input type="number" name="a">
             num2 =  <input type="number" name="b"><br><br>
            <input type="submit">
        </form>
	<p>
            plus: %(plus)d</br>
	    mult: %(mult)d</br>
	</p>
    </body>
</html>
"""
