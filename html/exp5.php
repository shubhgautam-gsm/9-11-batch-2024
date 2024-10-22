<!DOCTYPE html>
<html>
<body>

<?php
$admin_id='sdbiasbd121';
$adpass='rg3ul4rg';
$name='ram';
$email ='abc@gm';
$pass='jay123';


if ($email=='abc@gm' && $pass=='jay123') {
  if($admin_id=='sdbiasbd121' && $adpass=='rg3ul4rg')
  {
    // a=admin.html
    echo "welcome admin ".$name;
  }	
  else{
  // a= ram.html

   echo "welcome ".$name;
  }
}

else{
// a href signin.php
  echo "sign in";
}
?>
 
</body>
</html>
