<html>
	<head>
		<title>Analyser</title>
		<meta charset="UTF-8">
		<style>
		body {
		  background-image: url("b1.jpg");
		  font-family: Lora, sans-serif;
		  color:white;
		  -webkit-font-smoothing: antialiased;
		  -moz-osx-font-smoothing: grayscale;    
		}
		.btn {
		  -webkit-border-radius: 10;
		  -moz-border-radius: 10;
		  border-radius: 10px;
		  -webkit-box-shadow: 0px 1px 3px #666666;
		  -moz-box-shadow: 0px 1px 3px #666666;
		  box-shadow: 0px 1px 3px #666666;
		  font-family: Georgia;
		  color: #ffffff;
		  font-size: 20px;
		  background: #1a2f3d;
		  padding: 10px 20px 10px 20px;
		  text-decoration: none;
		}

		.btn:hover {
		  background: #8d979e;
		  text-decoration: none;
		}

		.ip, input
		{
		  border-radius: 6px; 
		  width:40%;
		}
		</style>
	</head>

	<body>
		<div class="container">
			<br><h1><strong><center>JOB/INTERNSHIP POST ANALYSER</center></strong></h1><br>
			<form method="post" action="../../cgi-bin/OSM_cgi/savepost.py">
				<h2><center>Enter the post you wish to analyse:</center></h2>
				<center><textarea class="ip" name=posts cols="50" rows="10"></textarea></center><br>
				<center><input style="width:auto" class='btn' type='submit' name ='submit' value='Submit' /></center>
			</form>
		</div>
	</body>
</html>