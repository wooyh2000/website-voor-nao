<!DOCTYPE html>
<html>
<head>
  <?php include '/website-voor-nao/style.css';?>
</head>
  <title>Eigen baas</title>
    <div class="navbar">
    <a href= https://wooyh2000.github.io/website-voor-nao/index.html>Home</a>
    <a href= https://wooyh2000.github.io/website-voor-nao/invoerpatient.html>Invoer patient</a>
    </div>
<body>
<title>Medewerkerpagina</title>
<SCRIPT TYPE="text/javascript" LANGUAGE="JavaScript">
<!--

function initArray() {
this.length = initArray.arguments.length;
for (var i = 0; i < this.length; i++)
this[i+1] = initArray.arguments[i];
}

var dagArray = new initArray("zondag","maandag", "dinsdag","woensdag","donderdag","vrijdag","zaterdag");

var maandArray = new initArray("januari","februari","maart","april","mei","juni","juli", "augustus","september","oktober","november","december");

var nu = new Date();
var dagtekst = dagArray[(nu.getDay()+1)];
var dag = nu.getDate();
var maandtekst = maandArray[(nu.getMonth()+1)];
var jaar = nu.getYear();
var jaar4 = ((jaar < 1900) ? (jaar + 1900) : (jaar));

var datumweergave = "Het is vandaag " + dagtekst + " " + dag + " " + maandtekst + " " + jaar4;

document.write(datumweergave);
</SCRIPT>
<p>Je agenda voor vandaag:</p>
</body>
</html>
