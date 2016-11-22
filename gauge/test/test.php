<html>
	<head>
		<title>Analysis</title>
		<meta name="viewport" content="width=1024, maximum-scale=1">
		<script type="text/javascript">
			var b=0;
		</script>
		<style>
			body {
			  font-family: Lora,sans-serif;
			  color:black;
			  -webkit-font-smoothing: antialiased;
			  -moz-osx-font-smoothing: grayscale;    
			}
			.gauge2{
				transition: all 0.2s ease-in 0s;
			}
			.demo2 {
				position: relative;
				width: 40vw;
				height: 40vw;
				left:40%;
				box-sizing: border-box;
				margin:20px;
				margin-top:-8%;
				margin-bottom: -15%;
				transition: all 0.3s ease-in 0s;
			}
			.score{
				position: relative;
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
			  font-size: 16px;
			  background: #1a2f3d;
			  padding: 8px 16px 8px 16px;
			  text-decoration: none;
			}

			.btn:hover {
			  background: #8d979e;
			  text-decoration: none;
			}
			.onoffswitch {
				position: relative; width: 214px;
				left:10%;
				-webkit-user-select:none; -moz-user-select:none; -ms-user-select: none;
			}
			.onoffswitch-checkbox {
				display: none;
			}
			.onoffswitch-label {
				display: block; overflow: hidden; cursor: pointer;
				border: 2px solid #999999; border-radius: 10px;
			}
			.onoffswitch-inner {
				display: block; width: 200%; margin-left: -100%;
				transition: margin 0.3s ease-in 0s;
			}
			.onoffswitch-inner:before, .onoffswitch-inner:after {
				display: block; float: left; width: 50%; height: 35px; padding: 0; line-height: 35px;
				font-size: 20px; color: white; font-family: Trebuchet, Arial, sans-serif; font-weight: bold;
				box-sizing: border-box;
			}
			.onoffswitch-inner:before {
				content: "HAM";
				padding-left: 15px;
				background-color: #34C23C; color: #FFFFFF;
			}
			.onoffswitch-inner:after {
				content: "SPAM";
				padding-right: 15px;
				background-color: #FF0000; color: #000000;
				text-align: right;
			}
			.onoffswitch-switch {
				display: block; width: 19px; margin: 8px;
				background: #FFFFFF;
				position: absolute; top: 0; bottom: 0;
				right: 178px;
				border: 2px solid #999999; border-radius: 10px;
				transition: all 0.3s ease-in 0s; 
			}
			.onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-inner {
				margin-left: 0;
			}
			.onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-switch {
				right: 0px; 
			}
		</style>
	</head>
	<body>
		<h1><center>Result</center></h1>
		<?php  $spam=$_GET['spam'];?>
		<h2>The entered post was found to be :</h2>
		<div class="onoffswitch">
			<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="myonoffswitch" >
			<label class="onoffswitch-label" for="myonoffswitch">
				<span class="onoffswitch-inner"></span>
				<span class="onoffswitch-switch"></span>
			</label>
		</div>
		<script type="text/javascript">
			b='<?php echo $no ?>';
			var sp='<?php echo $spam; ?>';
		</script>
		<script type="text/javascript">
		function spamtest()
		{
			if(sp == 1)
				document.getElementById("myonoffswitch").checked = false;
			else
				document.getElementById("myonoffswitch").checked = true;
		}
		spamtest();
		</script>	
		<br><br><a class='btn' href='../../OSM/p1.php'>Enter new post</a>
	</body>
</html>