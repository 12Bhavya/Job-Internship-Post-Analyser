<!doctype html>
<html>
<head>
<title>Analysis</title>
<meta name="viewport" content="width=1024, maximum-scale=1">
<link href="../jquery-gauge.css" type="text/css" rel="stylesheet">
<script type="text/javascript">
    var b=0;
</script>
<style>
body {
  background-image: url("b1.jpg");
  font-family: sans-serif;
  color:black;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;    
}
.gauge2{
    transition: all 0.3s ease-in 0s;
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
.onoffswitch {
    position: relative; width: 214px;
    left:10%;
    margin-top:5%;
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
<h1><center><strong>Analysis</strong></center></h1><br>
<?php $no1=$_GET['number'];
       $no=$no1*10; 
       $spam=$_GET['spam'];
       //$pos=$_GET['pos'];
       //echo "<h2>The entered post was '".$pos."'.</h2>";
       echo "<h2>The entered post was analysed and the result is as follows-</h2>";
?>
<div class="onoffswitch">
    <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="myonoffswitch" disabled>
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
</script>
    <!---<div class="gauge2 demo2"></div>-->
    <script src="../jquery.min.js"></script>
    <script type="text/javascript" src="../jquery-gauge.min.js"></script>
    <script>
        $('.gauge2').gauge({
            values: {
                0 : '0',
                10: '1',
                20: '2',
                30: '3',
                40: '4',
                50: '5',
                60: '6',
                70: '7',
                80: '8',
                90: '9',
                100: '10'
            },
            colors: {
                0.000: '#FF0000',
                3.125: '#FF1000',
                6.250: '#FF2000',
                9.375: '#FF3000',
                12.500: '#FF4000',
                15.625: '#FF5000',
                18.75: '#FF6000',
                21.875: '#FF7000',
                25.000: '#FF8000',
                28.125: '#FF9000',
                31.25: '#FFB000',
                37.500: '#FFC000',
                40.625: '#FFD000',
                43.75: '#FFE000',
                46.875: '#FFF000',
                50.000: '#FFFF00',
                53.125: '#F0FF00',
                56.25: '#E0FF00',
                59.375: '#D0FF00',
                62.500: '#C0FF00',
                65.625: '#A0FF00',
                71.875: '#90FF00',
                75.000: '#80FF00',
                78.125: '#70FF00',
                81.25: '#60FF00',
                84.375: '#50FF00',
                87.500: '#40FF00',
                90.625: '#30FF00',
                93.75: '#20FF00',
                96.875: '#10FF00',
            },
            angles: [
                180,
                360
            ],
            lineWidth: 15,
            arrowWidth: 15,
            arrowColor: '#0080ff',
            inset:true,
            value: b
        });
    spamtest();
    </script>
<!--<h3 id="score">The post has a score of <?php //echo $no1; ?> out of 10.</h3>-->
<br><br><a class='btn' href='p1.php'>Back</a>
</body>
</html>