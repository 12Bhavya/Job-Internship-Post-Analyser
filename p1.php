<html>
<head>
	<title>Analyser</title>
	<meta charset="UTF-8">
	<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
	<script src="bootstrap/jQuery/jquery.min.js"></script>
	<script src="bootstrap/js/bootstrap.min.js"></script>
<style>
body {
  background-image: url("b1.jpg");
  font-family: sans-serif;
  color:black;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;    
}

.btn {
   background: black;
  -webkit-border-radius: 7;
  -moz-border-radius: 7;
  border-radius: 7px;
  color: white;
  font-size: 12px;
  padding: 8px 13px 8px 13px;
  border: solid black 1px;
  text-decoration: none;
}

.btn:hover {
  color: white;
}

.ip, input
{
  border-radius: 6px; 
  width:40%;

}
</style>
</head>

<body>
<?php 
  if($_GET)
  { 
    $no1=$_GET['number'];
    $no=$no1*10; 
    $spam=$_GET['spam'];
  }
?>
<div class="container">
	<h2><strong><center>INTERNSHIP & JOB POSTS ANALYZER</center></strong></h2><br><br>
	<form method="post" action="../../cgi-bin/analyse_post.py">
		<h3><center>Enter the post you want to analyse:</center><br></h3>
		<center><textarea class="ip" name=posts cols="40" rows="8"></textarea></center><br>
		<center><input style="width:auto" class='btn' type='submit' name ='submit' value='Submit' /></center>
	</form>
</div>
</body>
</html>