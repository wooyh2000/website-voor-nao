</php
$personeelsnr = $_POST['personeelsnr'];
$wachtwoordinvoer = $_POST['wachtwoordinvoer'];

if (!empty($wachtwoordinvoer) || !empty($personeelsnr){
  $host = "oege.ie.hva.nl"
  $dbUsername = "wooyh"
  $dbPassword = "vyrdBMHRSmNtJx"
  %dbname = "zwooyh"
  
  //verbinding maken
  $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
  
  //verbinding mislukt
  if (mysqli_connect_error()){
      die('Connect error('.mysqli_connect_error().')'. mysqli_connect_error());
  } else {
  //data lezen
      $SELECT = "SELECT wachtwoord FROM inlog WHERE personeelsnummer = personeelsnr";
  }
  if ($wachtwoordinvoer==$wachtwoord){
  echo 'Connected successfully';
  }
?>
