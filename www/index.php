<?php

$ranks = array("reserve", "grunt", "nco", "sl", "hco", "xo", "co", "sco");

$EMC_PASS = "g2UBFaRLqjK";
$APN_PASS = "s2diooCnBEk";
$ADM_PASS = "YI7IM0gTnJo";

if ($_POST) {
    if ($_POST["password"] == $EMC_PASS) {
        if ($_POST["team"] != "emc") {
            $response = array('danger', 'Invalid Team Selected');
        }
    } elseif ($_POST["password"] == $APN_PASS) {
        if ($_POST["team"] != "apn") {
            $response = array('danger', 'Invalid Team Selected');
        }
    } elseif ($_POST["password"] == $ADM_PASS) {
        $response = "";
    } else {
        $response = array('danger', 'Authentication Failed');
    }
}


if (!$response && $_POST) {
    if ($_POST["team"] == "remove") {
        $postData = array(
            'uid' => $_POST["uid"],
        );

        $ch = curl_init('http://prt.blip2.net:7215/player/');
        curl_setopt_array($ch, array(
            CURLOPT_CUSTOMREQUEST => "DELETE",
            CURLOPT_RETURNTRANSFER => TRUE,
            CURLOPT_HTTPHEADER => array(
                'Content-Type: application/json'
            ),
            CURLOPT_POSTFIELDS => json_encode($postData)
        ));

        $json = curl_exec($ch);
        if($json === FALSE){
            $response = array('danger', 'Failed to talk to Teamspeak server');
        } else {
            $ret = json_decode($json, true);
            if ($ret['response'] == "success") {
                $response = array('success', "Permissions removed.");
            } else {
                $response = array('danger', $ret['response']);
            }
        }

    } else {

        $postData = array(
            'uid' => $_POST["uid"],
            'team' => $_POST["team"],
            'rank' => $_POST["rank"],
        );

        $ch = curl_init('http://prt.blip2.net:7215/player/');
        curl_setopt_array($ch, array(
            CURLOPT_CUSTOMREQUEST => "PUT",
            CURLOPT_RETURNTRANSFER => TRUE,
            CURLOPT_HTTPHEADER => array(
                'Content-Type: application/json'
            ),
            CURLOPT_POSTFIELDS => json_encode($postData)
        ));

        $json = curl_exec($ch);
        if($json === FALSE){
            $response = array('danger', 'Failed to talk to Teamspeak server');
        } else {
            $ret = json_decode($json, true);
            if ($ret['response'] == "success") {
                $response = array('success', "Permissions assigned.");
            } else {
                $response = array('danger', $ret['response']);
            }
        }

    }

}

?><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PRT Teamspeak Permissions</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <style>
    body {
      padding-top: 40px;
      padding-bottom: 40px;
      background-color: #eee;
    }

    .form-signin {
      max-width: 450px;
      padding: 15px;
      margin: 0 auto;
    }
    .form-signin .form-signin-heading,
    .form-signin .checkbox {
      margin-bottom: 10px;
    }
    .form-signin .checkbox {
      font-weight: normal;
    }
    .form-signin .form-control {
      position: relative;
      height: auto;
      -webkit-box-sizing: border-box;
         -moz-box-sizing: border-box;
              box-sizing: border-box;
      padding: 10px;
      font-size: 16px;
    }
    .form-signin .form-control:focus {
      z-index: 2;
    }
    .form-signin input[type="email"] {
      margin-bottom: -1px;
      border-bottom-right-radius: 0;
      border-bottom-left-radius: 0;
    }
    .form-signin input[type="password"] {
      margin-bottom: 10px;
      border-top-left-radius: 0;
      border-top-right-radius: 0;
    }
    </style>
</head>
<body>
<div class="container">

  <form class="form-signin" action="." method="post">
    <h2 class="form-signin-heading">PRT Teamspeak Permissions</h2>
    <?php
    if ($response) {
        echo '<div class="alert alert-'.$response[0].'">'.$response[1].'</div>';
    }
    ?>
    <p>
        <label for="password" class="sr-only">password</label>
        <input type="password" id="password" name="password" class="form-control" placeholder="password" value="<?=$_POST["password"]?>" required autofocus>
    </p>
    <p>
        <label for="uid" class="sr-only">uid</label>
        <input type="text" id="uid" name="uid" class="form-control" placeholder="Teamspeak UID" required>
    </p>
    <div class="radio">
      <label style="margin-right: 20px;"><input type="radio" name="team" value="emc"<?php if ($_POST["team"]=="emc") echo ' checked="checked"'; ?>/>EMC</label>
      <label style="margin-right: 20px;"><input type="radio" name="team" value="apn"<?php if ($_POST["team"]=="apn") echo ' checked="checked"'; ?> />APN</label>
      <label><input type="radio" name="team" value="remove"<?php if ($_POST["team"]=="remove") echo ' checked="checked"'; ?> />REMOVE</label>
    </div>
    <div class="form-group">
      <label for="rank" class="sr-only">Select list:</label>
      <select class="form-control" name="rank" id="rank">
        <?php
        foreach ($ranks as &$rank) {
            $selected = "";
            if ($_POST["rank"] == $rank) $selected = ' selected="selected"';
            echo '<option value="'.$rank.'"'.$selected.'>'.$rank.'</option>';
        }
        ?>
      </select>
    </div>
    <button class="btn btn-lg btn-primary btn-block" type="submit">Go</button>
  </form>

</div>
</body>
</html>
